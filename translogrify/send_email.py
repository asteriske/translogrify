from __future__ import absolute_import

import argparse
import translogrify.emailfunc

def send_email():

    lookback = 12
    minlevel = 5

    parser = argparse.ArgumentParser("Translogrify Emailer")

    parser.add_argument("--lookback",help="Number of hours to look back for logs")
    parser.add_argument("--minlevel",help="Minimum severity level to report")

    args = parser.parse_args()

    if args.lookback is not None:
        lookback = args.lookback

    if args.minlevel is not None:
        minlevel = args.minlevel

    translogrify.emailfunc.send_log_emails(lookback,minlevel) 

if __name__ == "__main__":

    send_email()
