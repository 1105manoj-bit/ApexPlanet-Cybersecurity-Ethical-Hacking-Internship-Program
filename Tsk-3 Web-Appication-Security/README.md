Task-3: Web Application Security

Objective

The objective of this task is to understand common web application vulnerabilities from the OWASP Top 10 and demonstrate them in a controlled lab environment using DVWA.

The vulnerabilities demonstrated include:
- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- File Inclusion
- HTTP Request Interception using Burp Suite
- Web Security Headers Analysis

Lab Environment
The lab environment used for this task:
- Kali Linux (Attacker Machine)
- DVWA (Damn Vulnerable Web Application)
- Apache Web Server
- MySQL Database
- Burp Suite for request interception
DVWA was configured with security level set to LOW in order to demonstrate the vulnerabilities.

Tools Used
- Kali Linux
- DVWA
- Burp Suite
- Web Browser
- SecurityHeaders Scanner

Vulnerabilities Demonstrated
1. SQL Injection
Extracted user information from the database by manipulating SQL queries.

2. Cross Site Scripting (XSS)
Demonstrated both stored and reflected XSS using JavaScript payloads.

3. Cross Site Request Forgery (CSRF)
Showed how a malicious webpage can trick a user into performing actions like changing a password.

4. File Inclusion
Used Local File Inclusion to access sensitive system files.

5. Burp Suite Interception
Captured and modified HTTP requests during login.

6. Security Headers Analysis
Scanned a website for missing security headers and explained their importance.

Conclusion
This task helped in understanding how common web vulnerabilities work and how attackers can exploit them. It also highlighted the importance of secure coding practices and proper security configurations in web applications.
