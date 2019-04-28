#!/usr/bin/env python3

import subprocess
import argparse
import getpass


def krbauth(username, password):
    cmd= ['kinit', username]
    success = subprocess.run(cmd, input=password.encode(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    return not bool(success)


def log(message, quiet):
    if not quiet:
        print('[*] {}'.format(message))


def kinit():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='Kerberos username', type=str)
    parser.add_argument('-p', '--password', help='Kerberos password', type=str)
    parser.add_argument('-r', '--realm', help='Kerberos REALM', type=str)
    parser.add_argument('-q', '--quiet', help='Quiet mode', action='store_true')
    args = parser.parse_args()

    username = args.username or input('[*] Kerberos username: ')
    password = args.password or getpass.getpass('[*] Kerberos password: ')
    if args.realm:
        username = '{}@{}'.format(username, args.realm)

    log('Logging in as {}'.format(username), args.quiet)
    res = krbauth(username, password)
    if res:
        log('Succesfully Logged in!', args.quiet)
        return 0
    else:
        log('Incorrect Login!', args.quiet)
        return 1
def destroy():
    cmd= ['kdestroy']
    success = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    print("Successfully Destroyed Tickets")
def service():
	cmd= ['ssh root@ssh.com']
	success=subprocess.call(cmd,shell=True)
	 
	
def main():
	print("Please Select One of the Below Options(0 for exit):\n")
	print("1.Get a Ticket")
	print("2.Use Service")
	print("3.Destroy Tickets")
	choice=int(input())
	while(choice != 0):
		if choice==1:
			kinit()
		if choice==2:
			service()
		if choice==3:
			destroy()
		choice=int(input("Enter your Choice"))
		
		

if __name__=='__main__':
    main()
