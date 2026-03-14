Cross Site Scripting (XSS)

What is XSS?

Cross-Site Scripting is a vulnerability where attackers inject malicious scripts into a webpage. These scripts run in the browser of other users.
This can allow attackers to steal cookies, session tokens, or perform actions on behalf of the victim.

Types Demonstrated

Stored XSS

In DVWA Stored XSS module, the following payload was used:
<script>alert('XSS')</script>The script was stored in the database and executed every time the page was loaded.
This means any user who visits the page will see the JavaScript alert.

Reflected XSS

In the Reflected XSS module, the same payload was entered into an input field.
The script was reflected immediately in the response page and executed in the browser.

Impact

XSS attacks can lead to:
- Cookie theft
- Session hijacking
- Malicious redirects
- Defacement of web pages

Prevention

Common mitigation techniques include:
- Input validation
- Output encoding
- Content Security Policy (CSP)
- Sanitizing user input

Example security header:
Content-Security-Policy: default-src 'self'
