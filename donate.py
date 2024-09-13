#!/usr/bin/python3
import os
import requests
from urllib.parse import urljoin
import posixpath
import json
import sys
import re

def main():
    api_key = os.environ["INPUT_APIKEY"]
    organization_id = os.environ["INPUT_ORGANIZATION_ID"]
    wallet_id = os.environ["INPUT_WALLET_ID"]
    user = os.environ["INPUT_USER"]
    test = os.environ["INPUT_TEST"]

    body_para = {
        "organization_id": organization_id,
        "wallet_id": wallet_id,
        "user": user,
        "test": test
    }
    headers = {"x-api-key": api_key}

    # Construct URL with query parameters
    url = f"https://www.goodcall.one/api/v1/donate?organization_id={organization_id}&wallet_id={wallet_id}&user={user}&test={test}"

    # Make the POST request with query parameters and headers
    r = requests.post(url, headers=headers)

    # Check if the response is successful
    if r.status_code == 400:
        print(f"Error 400: {r.text}")  # Log the detailed error message
        sys.exit(1)
    
    response = r.json()  # Parse the response JSON

    if r.status_code == requests.codes.ok:
        print("Request successful")
    else:
        print(f"Something went wrong. \n Your error code is: {r.status_code}")
        sys.exit(1)

    # Output the response
    print(f"::set-output name=response::{json.dumps(response)}")

if __name__ == "__main__":
    main()
