import sys
import pytest
sys.path.append(r"C:\Users\TomG\Documents\Python ISE\ISE-2.3")
"""
requires xmltodict
"""
from cream import ERS
 
def test_EPG():
	ise = ERS(ise_node='192.168.2.11', ers_user='ers', ers_pass='restM0', verify=False, disable_warnings=True)
	sys.stdout = open('test_EPG.txt','w')
	# Endpoint Group
	print ("EPG:")
	r = ise.get_endpoint_groups()
	for element in r['response']:
		print ("NAME:",element[0])
		print ("UUID:",element[1])
		print ("DESC:",element[2])
		rr = ise.get_endpoint_group(element[0])['response']
		print ("SYST:",rr['systemDefined'])
		print ("***")
	assert r['success']