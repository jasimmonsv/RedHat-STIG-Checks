#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000452 of DISA STIG RedHat_5-V1R1
#25 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Providing users with feedback on when account accesses last occurred facilitates user recognition and reporting of unauthorized account use.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Check that pam_lastlog is used and not silent, or that the SSH daemon is configured to display last login information.
#
## grep pam_lastlog /etc/pam.d/sshd
#If pam_lastlog is present, and does not have the "silent" option, this is not a finding.
#
## grep -i PrintLastLog /etc/ssh/sshd_config
#
#If PrintLastLog is not present in the configuration, this is not a finding. This is the default setting.
#If PrintLastLog is present in the configuration and set to "yes" (case insensitive), this is not a finding.
#Otherwise, this is a finding.
#
#Fix Text: 
#Implement pam_lastlog, or enable PrintLastLog in the SSH daemon.
#
#To enable pam_lastlog, add a line such as "session required pam_lastlog.so" to /etc/pam.d/sshd.
#
#To enable PrintLastLog in the SSH daemon, remove any lines disabling this option from /etc/ssh/sshd_config. 
#
#IA Controls:ECSC-1
#CCI: CCI-000052
#NIST SP 800-53 :: AC-9
#NIST SP 800-53A :: AC-9.1

import os

def run():
	f = os.popen('grep pam_lastlog /etc/pam.d/sshd').read()	
	if f = '':flag = 1
	else: 
		if f.find('silent') < 0: flag=0
		else: flag=1

	f = os.popen('grep -i PrintLastLog /etc/ssh/sshd_config').read()	
	if f
	return flag

run()
