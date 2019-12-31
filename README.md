# # RagCP
> RagCP is an open source control panel for rAthena. It is easy to install, mantain, it's written in Python and it uses Django Framework so that it is easy to add new features and integrate things.

[Discord](https://discord.gg/2Y92RMS)
--------|

# Requirements
Before installing RagCP there are certain tools and applications you will need which
differs between the varying operating systems available.

1. It is recommended to install on linux systems.
2. Make sure the host you'll use has access to your Ragnarok database.
3. Python Runtime | [Python 3 or newer](https://www.python.org/downloads/)

# Installation

After setting up your environment, run the following commands:

Note that depending of your setup you'll have to run python or python3 commands, also pip or pip3.

1. Modify database credentials

Edit the file `./ragcp/settings.py`, find this pattern: *`DATABASES =`*  and change the credentials to the ones you use on your server.

2. Add your domain to the whitelist

In the same file, find this pattern: *`ALLOWED_HOSTS =`* and add to the list your domain, for example: www.myragnarok.com

2. Install dependencies

`pip install -r requirements.txt`

3. Apply database changes

`python manage.py migrate`

4. Run the server

This command ignores the whitelist, for more information refer to [Django documentation](https://docs.djangoproject.com/en/3.0/ref/django-admin/)

`python manage.py runserver 0.0.0.0:80`
