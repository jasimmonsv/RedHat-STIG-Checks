#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000320 of DISA STIG RedHat_5-V1R1
#20 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Accounts sharing a UID have full access to each others' files.  This has the same effect as sharing a login.  There is no way to assure identification, authentication, and accountability because the system sees them as the same user. If the duplicate UID is 0, this gives potential intruders another privileged account to attack.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Perform the following to ensure there are no duplicate UIDs:
#
## cut -d: -f3 /etc/passwd | uniq -d
#
#If any duplicate UIDs are found, this is a finding.
#
#Fix Text: 
#Edit user accounts to provide unique UIDs for each account.
#
#IA Controls:IAIA-1, IAIA-2
#CCI: CCI-000764
#NIST SP 800-53A :: IA-2.1
#NIST SP 800-53 :: IA-2

import os

def run():
	f = os.popen("cut -d: -f3 /etc/passwd | uniq -d")
	if f.read() == '':
		return 1
	else: return 0

run()
