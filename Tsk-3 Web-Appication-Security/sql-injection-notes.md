SQL Injection Analysis

What is SQL Injection?
SQL Injection is a vulnerability where an attacker can manipulate a database query by inserting malicious SQL code into input fields.
If user input is not properly validated, the attacker can access or modify database data.

Demonstration in DVWA
In DVWA, the SQL Injection module was used.

Input used:
1' OR '1'='1
This payload modifies the SQL query.

Original query:
SELECT * FROM users WHERE id='1'
Injected query becomes:
SELECT * FROM users WHERE id='1' OR '1'='1'
Since the condition is always true, the database returns all user records.

Result
The application displayed all usernames and password hashes stored in the database.
This confirms that SQL Injection was successful.

Prevention

SQL Injection can be prevented using:
- Prepared statements
- Parameterized queries
- Input validation
- ORM frameworks

Example secure code:
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$id]);

Prepared statements ensure user input is treated as data and not executable SQL code.
