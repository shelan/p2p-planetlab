import os
import paramiko
import select
import thread


def setup(host_name):
    key = paramiko.RSAKey.from_private_key_file("id-rsa")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # print "connecting"
    try:
        client.connect(hostname=host_name.rstrip(), username="istple_seprs3", pkey=key)
        print "connected to ", host_name

        javaSetup = ["rm -rf setupJava*", "wget https://s3.eu-central-1.amazonaws.com/shelan-p2p/setupJava-2.sh",
                     "sh setupJava-2.sh",
                     "source ~/.bashrc",". ~/.bashrc","echo $JAVA_HOME", "java -version"]
        appSetup = ["killall java",
            "rm -rf p2p-bay-1.0-SNAPSHOT-jar-with-dependencies.jar",
            "wget https://s3.eu-central-1.amazonaws.com/shelan-p2p/p2p-bay-1.0-SNAPSHOT-jar-with-dependencies.jar"]

        cleanup = ["rm -rf ~/.bashrc","mv .bashrc-bk .bashrc"]

        checkjava =["java -version"]

        checkJavaProcess = ["fuser -n tcp 4567","ps ax| grep java"]

        appStart=["killall java","sh run.sh","sleep 10"]

        appKill=["killall java"]

        runscriptDownload =["rm -rf run.sh","wget https://s3.eu-central-1.amazonaws.com/shelan-p2p/run.sh"]

        #change clean up to javaSetup
        for command in appKill:
            print "Executing {}".format(command)
            stdin, stdout, stderr = client.exec_command(command)
            print stdout.read()
            print stderr.read()
    except Exception:
        print "error occured in ", host


        while not stdout.channel.exit_status_ready():
            # Only print data if there is data to read in the channel
            if stdout.channel.recv_ready():
                rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
                if len(rl) > 0:
                    # Print data from stdout
                    print stdout.channel.recv(1024),

    client.close()

active_list = []

active_list = [line.strip() for line in open("tmp-list")]
print active_list

for host in active_list:
    print "starting thread for ", host
    setup(host)

    #print len(error_list), "no of nodes(s) are failing out of", len(host_list)