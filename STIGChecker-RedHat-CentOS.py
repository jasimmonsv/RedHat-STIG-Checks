#! /usr/bin/python
#Python Version 2.1
#
#This script is the wrapper for all the checks of DISA STIG RedHat_5-V1R1
#20 September 2012
#Author: J.A. Simmons V
#

def main():
	toolCheck()
	result = os.popen("grep ':S:' /etc/inittab)
	if result.read().find(':S:') =-1:return False
	else: return True
	
def toolCheck():
#this function will check that all required tools are install on the system
	print "Checking toolsets: "
	#check last
	#check pwck
	#check cut find "command not found"
	pass
	
def runChecks():
	#main bulk of the program that runs and reports on all the various checks
	import GEN000020
	GEN000020.run()
	
	pass
	
	
	
main()
