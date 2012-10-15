#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000450 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Limiting simultaneous user logins can insulate the system from denial of service problems caused by excessive logins.  Automated login processes operating improperly or maliciously may result in an exceptional number of simultaneous login sessions.
#
#If the defined value of 10 logins does not meet operational requirements, the site may define the permitted number of simultaneous login sessions based on operational requirements.
#
#This limit is for the number of simultaneous login sessions for EACH user account.  This is NOT a limit on the total number of simultaneous login sessions on the system.
#
#Documentable: Yes
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Check for a default maxlogins line in the /etc/security/limits.conf and /etc/security/limits.d/* files.
#
#Procedure:
##grep maxlogins /etc/security/limits.conf /etc/security/limits.d/*
#
#The default maxlimits should be set to a max of 10 or a documented site defined number:
#
#* - maxlogins 10
#
#If no such line exists, this is a finding.
#
#Fix Text: 
#Add a "maxlogins" line such as "* hard maxlogins 10" to /etc/security/limits.conf or a file in /etc/security/limits.d. The enforced maximum should be defined by site requirements and policy.
#
#IA Controls:ECSC-1
#CCI: CCI-000054
#NIST SP 800-53 :: AC-10
#NIST SP 800-53A :: AC-10.1 (ii)

import os

def run(f):
	maxLoginLimit = 10
	f = os.popen('grep maxlogins /etc/security/limits.conf').read()	
	while len(f) > 0:
		if f[0] == '#':
			fnl = f.find('\n')+1 #\n counts as one character
			f = f[fnl:]
		else:
			g=f.find('maxlogins')
			if g > 0 : 
				f=f[g:]
				h=f.split()
				if h[2]>maxLoginLimit: return 1
	return 0

run()
