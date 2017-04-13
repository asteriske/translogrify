from __future__ import absolute_import, print_function

import argparse
import configparser
import json
import translogrify.create
import os
import pandas as pd
import sqlalchemy

def insert_log_entry(message, level, recipients):

    config = translogrify.create.read_config()
    
    conn_str = "mysql+pymysql://{S}:{P}@{H}/{D}".format(S=config['mysqluser'],
            P=config['mysqlpass'],
            H=config['mysqlhost'],
            D=config['db'])

    engine = sqlalchemy.create_engine(conn_str)

    meta = sqlalchemy.MetaData()
    meta.reflect(bind=engine)

    log_table = sqlalchemy.Table(config['table'],meta)

    ins = log_table.insert().values(level=level,
            message=message,
            recipient = recipients)

    with engine.connect() as con:
        try:
            con.execute(ins)
        except Exception as e:
            print(e)

def add_log_line_cli():

    config = translogrify.create.read_config()

    parser = argparse.ArgumentParser(description = "Take in a line to add to the translogrify log")

    parser.add_argument('message',type=str,nargs=1,
            help="Log file message")
    parser.add_argument('level',type=int,nargs=1,
            help="Level of alert")
    parser.add_argument('recipients',type=str,nargs='+',
            help="email addresses of relevant message recipients")

    args = parser.parse_args()

    recipients_json = json.dumps({"email":args.recipients})

    insert_log_entry(args.message[0], 
            args.level[0], 
            recipients_json)

def add_log_line(message, level, recipients):

    recipients_json = json.dumps({"email":recipients})

    insert_log_entry(message, 
            level, 
            recipients_json)


if __name__ == '__main__':

    add_log_line()
