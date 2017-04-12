# A Log combiner and processor: translogrify

Translogrify is designed to limit the deluge of log emails that occurs in technical emails. 

## How it works

Rather than have individual alerts send emails on their own, translogrify collects each alert into a row of a table along with a severity code and a list of its intended recipents. On demand, emails can then be sent per-recipient with a given lookback and severity level.

## Installation

Translogrify can be installed from github: 

    git clone git@github.com:asteriske/translogrify.git ~/translogrify

    pip install ~/translogrify

After installing, update ~/.translogrify.conf with settings appropriate to your environment:

    [DEFAULT]
    mailfromaddr = fromaddr
    mysqlpass = mysqlpass
    mailpass = mailpass
    table = log
    mysqlhost = mysqlhost
    mysqluser = mysqluser
    db = translogrify 
    mailserver = server

Currently TLS on port 587 is assumed. 

Assign a MySQL user with CREATE privileges and then run 

    $ create_db_and_table

which will create the log db as specified in `.translogrify.conf`. 

## Usage

A new line is added to the log with an invocation like the following:

    $ log_update MESSAGE ALERT_LEVEL EMAIL1 EMAIL2 ...

To send email digests to each user with their messages from the last 12 hours with severity >= 3,

    $ send_tgy_email --lookback 6 --minlevel 3

Each recipient will then get a color-coded priority-sorted email like this:

![translogrify example](https://github.com/asteriske/asteriske.github.io/blob/master/img/translogrify.png)
