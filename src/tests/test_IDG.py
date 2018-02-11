import sys
import pytest
sys.path.append(r"C:\Users\TomG\Documents\Python ISE\ISE-2.3")
"""
requires xmltodict
"""
from cream import ERS
 
def test_IDG():
	ise = ERS(ise_node='192.168.2.11', ers_user='ers', ers_pass='restM0', verify=False, disable_warnings=True)
	r = ise.get_identity_groups()
	sys.stdout = open('test_IDG.txt','w')
	print ("IDENTITY GROUPS")
	for element in r['response']:
		print ("NAME:",element[0])
		print ("UUID:",element[1])
		print ("DESC:",element[2])
		print ("HREF:",element[3])
		rr = ise.get_identity_group(element[0])
		#print (rr['success'])
		if rr['success']:
			print ('PARENT',rr['response']['parent'])
		print ("***")
	assert r['success']