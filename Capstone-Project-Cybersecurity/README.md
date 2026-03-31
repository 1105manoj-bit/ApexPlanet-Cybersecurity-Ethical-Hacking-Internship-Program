# ApexPlanet Internship — Capstone Pentest Project

## Overview
Web application penetration test against Metasploitable 2 running DVWA.
Conducted as part of ApexPlanet Security Internship Days 49-60.

## Lab Setup
| Machine | IP | Role |
|---|---|---|
| Kali Linux | 192.168.56.103 | Attacker |
| Metasploitable 2 | 192.168.56.102 | Target |

## Vulnerabilities Found
- SQL Injection — CVSS 9.8 Critical
- XSS Reflected — CVSS 7.2 High
- OS Command Injection — CVSS 10.0 Critical
- vsftpd 2.3.4 Backdoor — CVSS 10.0 Critical

## Tools Used
Nmap, Nikto, SQLMap, Burp Suite, Metasploit, Wireshark, Python3

## Results
- 23 open ports found
- 27 web vulnerabilities found
- 5 passwords cracked
- Root shell obtained

## Repository Structure
- recon/ — Nmap and Nikto scan outputs
- exploitation/ — Attack evidence and tool outputs
- screenshots/ — Visual proof of each attack
- incident-response/ — Post incident report
- scripts/ — lab-check.sh and evidence-collect.py
- final-report/ — Professional PDF report
