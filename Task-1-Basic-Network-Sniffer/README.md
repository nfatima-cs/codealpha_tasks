# Task 1: Basic Network Sniffer

## Overview
A basic Python network sniffer created for the CodeAlpha Cyber Security Internship.

The program captures IPv4 packets and displays:
- Source IP address
- Destination IP address
- Protocol: TCP, UDP, ICMP, or the IP protocol number
- A preview of the first 50 bytes from the Raw layer, when available

## Requirements
- Python 3
- Scapy
- Npcap for Windows

## Installation
Install Npcap on Windows, then install Scapy:

```bash
python -m pip install scapy
```

## How to Run
Open a terminal in the project folder with the required capture permissions.
On Windows, run the terminal as administrator.

```bash
python sniffer.py
```

The program captures up to 5 IPv4 packets or stops after 30 seconds.

## Understanding the Output
- Source IP identifies the sender.
- Destination IP identifies the receiver.
- Protocol identifies the transport or network protocol.
- Payload preview displays available Raw-layer bytes.
- "No Raw data" means no Raw layer was found, not necessarily that the packet has no application data.
- Binary or encrypted data may not appear as readable text.

## Limitations
- This version captures IPv4 traffic only.
- It does not decrypt encrypted traffic.
- It displays a short payload preview rather than reconstructing complete conversations.
- Captured packets are not saved to a file.

## Ethical Use
Use only on devices or networks you are authorized to monitor.
Do not publish private packet contents, credentials, or personal information.

## Author
Noor Fatima