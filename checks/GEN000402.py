#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000402 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources.
#
#This requirement applies to graphical desktop environments provided by the system to locally attached displays and input devices as well as to graphical desktop environments provided to remote systems, including thin clients.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Access the graphical desktop environment(s) provided by the system and attempt to log in. Check for either of the following login banners based on the character limitations imposed by the system. An exact match is required. If one of these banners is not displayed, this is a finding.
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
#Fix Text: 
#Configure the system to display one of the DoD login banners prior to, or as part of, the graphical desktop environment login process.
#
#Procedure:
#Modify /usr/share/gdm/themes/RHEL/RHEL.xml by adding the following xml after the first two "pixmap" entries.
#
#<item type="rect" id="custom-dod-banner">
#<pos anchor="nw" x="20%" y="10" width="80%" height="100%"/>
#<box>
#<item type="label">
#<normal font="Sans Bold 9" color="#ffffff"/>
#<text>
#Insert the "approved text" here based on the character limitations imposed by the system.
#</text>
#</item>
#</box>
#</item>
#
#
#Approved text:
#
#DoD Login Banners:
#
#You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.
#By using this IS (which includes any device attached to this IS), you consent to the following conditions:
#-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.
#-At any time, the USG may inspect and seize data stored on this IS.
#-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.
#-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.
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
