import re
from setuptools import setup

version = re.search(
        '^__version__\s*=\s*"(.*)"',
        open('translogrify/translogrify.py').read(),
        re.M
        ).group(1)

with open("README.md","rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
        name = "translogrify",
        packages = ["translogrify"],
        install_requires = ["appdirs>=1.4.3",
            "beautifulsoup4>=4.5.3",
            "configparser>=3.5.0",
            "cssutils>=1.0.2",
            "Jinja2>=2.9.6",
            "MarkupSafe>=1.0",
            "numpy>=1.12.1",
            "packaging>=16.8",
            "pandas>=0.19.2",
            "PyMySQL>=0.7.11",
            "pynliner>=0.8.0",
            "pyparsing>=2.2.0",
            "python-dateutil>=2.6.0",
            "pytz>=2017.2",
            "six>=1.10.0",
            "SQLAlchemy>=1.1.9"],
        setup_requires = ["SQLAlchemy>=1.1.9"],

        entry_points = {
            "console_scripts": ['create_db_and_table = translogrify.create:create_db_and_table',
                'log_update = translogrify.log_update:add_log_line',
                'send_tgy_email = translogrify.send_email:send_email']
            },
        version = version,
        description = "Log combiner and processor",
        long_description = long_descr,
        author = "Patrick McCarthy",
        author_email = "patrickjmc@gmail.com",
        url = "http://asteriske.github.io",
        )
#from translogrify import create, send_email
#create.write_new_config()
