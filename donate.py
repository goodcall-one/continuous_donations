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

    url = "https://www.goodcall.one/api/v1/donate"

    r = requests.post(url, json=body_para, headers=headers)
    response = json.loads(r.text)

    if r.status_code == requests.codes.ok:
        print("Request successful")
    else:
        print("Something went wrong. \n Your error code is: " + str(r.status_code))
        sys.exit(1)

    print(f"::set-output name=response::{response}")

if __name__ == "__main__":
    main()
