#!/bin/bash
# ============================================================
#  ApexPlanet Capstone — Lab Verification Script
#  Run this on Kali Linux before starting exploitation phase
#  Usage: chmod +x lab-check.sh && ./lab-check.sh
# ============================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'
BOLD='\033[1m'

DVWA_IP="192.168.56.102"
BWAPP_IP="192.168.56.102"
PASS=0
FAIL=0
WARN=0

banner() {
  echo ""
  echo -e "${BLUE}${BOLD}============================================================${NC}"
  echo -e "${BLUE}${BOLD}   ApexPlanet Capstone — Lab Readiness Check${NC}"
  echo -e "${BLUE}${BOLD}   Kali Linux Attacker: 192.168.56.102${NC}"
  echo -e "${BLUE}${BOLD}============================================================${NC}"
  echo ""
}

check_tool() {
  local name="$1"
  local cmd="$2"
  local expected="$3"

  result=$(eval "$cmd" 2>&1 | head -1)
  if echo "$result" | grep -qi "$expected"; then
    echo -e "  ${GREEN}[PASS]${NC} $name — $result"
    PASS=$((PASS + 1))
  else
    echo -e "  ${RED}[FAIL]${NC} $name — got: $result"
    FAIL=$((FAIL + 1))
  fi
}

check_network() {
  local name="$1"
  local host="$2"
  local port="$3"

  if ping -c 1 -W 2 "$host" > /dev/null 2>&1; then
    echo -e "  ${GREEN}[PASS]${NC} Ping $name ($host) — reachable"
    PASS=$((PASS + 1))
  else
    echo -e "  ${RED}[FAIL]${NC} Ping $name ($host) — unreachable. Check VM is running & IP is set."
    FAIL=$((FAIL + 1))
    return
  fi

  if [ -n "$port" ]; then
    if curl -s --connect-timeout 3 "http://$host:$port" > /dev/null 2>&1; then
      echo -e "  ${GREEN}[PASS]${NC} HTTP $name ($host:$port) — responding"
      PASS=$((PASS + 1))
    else
      echo -e "  ${YELLOW}[WARN]${NC} HTTP $name ($host:$port) — port $port not responding. Is the web server running?"
      WARN=$((WARN + 1))
    fi
  fi
}

check_dvwa() {
  echo -e "\n${CYAN}${BOLD}  Checking DVWA application...${NC}"
  response=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 "http://$DVWA_IP/dvwa/login.php")
  if [ "$response" = "200" ]; then
    echo -e "  ${GREEN}[PASS]${NC} DVWA login page accessible at http://$DVWA_IP/dvwa/login.php"
    PASS=$((PASS + 1))
  else
    echo -e "  ${RED}[FAIL]${NC} DVWA login page returned HTTP $response"
    FAIL=$((FAIL + 1))
  fi
}

check_bwapp() {
  echo -e "\n${CYAN}${BOLD}  Checking bWAPP application...${NC}"
  response=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 "http://$BWAPP_IP/bWAPP/login.php")
  if [ "$response" = "200" ]; then
    echo -e "  ${GREEN}[PASS]${NC} bWAPP login page accessible at http://$BWAPP_IP/bWAPP/login.php"
    PASS=$((PASS + 1))
  else
    echo -e "  ${YELLOW}[WARN]${NC} bWAPP returned HTTP $response — bee-box may need http://$BWAPP_IP/bWAPP/install.php first"
    WARN=$((WARN + 1))
  fi
}

summary() {
  echo ""
  echo -e "${BLUE}${BOLD}============================================================${NC}"
  echo -e "${BOLD}  Results: ${GREEN}$PASS passed${NC}  ${RED}$FAIL failed${NC}  ${YELLOW}$WARN warnings${NC}"
  echo -e "${BLUE}${BOLD}============================================================${NC}"

  if [ "$FAIL" -eq 0 ] && [ "$WARN" -eq 0 ]; then
    echo -e "\n  ${GREEN}${BOLD}Lab is READY. You can start the exploitation phase!${NC}"
  elif [ "$FAIL" -eq 0 ]; then
    echo -e "\n  ${YELLOW}${BOLD}Lab mostly ready. Fix warnings before proceeding.${NC}"
  else
    echo -e "\n  ${RED}${BOLD}Fix FAILED items before starting exploitation.${NC}"
  fi
  echo ""
}

# ── RUN ALL CHECKS ────────────────────────────────────────────

banner

echo -e "${CYAN}${BOLD}[1] Tool availability checks${NC}"
check_tool "Nmap"        "nmap --version"           "Nmap"
check_tool "Metasploit"  "msfconsole -v 2>/dev/null" "Framework"
check_tool "SQLMap"      "sqlmap --version"          "sqlmap"
check_tool "Nikto"       "nikto -Version 2>&1"       "Nikto"
check_tool "Wireshark"   "wireshark --version"       "Wireshark"
check_tool "Gobuster"    "gobuster version"          "gobuster"
check_tool "Python3"     "python3 --version"         "Python 3"
check_tool "Curl"        "curl --version"            "curl"
check_tool "Dirb"        "dirb 2>&1"                 "dirb"

echo -e "\n${CYAN}${BOLD}[2] Network connectivity checks${NC}"
check_network "DVWA target"  "$DVWA_IP"  "80"
check_network "bWAPP target" "$BWAPP_IP" "80"

check_dvwa
check_bwapp

echo -e "\n${CYAN}${BOLD}[3] Burp Suite check${NC}"
if which burpsuite > /dev/null 2>&1; then
  echo -e "  ${GREEN}[PASS]${NC} Burp Suite found at $(which burpsuite)"
  echo -e "  ${YELLOW}[INFO]${NC} Launch manually: burpsuite & (configure browser proxy to 127.0.0.1:8080)"
  PASS=$((PASS + 1))
else
  echo -e "  ${YELLOW}[WARN]${NC} burpsuite not in PATH. Try: /usr/bin/burpsuite or search in Kali apps menu."
  WARN=$((WARN + 1))
fi

echo -e "\n${CYAN}${BOLD}[4] Current IP configuration${NC}"
echo -e "  Kali IP addresses:"
ip -4 addr show | grep "inet " | awk '{print "    " $2}' | grep -v "127.0"

summary

echo -e "  ${BLUE}Save this output as:${NC} screenshots/00_lab_verification.txt"
echo -e "  ${BLUE}Command:${NC} ./lab-check.sh | tee screenshots/00_lab_verification.txt"
echo ""
