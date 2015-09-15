import xmlrpclib
api_server = xmlrpclib.ServerProxy('https://www.planet-lab.eu/PLCAPI/')

node_list = [line.strip() for line in open("error-list.txt")]

auth = {}
auth['Username'] = "shelanrc@gmail.com"
auth['AuthString'] = "shelan@1987"
auth['AuthMethod'] = "password"

slice_name = "istple_seprs3";

authorized = api_server.AuthCheck(auth)
if authorized:
    print "logged in successfully"
else:
    print "[FAILURE] Permission denied."

status = api_server.DeleteSliceFromNodes(auth, slice_name, node_list)

if(status):
    print len(node_list)," slices removed successfully"
else:
    print "something went wrong while removing nodes to the slice"