from django.db import models

# Create your models here.
class Patcher(models.Model):
    name = models.CharField(max_length=128, null=True, default=True, db_index=True, help_text='Friendly name, used as index for security reasons, use dashes instead of spaces, avoid special characters and use an URL-friendly name')
    allow = models.BooleanField(default=True, null=False, help_text='Allow patching or not')
    force_start = models.BooleanField(default=False, null=False, help_text='Should patcher ignore everything else and finish patch immediately?')
    policy_msg = models.TextField(null=False, default='Under maintenance', blank=True, help_text='if the patcher is ignoring updates, what message should appear?')
    file_url = models.TextField(null=False, blank=False, default='http://domain.com/patch/data/', help_text='http://domain.com/patch/data/')
    client_sum = models.TextField(null=False, blank=True, default='', help_text='use CheckSum tool, hash for client & patcher used to make sure exe is up to date (leave empty to disable this feature)')
    patcher_sum = models.TextField(null=False, blank=True, default='', help_text='use CheckSum tool, hash for client & patcher used to make sure exe is up to date (leave empty to disable this feature)')
    client_path = models.CharField(max_length=128, null=False, blank=True, default='', help_text='This is compressed file for patcher & client update, for example client.thor')
    patcher_path = models.CharField(max_length=128, null=False, blank=True, default='', help_text='This is compressed file for patcher & client update, for example patcher.thor')
    fragment_limit = models.SmallIntegerField(null=False, default=50, help_text='Set a limit for fragment, when reach this limit, patcher will ask user to defrag')

    class Meta:
        unique_together = [['client_path', 'name'], ['patcher_path', 'name']]

    def __str__(self):
        return '%s: %s' % (self.pk, self.name)

    @property
    def num_clients(self):
        return self.customclient_set.count()


class Update(models.Model):
    patcher = models.ForeignKey(Patcher, on_delete=models.CASCADE, help_text='Patch client that will receive the update')
    created = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=128, null=False, help_text='.thor filename')

    class Meta:
        unique_together = [['filename', 'patcher']]

    def __str__(self):
        return '%s: %s' % (self.pk, self.filename)

class CustomClient(models.Model):
    patcher = models.ForeignKey(Patcher, on_delete=models.CASCADE, help_text='Patch client that will perform these file checks')
    name = models.CharField(max_length=128, null=True, default=True, help_text='_Name - Filename of exe')
    created = models.DateTimeField(auto_now_add=True)
    checksum = models.CharField(max_length=128, null=False, default=None, help_text='_sum - checksum, use CheckSum tool.')
    path = models.CharField(max_length=128, null=False, blank=True, default=None, help_text='.thor _Path - Path for file [Compressed]')

    class Meta:
        unique_together = [['path', 'patcher']]

    def __str__(self):
        return '%s' % self.name