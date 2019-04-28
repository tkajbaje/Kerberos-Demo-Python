# Kerberos-Demo-Python
This is a small guide on the workings of kerberos protocol.We will set up a kerberos environment in ubuntu 18.04 running as guest on virutalbox and access a service from a client using kerberos.

# What you will need.
Ubuntu 18.04 or Later

VMWare

Python

# VMs:
Create Two Virtual Machines for kerberos server and ssh service(Use Ubuntu 18.04).

Assign a static ip to both machines and enable two network adapters in each machine(1.NAT 2.Bridged Adapter)

add below lines to `/etc/hosts` file of three machines

`<ip of server machine>` kerberos.com

`<ip of client machine>` client.com 

`<ip of ssh machine>` ssh.com

Make sure you can ping kerberos.com,client.com and ssh.com from all three VM's

# Keberos Server(kerberos.com)

Execute the following command on keberos.com Machine

>sudo apt-get install krb5-admin-server krb5-kdc

-Default Kerberos version 5 realm? [KERBEROS.COM]

-Kerberos servers for your realm? [kerberos.com]

-Administrative server for your realm? [kerberos.com]

## Configure kerberos.com

>sudo krb5_newrealm

It will ask you to enter a password for database creation and after that, it will start Kerberos KDC krb5kdc and Kerberos administrative servers kadmind processes.

Add users(Principles):

>sudo kadmin.local

Add User by typing >addprinc root

Enter a new password if prompted

Assign admin role to the user

>addprinc root/admin

uncomment the line */admin * in /etc/krb5kdc/kadm.acl file.

>kinit root

if it prompts for password server is setup successfully.

# Client(Host Machine)

>apt-get install krb5-user

-Default Kerberos version 5 realm? [KERBEROS.COM]

-Kerberos servers for your realm? [kerberos.com]

-Administrative server for your realm? [kerberos.com]

>kinit root 

Enter the password to get a ticket from server.

# Service(ssh.com)

Install OpenSSH on ssh.com

>apt-get install openssh-server krb5-config

Edit /etc/ssh/sshd_config and enable the following lines

>GSSAPIAuthentication yes

>GSSAPICleanupCredentials yes

Then restart the ssh server [/etc/init.d/ssh restart] 

# Kerberos Server(kerberos.com)

>sudo kadmin.local

>addprinc -randkey host/ssh.com

>ktadd -k /tmp/ssh.com.keytab host/ssh.com

>scp /tmp/ssh.com.keytab root@ssh.com:/etc/krb5.keytab

# Client(Host Machine)

Edit /etc/ssh/ssh_config and enable the following lines

>GSSAPIAuthentication yes

>GSSAPIDelegateCredentials yes


# Python Wrapper
>python kerberos.py

Please Select One of the Below Options(0 for exit):

1.Get a Ticket

2.Use Service

3.Destroy Tickets


After Getting a Ticket you will be able to access the ssh service without prompting for a password.

After Destroying Tickets you will be prompted for password.




