#!/bin/env python

from pyrundeck import Rundeck
from pprint import pprint
import logging

rundeck_url='http://localhost:4440'
rundeck_url = os.environ.get('RUNDECK_URL')
    username = os.environ.get('RUNDECK_USER')
    password = os.environ.get('RUNDECK_PASS')
    assert rundeck_url, 'Rundeck URL is required'
    assert username, 'Username is required'
    assert password, 'Password is required'
rundeck_api_token='bsle4qPtUkxbqpHrIov4HMEqB0C8A5SL'

logging.getLogger().setLevel(logging.WARNING)

rundeck=Rundeck(rundeck_url, token=rundeck_api_token, api_version=23, verify=False)

pprint(rundeck.list_projects())
for project in rundeck.list_projects():
   pprint(rundeck.list_jobs(project['name']))
