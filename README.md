# # RagCP

![CodeQL](https://github.com/Freyja-Folkvangr/ragpycp/workflows/CodeQL/badge.svg)

> RagCP is an open source control panel for rAthena. It is easy to install, mantain, it's written in Python and it uses Django Framework so that it is easy to add new features and integrate things.

[Discord](https://discord.gg/2Y92RMS)
--------|

# Requirements
Before installing RagCP there are certain tools and applications you will need which
differs between the varying operating systems available.

1. It is recommended to install on linux systems.
2. Make sure the host you'll use has access to your Ragnarok database.
3. Python Runtime | [Python 3.6 or newer](https://www.python.org/downloads/)
4. Your login table **MUST NOT HAVE ADDITIONAL COLUMNS**.
5. Your server **MUST** run with MD5 password encryption enabled by default (So if a server uses RagCP, you already know your password has some level of security).

WARNING: We do not give support for third party addons and/or mods that modify, add or remove columns of rAthena database tables, always install RagCP on a clean database structure and backup your data if something apocalyptic happens. We modify any existing login table and generate a backup.

For additional information refer to database migration files located at ``./users/migrations/`` from number 1 to 4.

# Installation

After setting up your environment, run the following commands:

Note that depending of your setup you'll have to run ``python`` or ``python3`` commands, also ``pip`` or ``pip3``.

Are you an advanced user that feels lazy about setting up the environment? We provided a ``Dockerfile``.

### 1. Create this environment variables to store database credentials

Log in to the server you'll use to run the CP and create the following environment variables.

- `DATABASE_PORT`

- `DATABASE_HOST`

- `DATABASE_USER`

- `DATABASE_PASSWORD`

- `DATABASE_NAME`


### 2. Add your domain to the whitelist

Create an environment variable called ``HOST`` which its value is the hostname where the CP is going to be located. Don't include ``https://``. More details on Environment Variables section.


### 3. Install python dependencies

`pip install -r requirements.txt`

### 4. Change some table's engine

rAthena uses MyISAM as table engine, run the following command to upgrade tables used by RagCP to InnoDB

`python manage.py convert-engine`

### 5. Run database migrations

Modifying ``login`` table to work with Django auth

`python manage.py migrate users`

Migrate all other database tables:

`python manage.py migrate`

### 6. Run the CP

This command ignores the whitelist and runs uwsgi on port 8000 to serve the web app, feel free to change the port and for more information refer to [Django documentation](https://docs.djangoproject.com/en/3.0/ref/django-admin/)

`python manage.py runserver 0.0.0.0:8000`

# Feature toggle

There are other configurations that you can change in order to customize RagCP to your taste.

Open file ```./ragcp/settings.py``` and search the string ```# User settings```, below that line are the variables you can change.

- ``FEED_ENABLED``: Enable or disable dynamic index that reads an  RSS Feed to populate news automatically. (default: True)

- ``STATIC_CONTENT``: Do not show post and RSS content, shows an static welcome page instead. (default: False)

- ``CHANGELOG_ENABLED``: Show changelog tab

- ``RAGCP_CHANGELOG``: Show RagCP commit messages to allow users stay up to date of what they can do with the CP. Requires CHANGELOG_ENABLED: True and GITHUB_TOKEN

- ``RATHENA_CHANGELOG``: Show rAthena commit messages to allow users stay up to date of what have changed on the server. Requires CHANGELOG_ENABLED: True and GITHUB_TOKEN

# Optional environment variables

List of other environment variables you need to configure in order to use optional features.

- ``RSS_FEED``: The URL of the RSS Feed that will generate the index page, if this setting is not configured it will default to RagCP feed. If you disable RSS Feed on ``settings.py``, an static page will be shown instead.

- `HOST`: The domain name your users will use to open the web page, for example ``freyja-ro.xyz``, ``octocat.xyz``, ``my-ro.net``.

- `DJANGO_SETTINGS_MODULE`: Leave blank for default, refer to Django documentation to use this feature

- ``GITHUB_TOKEN``: Github Token used to read RagCP changelog

- ``RAGCP_REPO_NAME``: Defines the name of the repository where RagCP will read commit messages to display a changelog.

- ``RATHENA_REPO_NAME``: Defines the name of the repository where RagCP will read commit messages to display a changelog.

**Note: If you are going to run RagCP by building a Docker image, set all environment variables on the ``Dockerfile`` instead**.

# Change the index page

You can change the content that is displayed on the homepage, to do so you have to modify its HTML content.

Content of the index page is located at:

`./ragcp/templates/index.html`

Static index content is located at

`./ragcp/templates/welcome_content.html`

In future versions, you'll be able to customize it from the CP (Django Admin).

# RSS Feed - Developer comments

We created a Zappier account for RagCP and configured a couple of ``Zaps`` that read new content from several sources such as our GitHub pull requests, rAthena pull requests, Facebook page, etc. in order to automate and centralice all our information into one place.

# Common issues

## RagCP does not looks as expected

This could happen on certain environments, if this is your case, run the following command, then restart the server.

`python manage.py collectstatic`

The command collects the static files located on ``STATIC_ROOT`` path configured in ``settings.py``

**Comment: There is an environment variable used by Heroku that is configured as follows:**

``DISABLE_COLLECTSTATIC=1``

We haven't tested that setting outside the Heroku environment, but you can take a try. Let us know your results.

