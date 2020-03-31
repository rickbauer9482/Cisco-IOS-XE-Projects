import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('AAAA', 'BBBB')
    myheaders = {'Content-Type': 'application/json'}
    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show version",
            "output_format": "json"
  }
}
url='http://XXX.XXX.XXX.XXX/ins'
response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=auth)
#for key in response.keys():
#     print "response includes", key
# print 'Status Code: ' + str(response.status_code)
rx_object = json.loads(response.text)
print json.dumps(rx_object, indent=4)
simple = rx_object['ins_api']['outputs']['output']['body']
