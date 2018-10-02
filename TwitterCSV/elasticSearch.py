#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:26:15 2018

@author: navneet
"""
#sending data via elasticsearch api python
import requests
from elasticsearch import Elasticsearch,helpers
import csv

username = "admin"
password = "BAZHTLDKOQSWOTFM"

es = Elasticsearch([
    {'host': 'portal-ssl50-37.bmix-dal-yp-84784341-8295-4791-ab69-853ad7d5dd46.4264710258.composedb.com', 'port': 58391, 'use_ssl': True},        
],http_auth=(username,password))


with open('/home/hp/Desktop/TwitterCSV/sampleTweet.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es,reader,index='testtweet',doc_type='testTweetData')
    
#request for authentication for get in elasticsearch

#url ='https://portal-ssl50-37.bmix-dal-yp-84784341-8295-4791-ab69-853ad7d5dd46.4264710258.composedb.com:58391/_cat/indices?v'
#res = requests.get(url, auth=(username, password))
#print(res.content)



