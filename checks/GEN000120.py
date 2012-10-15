#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000120 of DISA STIG RedHat_5-V1R1
#20 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Timely patching is critical for maintaining the operational availability, confidentiality, and integrity of information technology #(IT) systems.  However, failure to keep operating system and application software patched is a common mistake made by IT #professionals. New patches are released daily, and it is often difficult for even experienced system administrators to keep abreast #of all the new patches.  When new weaknesses in an operating system exist, patches are usually made available by the vendor to #resolve the problems.  If the most recent recommended updates and security patches are not installed, unauthorized users may take #advantage of weaknesses present in the unpatched software.  The lack of prompt attention to patching could result in a system #compromise.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Obtain the list of available package updates from Red Hat. Check the available package updates have been installed on the system.
#
#Use the "rpm" command to list the packages installed on the system.
#Example:
## rpm -qa -last
#
#If updated packages are available and applicable to the system and have not been installed, this is a finding.
#
#One source for the list of Red Hat updates is available at https://access.redhat.com/security/updates/active/
#
#Fix Text: 
#Install the patches or updated packages available from the vendor.
#
#IA Controls:VIVM-1
#CCI: CCI-001227
#NIST SP 800-53 :: SI-2 a
#NIST SP 800-53A :: SI-2.1 (i)
#

import os

def run():return False

run()
