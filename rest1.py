import requests
from requests.auth import HTTPDigestAuth
import json



user = requests.get("http://localhost:3317",auth=HTTPDigestAuth(raw_input("userName: "), raw_input("password: ")), verify=True) #ask for creds in run time

if(user.ok):

    jData = json.loads(user.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
        print key + " : " + jData[key]
else:

    user.raise_for_status()