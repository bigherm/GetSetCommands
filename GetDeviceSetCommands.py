#!/usr/bin/env python3

'''
    This script will get the Mist commands that are sent to Juniper devices.
'''

import requests
import json
import os
import datetime

# Create a list of the site device, use the device IDs.
device_list = [
    '',
    ''
    ]

# Get the current time and date when the program is executed.
my_today = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")

token_id = 'InsertTokenHere'
site_id = 'InsertSiteID'

headers = {
    'Content-Type': 'application/json',
    'Authorization': token_id
}

# Loop through the device_list, get the device name and the commands and save to a file.
for device in device_list:
    device_url = f'https://api.mist.com/api/v1/sites/{site_id}/devices/{device}'
    config_url = f'{device_url}/config_cmd'

    # Get the device name
    d_name = requests.get(device_url, headers=headers)
    device_name = (json.loads(d_name.text)['name'])

    cmd_response = requests.get(config_url, headers=headers)
    cmd_info = json.loads(cmd_response.text)

    with open("AIDEconfig.json", "a") as json_file:
        # Write the current time when the script is executed.
        json_file.write(f'\n{my_today} Device Name: {device_name} with ID:  {device}\n')

        # Write the json information.
        json.dump(cmd_info, json_file, indent=2)
