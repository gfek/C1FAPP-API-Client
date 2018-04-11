# -*- coding: utf-8 -*-
import json
import sys
import os
import argparse
import sys
import re
import requests
from prettytable import PrettyTable
from colorama import init
from termcolor import colored

init()

def c1fapp_res(search,api):
	session=requests.Session()
	url = "https://www.c1fapp.com/cifapp/api/"
	payload = {'key':api,
		'format': 'json',
		'backend':'es',
		'request':search
		}

	c1fapp_query = session.post(url, data=json.dumps(payload),timeout=10)
	results = json.loads(c1fapp_query.text)
	return results

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(prog="c1fapp.py",description='C1fapp Threat Intel API Search.')
	parser.add_argument("-s", action="store", dest='search', help="Search ip/domain/url",required=True)
	parser.add_argument("-k", action="store", dest='api', help="c1fapp api key",required=True)
	parser.add_argument("-v", action="version",version="%(prog)s v1.0")
	args = parser.parse_args()

	try:
		c1fapp_res=c1fapp_res(args.search,args.api)
	except ValueError:
		print colored("No JSON object could be decoded.",'red')
		sys.exit(-1)

	c1fappTab = PrettyTable(["feed label",
		"domain", 
		"description", 
		"assessment",
		"confidence",
		"reportime",
		"ipaddress",
		"asn",
		"derived"
	])

	if len(c1fapp_res) > 0:
		for res in c1fapp_res:
			if isinstance(res['confidence'][0],int):
				c1fappTab.add_row([''.join(res['feed_label']), 
					''.join(res['domain']),
					''.join(res['description']), 
					''.join(res['assessment']),
					''.join(str(res['confidence'])[1:-1]),
					''.join(res['reportime']),
					''.join(res['ip_address']),
					''.join(res['asn']),
					''.join(res['derived']),
					])
			else:
				c1fappTab.add_row([''.join(res['feed_label']), 
					''.join(res['domain']),
					''.join(res['description']), 
					''.join(res['assessment']),
					''.join(res['confidence']),
					''.join(res['reportime']),
					''.join(res['ip_address']),
					''.join(res['asn']),
					''.join(res['derived'])
					])
	else:
		print colored("No data found for the search {}.".format(args.search), 'yellow')
		sys.exit(-1)

	print colored(c1fappTab,'cyan')