from fabric.api import *
import os

env.hosts = ['planetlab1.di.fct.unl.pt']
env.user = 'istple_seprs3'
env.key_filename = 'id-rsa'

error_nodes = []

def set_hosts():
    env.hosts = open('nodes.txt', 'r').readlines()
    print hosts

def copy_jar():

    print "connecting ", env.host_string

    try:
        run("rm -rf tmp/")
        run("mkdir tmp/")
       # os.system("scp -i id-rsa /Users/shelan/github/uni-projects/p2p-bay/target/p2p-bay-1.0-SNAPSHOT-jar-with-dependencies.jar istple_seprs3@"+env.host_string+":/home/istple_seprs3/tmp")
        run("ls tmp/")

    except Exception:
        print "error occured"


