
from scapy.all import *
conf.iface = "Npcap Loopback Adapter "

def HTTPFilter(p):
    return Raw in p and p[Raw].load.startswith(b'GET')

def HTTPrint(p):
    url = p[Raw].load.split(b' ')[1][1::].decode()
    print(url)

sniff(iface="Npcap Loopback Adapter",count=10,lfilter=HTTPFilter,prn=HTTPrint)
