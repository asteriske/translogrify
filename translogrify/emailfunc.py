from __future__ import absolute_import

import argparse
import json
import numpy as np
import os
import pandas as pd
import pynliner
import pymysql
import smtplib
import sqlalchemy
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import translogrify.create

def parse_email_json(x):

    if x is not None:
        return(json.loads(x)['email'])
    else:
        return ''

def split_and_map(in_df, func):
    
    # add a column which is a clean list of addresses
    in_df.loc[:,'addr_list'] = in_df['recipient'].apply(parse_email_json)
    addr_df                  = in_df[in_df['addr_list'] != '']

    # explode the df, one address per line
    rows = []
    for i, row in addr_df.iterrows():
        for a in row.addr_list:
            rows.append([a,row.level,row.message,row.date])
    
    out_df = pd.DataFrame(rows,columns=['recipient','level','message','date'])
    
    # assumes we don't care a great deal about the return value, only execution
    for r in out_df.recipient.unique():
        
        try:
            func(out_df[out_df.recipient==r])

        except Exception as e:
            print(e)
        time.sleep(5)

def color_alert(data):
    
    color_dict = {1:'white',
                 2:'green',
                 3:'yellow',
                 4:'orange',
                 5:'red'}

    color_font_dict = {1:'black',
            2:'white',
            3:'black',
            4:'white',
            5:'white'}

    
    color      = color_dict[np.round(data)]
    color_font = color_font_dict[np.round(data)]

    return 'background-color: {COLOR}; color: {FONTCOLOR}'.format(COLOR=color,FONTCOLOR=color_font)


def send_email(in_df):

    config = translogrify.create.read_config()

    df = in_df.copy()
    df.sort_values(['level','date'],ascending=False,inplace=True)
    color_table = (df[["date","level","message"]]
            .style.applymap(color_alert, subset=['level']))
    
    toaddr = df.recipient.tolist()[0]
    fromaddr = config['mailfromaddr'] 

    msg = MIMEMultipart('alternative')
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log Alert"
     
    body = df[["date","level","message"]].to_string(index=False) 

    html_msg = pynliner.fromString(color_table.render()) 

    html = """
    <html>
    <head/>
    <body>
    {}
    </body>
    </html>
    """.format(html_msg)

    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    try: 
        server = smtplib.SMTP(config['mailserver'], 587)
        server.starttls()
        server.login(fromaddr, config['mailpass'])
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

    except Exception as e:
        print(e)

def send_log_emails(lookback_hr,min_level):

    config = translogrify.create.read_config()

    conn_str = "mysql+pymysql://{S}:{P}@{H}/{D}".format(S=config['mysqluser'],
            P=config['mysqlpass'],
            H=config['mysqlhost'],
            D=config['db'])

    engine = sqlalchemy.create_engine(conn_str)
    conn = engine.connect()

    if lookback_hr is None:
        lookback_hr = 24

    if min_level is None:
        min_level = 5

    print("Lookback: {}".format(lookback_hr))
    print("Min Severity: {}".format(min_level))

    retdf = pd.read_sql("""
        select *
        from {TABLE}
        where level >= {LEVEL}
        and date >= date_sub(now(), interval {HOUR} hour)
        """.format(LEVEL=min_level,
            TABLE=config['table'],
            HOUR=lookback_hr),conn)

    split_and_map(retdf,send_email)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser("MDF Emailer")

    parser.add_argument("--lookback",help="Number of hours to look back for logs")
    parser.add_argument("--minlevel",help="Minimum severity level to report")

    args = parser.parse_args()
    send_log_emails(args.lookback,args.minlevel)
