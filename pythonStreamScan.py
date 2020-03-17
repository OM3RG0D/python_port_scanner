#port scanner for TAMUK-Quickstart Python Project B (Omer Libich)

#allow for input of scan target
import socket
server = input('Enter a Host to Scan:')
remoteServerIP = socket.gethostbyname(server)
print (remoteServerIP)
#start with timestamp for start
from datetime import datetime
startTimestamp = datetime.now()

#create file object to write scan output(redirect each print to point to file object)
f = open("scanresults.txt", 'w')
#banner
print("-"*60, file=f)
print("Please wait, scanning remote host", server, file=f)
print("-"*60, file=f)
print(startTimestamp, file=f)

#get accurate start time for scan time calculation
import time
start = time.time()

#core scanner code (creates a stream socket)
import socket
import sys
try:
    for port in range(1, 1026):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:  OPEN".format(port), file=f)
        sock.close()

except KeyboardInterrupt:
    print("Scan was aborted by user.", file=f)
    sys.exit()

except socket.gaierror:
    print("Host name could not be resolved. Exiting Scan.", file=f)
    sys.exit()

except socket.error:
    print("Could not connect to server", file=f)
    sys.exit()

#end with timestamp for calculation
from datetime import datetime
endTimestamp = datetime.now()
print(endTimestamp, file=f)

#show process length
print("Scan completed in", time.time()-start, "seconds.", file=f)
