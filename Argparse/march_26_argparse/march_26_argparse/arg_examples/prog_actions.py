import argparse
import datetime as dt


parser = argparse.ArgumentParser()
parser.add_argument('action', choices=['get_date', 'get_datetime', 'get_utc'])
args = parser.parse_args()

if args.action == 'get_date':
    print(dt.date.today())
elif args.action == 'get_datetime':
    print(dt.datetime.now())
