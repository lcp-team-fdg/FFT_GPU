'''
================================================
 Future Defense Group (FDG)
 File used to graph the IED Detection Pattern.
================================================

'''

# Libraries
#!/usr/bin/python
import socket
import sys

from fdg.client.fdg_client import Client

cli = Client(url='http://127.0.0.1:8000', username='admin', password='password')

address = ("0.0.0.0", 5021)
#address = ("192.168.137.92S", 5021)

sock = socket.socket(socket.AF_INET,    # Internet
                     socket.SOCK_DGRAM) # UDP
                     
# Accept UDP datagrams, on the given port, from any sender                     
sock.bind(address)

print ("waiting on port:", address)

while True:
    data, address = sock.recvfrom(1024)#buffer size is 1024 bytes
    print ("Received:", data)
    
    temp2 = str(data)
    temp = temp2.split(', ')
    
    FFTSNR = temp[0]
    FFTSNR = float(FFTSNR[2:])
    FFTNoise = float(temp[1])
    FFTMax = float(temp[2])
    TimeStamp = temp[3]
    TimeStamp = TimeStamp[:TimeStamp.find(" \n")]
    
    print("writting")
    
    cli.post_snr_data(snr=FFTSNR, noise=FFTNoise, max=FFTMax, timestamp=TimeStamp)
