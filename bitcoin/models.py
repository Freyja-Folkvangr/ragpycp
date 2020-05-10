from django.db import models

# Create your models here.
from ragcp import settings
import blockchain

from ragcp.settings import logger
from users.models import Login


class Wallet(models.Model):
    identifier = models.CharField(primary_key=True, max_length=255)
    friendly_name = models.TextField(db_index=True)
    password = models.TextField()
    api_code = models.TextField()

    @property
    def service_url(self):
        if settings.host[-1] == '/':
            return settings.host
        else:
            return settings.host + '/'

    """
    An instance of the Wallet class needs to be initialized before it can be used.
    identifier : str
    password : str
    service_url : str - URL to an instance of service-my-wallet-v3 (with trailing slash)
    second_password : str (optional)
    api_code : str (optional)
    """

    @property
    def wallet(self) -> blockchain.wallet.Wallet:
        return blockchain.wallet.Wallet(self.identifier, self.password, self.service_url, None, self.api_code)

    """
    Send bitcoin from your wallet to a single address. Returns a PaymentResponse object.
    to : str - receiving address
    amount : int - amount to send (in satoshi)
    from_address : str - specific address to send from (optional)
    fee : int - transaction fee in satoshi. Must be greater than default (optional)
    note : str - public note to include with the transaction if amount >= 0.005 BTC (optional)
    """

    def send(self, to: str, amount: int, from_address: str, fee: int,
             note: str = None) -> blockchain.wallet.PaymentResponse:
        if amount >= 500000 and note:
            response = self.wallet.send(to, amount, from_address, fee, note)
        else:
            logger.info('Could not add note to transaction due to min amount restriction')
            response = self.wallet.send(to, amount, from_address, fee)

        PaymentResponse(from_address=Address.objects.get(address=from_address),
                        to_address=Address.objects.get(address=to), amount=amount, message=response.message,
                        tx_hash=response.tx_hash, notice=response.notice).save()
        return response

    """
    Send bitcoin from your wallet to multiple addresses. Returns a PaymentResponse object.
    recipients : dictionary - dictionary with the structure of 'address':amount
    from_address : str - specific address to send from (optional)
    fee : int - transaction fee in satoshi. Must be greater than default (optional)
    note : str - public note to include with the transaction if amount >= 0.005 BTC (optional)
    """
    def send_many(self, recipients: dict, from_address: str, fee: int = 0,
                  note: str = None) -> blockchain.wallet.PaymentResponse:
        from_address_obj = Address.objects.get(address=from_address)
        if note:
            response = self.wallet.send_many(recipients, note)
        else:
            response = self.wallet.send_many(recipients)

        for address in recipients.keys():
            PaymentResponse(
                from_address=from_address_obj,
                to_address=Address.objects.get(address=address),
                amount=recipients[address],
                message=response.message,
                tx_hash=response.tx_hash,
                notice=response.notice
            ).save()
        return response

    """
    Fetch the wallet balance. Includes unconfirmed transactions and possibly double spends. Returns the wallet balance in satoshi.
    """

    @property
    def balance(self):
        return self.wallet.get_balance()

    """
    List all active addresses in the wallet. Returns an array of Address objects.
    confirmations : int - minimum number of confirmations transactions must have before being included in balance of addresses (optional)
    """

    @property
    def addresses(self) -> [blockchain.wallet.Address]:
        return self.wallet.list_addresses()

    """
    Archive an address. Returns a string representation of the archived address.
    address : str - address to archive
    """

    def archive_address(self, address) -> str:
        return self.wallet.archive_address(address)

    """
    Unarchive an address. Returns a string representation of the unarchived address.
    address : str - address to unarchive
    """

    def unarchive_address(self, address) -> str:
        return self.wallet.unarchive_address(address)

    """
    Retrieve an address from the wallet. Returns an Address object.
    confirmations : int - minimum number of confirmations transactions must have before being included in the balance (optional)
    """

    def get_address(self, address: str, confirmations: int = 0):
        return self.wallet.get_address(address, confirmations=confirmations)

    def new_address(self, label: str) -> blockchain.wallet.Address:
        if label == 'main':
            blockchain_address = self.wallet.new_address(label)
            system_user = Login.objects.filter(sex='S').first()
            new_address = Address(address=blockchain_address.address, user=system_user, wallet=self)
            new_address.save()
            return blockchain_address
        else:
            return self.wallet.new_address(label)

    def get_address_by_label(self, label: str) -> blockchain.wallet.Address:
        for address in self.addresses:
            if address.label == label:
                return address
        return self.new_address(label)

    @property
    def main_address(self):
        return self.get_address_by_label('main')


class Address(models.Model):
    address = models.CharField(primary_key=True, max_length=255)
    user = models.OneToOneField(Login, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    @property
    def balance(self):
        return self.wallet.get_address(self.address).balance

    @property
    def label(self):
        return self.wallet.get_address(self.address).label

    @property
    def total_received(self):
        return self.wallet.get_address(self.address).total_received

    def deduct(self, amount, note='') -> blockchain.wallet.PaymentResponse:
        return self.wallet.send(self.wallet.main_address.address, amount, self.address, 0, note)

    # This allows the user to withdraw their unused money
    def withdraw(self, amount, to, note='Withdraw from Freyja RO using RagCP'):
        return self.wallet.send(to, amount, self.address, 0, note)

    def archive(self) -> str:
        return self.wallet.archive_address(self.address)

    def unarchive(self) -> str:
        return self.wallet.unarchive_address(self.address)


class PaymentResponse(models.Model):
    from_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='from_addresses')
    to_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='to_addresses')
    amount = models.BigIntegerField()
    message = models.TextField()
    tx_hash = models.TextField()
    notice = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
