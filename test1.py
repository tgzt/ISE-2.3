import sys
sys.path.append(r"C:\Users\TomG\Documents\Python ISE\ISE-2.3")
"""
requires xmltodict
"""
from cream import ERS
ise = ERS(ise_node='192.168.2.11', ers_user='ers', ers_pass='restM0', verify=False, disable_warnings=True)
print('ise setup')
r = ise.get_identity_groups()['response']
print ("IDENTITY GROUPS")
for element in r:
	print ("NAME:",element[0])
	print ("UUID:",element[1])
	print ("DESC:",element[2])
	print ("HREF:",element[3])
	rr = ise.get_identity_group(element[0])
	#print (rr['success'])
	if rr['success']:
		print ('PARENT',rr['response']['parent'])
	print ("***")
# Endpoint Group
print ("EPG:")
r = ise.get_endpoint_groups()['response']
for element in r:
	print ("NAME:",element[0])
	print ("UUID:",element[1])
	print ("DESC:",element[2])
	rr = ise.get_endpoint_group(element[0])['response']
	print ("SYST:",rr['systemDefined'])
	print ("***")
# USERS
r = ise.get_users()['response']
for element in r:
	print ("USER:",element[0])
	print ("UUID:",element[1])
	rr=ise.get_user(user_id=element[0])['response']
	print("GROUP:",rr['identityGroups'])
print ("ADD USER:")
r3 = ise.add_user(user_id='EMP002', password='Testing1', user_group_oid=rr['identityGroups'])
r = ise.get_users()['response']
for element in r:
	print ("USER:",element[0])
	print ("UUID:",element[1])
	rr=ise.get_user(user_id=element[0])['response']
	print("GROUP:",rr['identityGroups'])
print ("DEL USER:")
r = ise.delete_user(user_id='EMP002')
r = ise.get_users()['response']
for element in r:
	print ("USER:",element[0])
	print ("UUID:",element[1])
	rr=ise.get_user(user_id=element[0])['response']
	print("GROUP:",rr['identityGroups'])