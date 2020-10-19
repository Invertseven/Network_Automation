import getpass
import telnetlib

HOST = "Localhost"
user = input("Enter your telnet Username: ")
password = getpass.getpass()
f = open ('myswitches')

for IP in f:
    IP=IP.strip()
    print ("Saving Configs  " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    tn.write(b"end\n")
    print(tn.read_all().decode('ascii'))



