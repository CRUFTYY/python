import json
import hashlib
import csv
import datetime
import sys
import os


def respond(err, results=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(results),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }


def lambda_handler(event, context):
    try:
        csv_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), './tmp/headlines.csv'), 'r')
        field_names = ("Title", "Abstract", "Authors", "documentType", "entryDate", "pubdate", "DocumentURL", "startPage", "FindACopy")
        reader = csv.DictReader(csv_file, field_names)

        if event['pathParameters']:
            if 'month_day' in event['pathParameters']:
                the_day = datetime.datetime.strptime(event['pathParameters']['month_day'], '%m%d')
                return respond(None, get_headlines_by_date(reader, the_day))
            elif 'hash' in event['pathParameters']:
                return respond(None, get_headlines_by_hashcode(reader, event['pathParameters']['hash']))
        the_day = datetime.date.today()
        return respond(None, get_headlines_by_date(reader, the_day))
    except Exception, e:
        return respond(e)


def get_headlines_by_date(reader, the_day):
    results = []
    for row in reader:
        if the_day.strftime('%b %-d,') in row['pubdate']:
            results.append(get_hashed_row(row))
    return results


def get_headlines_by_hashcode(reader, hash_code):
    results = []
    for row in reader:
        hashed_row = get_hashed_row(row)
        if hashed_row['hash'] == hash_code:
            results.append(hashed_row)
    return results


def get_hashed_row(row):
    hash_code = hashlib.sha1(json.dumps({'title': row['Title'], 'abstract': row['Abstract'], 'pubdate': row['pubdate']}, sort_keys=True)).hexdigest()
    return {'hash': hash_code, 'title': row['Title'], 'abstract': row['Abstract'], 'pubdate': row['pubdate']}

######################################################################
######################################################################
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print lambda_handler([], [])
    else:
        print lambda_handler(sys.argv[1], [])