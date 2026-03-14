Cross Site Request Forgery (CSRF)

What is CSRF?

Cross Site Request Forgery is a vulnerability where an attacker tricks a logged-in user into performing unwanted actions on a web application.
The user is authenticated, so the server accepts the malicious request.

Demonstration in DVWA

The CSRF module in DVWA allows changing the password.
Normally the user fills a form and submits it.
However, an attacker can create a malicious webpage containing a hidden form.

Example attack page:
<form action="http://localhost/dvwa/vulnerabilities/csrf/" method="POST">
<input type="hidden" name="password_new" value="123456">
<input type="hidden" name="password_conf" value="123456">
<input type="submit" value="Click">
</form>If a logged-in user clicks this button, the password will change automatically.

Impact

CSRF attacks can cause:
- Unauthorized password changes
- Money transfers
- Account modifications

Prevention

CSRF can be prevented using:
- CSRF tokens
- SameSite cookies
- Re-authentication for sensitive actions
- Checking HTTP referrer headers

Example CSRF token:
<input type="hidden" name="csrf_token" value="random_secure_token">
