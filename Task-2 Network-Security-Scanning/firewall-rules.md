# Firewall Rules Configuration (iptables)

## Objective
The objective of this task was to understand how firewall rules can allow or block specific network traffic.

## Rules Created

### 1. Allow SSH (Port 22)

Command used:
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

Explanation:
This rule allows incoming SSH connections to the system.  
SSH is commonly used for secure remote access.

### 2. Block HTTP (Port 80)

Command used:
sudo iptables -A INPUT -p tcp --dport 80 -j DROP

Explanation:
This rule blocks incoming HTTP traffic.  
This demonstrates how a firewall can prevent access to web services.

### 3. View Active Rules

Command used:
sudo iptables -L

Explanation:
This command lists all active firewall rules currently applied to the system.

## Conclusion

By using iptables, specific ports can be allowed or blocked.  
Firewalls are an important security layer that helps protect systems from unauthorized access and network-based attacks.
