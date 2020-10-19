import getpass
import telnetlib

HOST = "Localhost"
user = input("Enter your telnet Username: ")
password = getpass.getpass()
#Telnet to multiswitches when using a file called myswitches
f = open ('myswitches')

for IP in f:
    IP=IP.strip()
    print ("Get running config from switch " + (IP))#Output of what is being shown when connecting
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
    	tn.write(password.encode('ascii') + b"\n")
	tn.write(b"enable\n")
	tn.write(b"cisco\n")
#	tn.write(b"conf t\n")
#This would be the end of the altercode

#Backup Network Device config. Config t is not needed because we do not pull that info from global config

    #tn.write(b"terminal length 0\n")
   # tn.write(b"show run\n")
    #tn.write(b"exit\n")
    #readoutput = tn.read_all()
    #saveoutput = open("switch" + HOST, "w")
    #saveoutput.write(readoutput.decode('ascii'))
    #saveoutput.write("\n")
    #saveoutput.close


#this is the format if only connecting to one switch/router at a time

#tn = telnetlib.Telnet(HOST)

#tn.read_until(b"Username: ")
#tn.write(user.encode('ascii') + b"\n")
#if password:
#    tn.read_until(b"Password: ")
#    tn.write(password.encode('ascii') + b"\n")

#tn.write(b"enable\n")
#tn.write(b"cisco\n")



#VLAN LOOP
#    for n in range (2,21):
#        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
#        tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")


#VLANS (must indent to keep inside for IP in f:)
#tn.write(b"vlan 2\n")
#tn.write(b"name Python_VLAN_2\n")
#tn.write(b"vlan 3\n")
#tn.write(b"name Python_VLAN_3\n")
#tn.write(b"vlan 4\n")
#tn.write(b"name Python_VLAN_4\n")
#tn.write(b"vlan 5\n")
#tn.write(b"name Python_VLAN_5\n")
#tn.write(b"vlan 6\n")
#tn.write(b"name Python_VLAN_6\n")
#tn.write(b"vlan 7\n")
#tn.write(b"name Python_VLAN_7\n")
#tn.write(b"vlan 8\n")
#tn.write(b"name Python_VLAN_8\n")



#Loopbacks
#tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
#tn.write(b"exit\n")
#tn.write(b"int loop 1\n")
#tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
#tn.write(b"exit\n")

#OSPF
#tn.write(b"router OSPF 1\n")
#tn.write(b"network 1.1.1.1 255.255.255.255 area 0\n")
#tn.write(b"network 2.2.2.2 255.255.255.255 area 0\n")
#tn.write(b"exit\n")
#Closing remarks not needed when saving config
	tn.write(b"end\n")
	tn.write(b"wr\n")
	tn.write(b"exit\n")
	print(tn.read_all().decode('ascii'))
