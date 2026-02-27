# Task-2: Network Security & Scanning

## Objective
The objective of this task is to learn reconnaissance, network scanning, traffic analysis, vulnerability identification, and basic firewall configuration in a controlled lab environment.

## Lab Setup
- Attacker Machine: Kali Linux
- Target Machine: Metasploitable2
- Network Type: Host-Only Network

## Tools Used
- Nmap
- Wireshark
- Netcat (nc)
- OpenVAS / Nessus
- hping3
- iptables

## Part 1: Reconnaissance
Passive reconnaissance was performed using:
- `whois`
- `nslookup`
These commands help gather public information about IP addresses and domains without directly interacting with the target system.

## Part 2: Active Reconnaissance
Active testing was done using:
- `ping` to check if the target is alive
- `nc` (Netcat) for banner grabbing

This helped confirm that the target system was reachable and running FTP services.

## Part 3: Nmap Scanning
Different types of scans were performed:
- TCP Scan (`-sS`) to find open TCP ports
- UDP Scan (`-sU`) to find open UDP ports
- Service Version Detection (`-sV`) to identify service versions
- OS Detection (`-O`) to guess the operating system

The scan results showed multiple open ports and outdated services running on the target machine.

## Part 4: Vulnerability Scanning
A vulnerability scan was performed on the Metasploitable system.  
The scan identified several Critical and High severity vulnerabilities because Metasploitable is intentionally designed to be insecure for practice purposes.

## Part 5: Traffic Analysis
Wireshark was used to capture network traffic.

- ICMP traffic was captured during ping testing.
- FTP traffic was captured to observe how credentials can be seen in unencrypted communication.

This demonstrated how attackers can analyze network packets.

## Part 6: SYN Flood Demonstration
Using `hping3`, a SYN flood simulation was performed to demonstrate how denial-of-service attacks work.

## Part 7: Firewall Configuration

Basic firewall rules were created using `iptables` to allow and block specific ports.  
This demonstrated how firewall rules can control network access.

## Conclusion

In this task, reconnaissance and scanning techniques were used to identify open ports, services, vulnerabilities, and network traffic in a controlled lab environment.  
This task helped in understanding how attackers gather information and how defensive measures like firewalls can reduce risks.
