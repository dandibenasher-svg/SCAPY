from scapy.all import *
conf.verb = 0
SERVER_IP = "192.168.72.173"
PORT = 12345


while True:
    data = input("enter a 5 letter word or exit! to quit")
    if data != "exit!" and len(data) != 5:
        print("illegal input word must only have 5 letters")
        continue

    packet = IP(dst=SERVER_IP)/UDP(dport=PORT)/Raw(load=data)
    send(packet, verbose=0)
    if data == "exit!":
        break

print("closed connection")
