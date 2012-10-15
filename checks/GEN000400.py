#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000400 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#If a user is assigned the GID of a group not existing on the system, and a group with the GID is subsequently created, the user may have unintended rights to the group.
#
#
#Discussion: 
#Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Access the system console and make a login attempt. Check for either of the following login banners based on the character limitations imposed by the system. An exact match is required. If one of these banners is not displayed, this is a finding.
#
#You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.
#
#By using this IS (which includes any device attached to this IS), you consent to the following conditions:
#
#-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.
#
#-At any time, the USG may inspect and seize data stored on this IS.
#
#-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.
#
#-This IS includes security measures (e.g., authentication and access controls) to protect USG interests- -not for your personal benefit or privacy.
#
#-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. 
#
#OR
#
#I've read & consent to terms in IS user agreem't.
#
#Fix Text: 
#Edit /etc/issue and add one of the DoD login banners (based on the character limitations imposed by the system).
#
#DoD Login Banners:
#
#You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.
#By using this IS (which includes any device attached to this IS), you consent to the following conditions:
#-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.
#-At any time, the USG may inspect and seize data stored on this IS.
#-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.
#-This IS includes security measures (e.g., authentication and access controls) to protect USG interests- -not for your personal benefit or privacy.
#-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. 
#
#OR
#
#I've read & consent to terms in IS user agreem't.   
#
#IA Controls:ECWM-1
#CCI: CCI-000048
#NIST SP 800-53 :: AC-8 a
#NIST SP 800-53A :: AC-8.1 (ii)

import os

def run():
	return -1

run()
