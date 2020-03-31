import requests
import json

"""
Modify these please
"""
url='http://XXX.XXX.XXX.XXX/ins'
switchuser='AAAA'
switchpassword='BBBB'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "sh ip int brie",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword))
rx_object = json.loads(response.text)
print rx_object
