import sys
import re
import pprint # debugging
r = []
sys.path.append(r"C:\Users\TomG\Documents\Python ISE\ISE-2.3")
"""
read 'macadd.txt' and 'macdel.txt' to add and delete endpoints, respectively
if a MAC (EP) already exists then update its identity group (EPG)
specify the defaultEPG for an installation
"""
defaultEPG = 'HRSA_Mobile'

from cream import ERS
ise = ERS(ise_node='192.168.2.11', ers_user='ers', ers_pass='restM0', verify=False, disable_warnings=True, timeout=6)

def iseMACadd():
	global r
	with open('macadd.txt','r') as f:
		for line in f:
			r = line.split()
			mac = r[0].replace(".",":")

			if ise._mac_test(mac): # MAC seems valid
				try:
					group = r[1]
				except:
					group = "HRSA_Mobile"
				print('Adding',mac,)
				r = ise.get_endpoint_group(group)
				if r['success']: # EPG was found
					gid = r['response']['@id']
					print('   as',group,gid)
					rr = ise.get_endpoint(mac)
					if rr['success']: # EP/FOUND already exists ... update EPG
						epid = rr['response']['@id']
						print('   mac exists',mac,epid)
						r = ise.update_epg_endpoint(mac,epid,gid)
						if r['success']:
							print('   updated to group',group,gid)
							print('...success')
						else:
							print('...error')
							pprint.pprint(r)
					else: # EP/MAC not found ... add 
						r = ise.add_endpoint(mac,gid)
						if r['success']:
							print('...successfully added')
						else:
							print('...error adding') 
				else:
					print('   iseMACadd/unknown Identity Group',group)
			else:
				print('   iseMACadd/invalid MAC',mac)
			
def iseMACdel():
	try:
		f = open('macdel.txt','r')
	except:
		print('no MAC endpoints to delete')
	else:
		for line in f:
			l = line.split()
			mac = l[0].replace(".",":")
			if ise._mac_test(mac):
				print('Delete',mac)
				r = ise.delete_endpoint(mac)
				if r['success']:
					print('...success')
			else:
				print('iseMACdel/invalid MAC',mac)
		print ('... deletion(s) complete')

if __name__ == "__main__":
	iseMACadd()
	iseMACdel()