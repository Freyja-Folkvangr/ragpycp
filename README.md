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
4. Your login table MUST NOT HAVE ADDITIONAL COLUMNS.
5. Your server MUST run with MD5 passwords enabled by default.

# Installation

After setting up your environment, run the following commands:

Note that depending of your setup you'll have to run python or python3 commands, also pip or pip3.

1. Create environment variables to store database credentials

Log in to the server you'll use to run the CP and create the following environment variables.

`DATABASE_PORT`

`DATABASE_HOST`

`DATABASE_USER`

`DATABASE_PASSWORD`

`DATABASE_NAME`

2. Add your domain to the whitelist

Create an environment variable called HOST which its value is the hostname where the CP is going to be located. Don't include https://

For example www.myragnarok.com

2. Install dependencies

`pip install -r requirements.txt`

3. Apply database changes

rAthena uses MyISAM as table engine, run the following command to upgrade tables used by RagCP to InnoDB

`python manage.py preinstall`

Then run database migrations

`python manage.py migrate users`

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

# Common issues

## RagCP does not looks as expected

This could happen on certain environments, if this is your case, run the following command, then restart the server.

`python manage.py collectstatic`

The command collects the static files into STATIC_ROOT

# Demo
I'm creating a Ragnarok server to play with friends, we'll be using RagCP, so feel free to take a look :)

[Freyja](https://freyja-ro.herokuapp.com)
