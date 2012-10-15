#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000440 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources.
#
#Note:  SFTP and FTPS are encrypted alternatives to FTP to be used in place of FTP.  SFTP is implemented by the SSH service and uses its banner configuration.
#
#Discussion: 
#Monitoring and recording successful and unsuccessful logins assists in tracking unauthorized access to the system.  Without this logging, the ability to track unauthorized activity to specific user accounts may be diminished.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Determine if all logon attempts are being logged.
#
#Procedure:
#Verify successful logins are being logged:
## last -R | more 
#If the command does not return successful logins, this is a finding.
#
#Verify if unsuccessful logons are being logged: 
## lastb -R | more
#If the command does not return unsuccessful logins, this is a finding.
#
#Fix Text: 
#Make sure the collection files exist.
#Procedure:
#If there are no successful logins being returned from the "last" command, create /var/log/wtmp:
## touch /var/log/wtmp
#
#If there are no unsuccessful logins being returned from the "lastb" command, create /var/log/btmp:
## touch /var/log/btmp
#
#IA Controls:ECAR-1, ECAR-2, ECAR-3
#CCI: CCI-000126
#NIST SP 800-53A :: AU-2.1 (v)
#NIST SP 800-53 :: AU-2 d

import os

def run():
	if os.popen('last -R').read() >= 1 and os.popen('lastb -R') >= 1:
		return 1
	else: return 0

run()
