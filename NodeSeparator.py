__author__ = 'shelan'
import os
import paramiko

host_list =[]
error_list= []
active_list=[]


host_list = [line.strip() for line in open("nodes.txt")]
for host in host_list:
    #os.system("ping -c 1 "+host)

    key = paramiko.RSAKey.from_private_key_file("id-rsa")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #print "connecting"
    try:
        client.connect( hostname = host.rstrip(), username = "istple_seprs3", pkey = key )
        active_list.append(host)
        print "connected to ",host
    except Exception:
        print "error occured in ",host
        error_list.append(host)


error_file = open("error-list.txt",'w+')
active_file = open("active-list.txt",'w+')
for host in error_list:
    error_file.writelines(host+"\n")
for host in active_list:
    active_file.writelines(host+"\n")

print len(error_list), "no of nodes(s) are failing out of", len(host_list)