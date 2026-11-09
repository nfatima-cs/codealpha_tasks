# Educational use only. Capture traffic only on devices or networks you are authorized to monitor.
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def show_packet(packet):
    if IP in packet:
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = str(packet[IP].proto)

        print("-" * 40)
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", protocol)
        if Raw in packet:
            print("Payload length:", len(packet[Raw].load), "bytes")
        else:
           print("Payload length: No Raw data")

print("Capturing up to 5 IPv4 packets. Please wait...")

sniff(
    filter="ip",
    count=5,
    timeout=30,
    prn=show_packet,
    store=False
)

print("Capture finished.")