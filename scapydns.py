
from scapy.all import *

conf.iface ="Realtek Gaming GbE Family Controller"


def DNSFilter(p):
    return DNS in p and p[DNS].qr == 1 and p[DNS].ancount > 0 and p[DNS].an.type == 1

def DNSPrint(pack):
    ip = packet[DNS].an.rdata
    print(ip)

p = sniff(iface="Realtek Gaming GbE Family Controller", count=10, lfilter=DNSFilter, prn=DNSPrint)
