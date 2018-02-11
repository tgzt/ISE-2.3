import sys
sys.path.append(r"C:\Users\TomG\Documents\Python ISE\ISE-2.3")
"""
requires xmltodict
"""
from cream import ERS
def test_IUSR():
	ise = ERS(ise_node='192.168.2.11', ers_user='ers', ers_pass='restM0', verify=False, disable_warnings=True)
	sys.stdout = open('test_IUSR.txt','w')
	# USERS
	r = ise.get_users()['response']
	if r != []:
			for element in r:
					print ("USER:",element[0])
					print ("UUID:",element[1])
					rr=ise.get_user(user_id=element[0])['response']
					print("GROUP:",rr['identityGroups'])
	else:
			print("NO USERS")
	rid=ise.get_identity_group('Employee')['response']['@id']
	print ("ADD USER(Employee):",rid)
	r3 = ise.add_user(user_id='EMP002', password='Testing1', user_group_oid=rid)
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
	
