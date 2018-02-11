import base64
import requests
import xmltodict
import json
import pprint
import os
requests.packages.urllib3.disable_warnings()
base_dir = os.path.dirname(__file__) ; print ('CREAM: running from %s' % base_dir)
ise = "192.168.2.11"
user = "admin"
pwd  = "Cangetin1"
url = "https://{0}/admin/API/mnt/Version".format(ise)

auth=(user,pwd)

headers = {'Content-Type': 'application/xml', 'Accept': 'application/xml'}

response = requests.get(url, headers=headers, auth=auth, verify=False)
if response.ok:
	r = json.loads(json.dumps(xmltodict.parse(response.content)))
	pprint.pprint(r)
	print (r['product']['version'])
else:
	print (response)