#!/usr/bin/env python

""" 
@add/remove user(s) to multiply groups 
@Ver. 1.02 
@Author: R.Slipchenko 
### Your improvements are welcome! ###
### Script requires GAM configured! ###
### Replace gam_dir var. with your value! ### 
"""

import sys
import os

#domain = '@****.com'
#gam_dir = '~/gam/gam.py'
domain = '@****.com'
gam_dir = '~/**gam/gam.py'
gam_file = 'gam_list.txt'
gam_py = gam_dir + ' batch ' + gam_file 
trunc_file = ">"+gam_file

group_dict = {}

def add_user():
	global users_list
	add_users = raw_input("Enter users, comma separated:\n")
	users_list = add_users.split(",")
	return users_list

def add_group():
	global groups_list
	add_groups = raw_input("Enter mail lists, comma separated:\n")
	groups_list = add_groups.split(",")
	return groups_list

def groups_add():
	group_dict['grp_email'] = raw_input("Enter group address, without domain:\n")
	group_dict['grp_name'] = raw_input("Enter group name:\n")
	group_dict['grp_desc_key'] = raw_input("Enter JIRA ticket number(IP):\n")
	group_dict['grp_desc'] = raw_input("Enter group description:\n")
	return None

def actions():
	global action
	#Looping the input
	while True:
		action = raw_input("Choose action (Enter a digit) [4]:\n1.Add user(s) to groups\n2.Remove member(s) from group\n3.Create new group\n4.Exit\n")
		if action == str(1) or action == str(2) or action == str(3) or action == str(4):
			break
		else:
			print "Only 1,2,3 or 4!"
		#Forming lists
	if action == str(1) or action == str(2):
		users_list = set([x.strip(' ') for x in add_user()])
		groups_list = set([x.strip(' ') for x in add_group()])
	elif action == str(3): 
		groups_add()
	else:
		sys.exit('Bye.')
	return action	
	
def length_check():
	if action == str(1) or action == str(2):
		if '' in users_list:
			#print users_list
			print 'Empty users list!'
			return 1
		elif '' in groups_list:
			#print groups_list
			print 'Empty groups list!'
			return 1
	elif action == str(3):
		for k in group_dict:
			if not group_dict[k]:
				print "Empty!", k
				return 1

def actionDo(action):
	with open(gam_file, 'a') as users:
		for l in groups_list:
			for u in users_list:
				#Debug:
				#print ('gam update group ' + str(l) +  ' ' + action + ' member ' + str(u) + "\n")
				try:
				    users.write('gam update group ' + str(l) +  ' ' + action + ' member ' + str(u) + "\n")
				except Exception:
				    pass

def createGroup():
	with open(gam_file, 'a') as groups:
				#Debug:
				#print 'gam create group '+group_dict['grp_email']+domain+' '+'name '+"'"+group_dict['grp_name']+"'"+' '+'description '+"'"+group_dict['grp_desc_key']+':'+group_dict['grp_desc']+"'"+"\n" \
				    #+'commit-batch'+"\n" \
				    #+'gam update group '+group_dict['grp_email']+domain+' who_can_post_message anyone_can_post'+"\n" \
				    #+'gam update group '+group_dict['grp_email']+domain+' who_can_view_membership all_in_domain_can_view'  	
				try:
				    groups.write('gam create group '+group_dict['grp_email']+domain+' '+'name '+"'"+group_dict['grp_name']+"'"+' '+'description '+"'"+group_dict['grp_desc_key']+':'+group_dict['grp_desc']+"'"+"\n" \
				    +'commit-batch'+"\n" \
				    +'gam update group '+group_dict['grp_email']+domain+' who_can_post_message anyone_can_post'+"\n" \
				    +'commit-batch'+"\n" \
				    +'gam update group '+group_dict['grp_email']+domain+' who_can_view_membership all_in_domain_can_view'+"\n" \
				    +'commit-batch'+"\n" \
				    )
				except Exception:
				    pass

def perform_action():
	if action == str(1):
		actionDo('add')
	elif action == str(2):
		actionDo('remove')
	elif action == str(3):
		createGroup()
	return action		
	
def gam_run():
	os.system(gam_py)
	os.system(trunc_file)
								
actions()

while length_check() == 1:
	actions()

perform_action()
gam_run()

	

	

		
