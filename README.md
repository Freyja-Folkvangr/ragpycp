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

rAthena uses MyISAM as table engine, run the following command to upgrade them to InnoDB

`python manage.py preinstall`

`python manage.py migrate users --fake-initial`

The following migration has a RagCP known issue

`python manage.py migrate admin`

3.5 Collects the static files into STATIC_ROOT

`python manage.py collectstatic`

Finally run:

`python manage.py migrate`

4. Run the CP

This command ignores the whitelist, for more information refer to [Django documentation](https://docs.djangoproject.com/en/3.0/ref/django-admin/)

`python manage.py runserver 0.0.0.0:80`

# Change the index page

You can change the content that is displayed on the homepage, to do so you have to modify its HTML content.

Content of the index page is located at:

`./ragcp/templates/index.html`

In future versions, you'll be able to customize it from the CP (Django Admin).
