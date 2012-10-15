#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000410 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources.
#
#Note:  SFTP and FTPS are encrypted alternatives to FTP to be used in place of FTP.  SFTP is implemented by the SSH service and uses its banner configuration.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#FTP to the system. 
## ftp localhost
#Check for either of the following login banners based on the character limitations imposed by the system. An exact match is required. If one of these banners is not displayed, this is a finding. If the system does not run the FTP service, this is not applicable.
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
#Fix Text: 
#Provide the proper text for the DoD banner to be presented by the FTP server to the user.
#
#For vsftp:
#Examine the /etc/vsftp.conf file for the "banner_file" entry. (i.e. banner_file = /etc/banner/vsftp)
#
#For gssftp:
#Examine the /etc/xinetd.d/gssftp file for the "banner" entry. (i.e. banner = /etc/banner/gssftp)
#
#For both:
#Add the banner entry if one is not found.
#
#Modify or create the referenced banner file to contain one of the following DoD login banners (based on the character limitations imposed by the system).
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
