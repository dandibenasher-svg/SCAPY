from scapy.all import *
SERVER_IP = "192.168.72.173"
PORT = 12345

def filterWord(p):
    return IP in p and UDP in p and Raw in p and p[IP].dst == SERVER_IP and p[UDP].dport == PORT

msg = None
while msg != "exit!":
    p = sniff(iface="Npcap Loopback Adapter",count=1, lfilter=filterWord)
    msg = p[0][Raw].load.decode()
    print(msg)

print("Server closed")


