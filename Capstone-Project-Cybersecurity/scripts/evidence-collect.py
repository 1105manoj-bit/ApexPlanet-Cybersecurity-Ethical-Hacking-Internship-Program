#!/usr/bin/env python3
"""
ApexPlanet Capstone — Evidence Collection Helper
Automates saving tool outputs with timestamps for your GitHub repo.

Usage:
  python3 evidence-collect.py --phase recon --tool nmap --cmd "nmap -sV -p- 192.168.56.20"
  python3 evidence-collect.py --phase exploitation --tool sqlmap --cmd "sqlmap -u 'http://192.168.56.20/dvwa/vulnerabilities/sqli/?id=1' --dbs"
  python3 evidence-collect.py --list   # Show all saved evidence
"""

import subprocess
import argparse
import datetime
import os
import sys
import json

EVIDENCE_DIR = os.path.expanduser("~/capstone-pentest")
PHASES = ["recon", "exploitation", "post-exploitation", "incident-response"]

COLORS = {
    "green":  "\033[92m",
    "red":    "\033[91m",
    "yellow": "\033[93m",
    "blue":   "\033[94m",
    "cyan":   "\033[96m",
    "reset":  "\033[0m",
    "bold":   "\033[1m",
}

def c(color, text):
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"

def setup_dirs():
    """Create the full repo structure if it doesn't exist."""
    dirs = [
        EVIDENCE_DIR,
        f"{EVIDENCE_DIR}/recon",
        f"{EVIDENCE_DIR}/exploitation/sqli",
        f"{EVIDENCE_DIR}/exploitation/xss",
        f"{EVIDENCE_DIR}/exploitation/csrf",
        f"{EVIDENCE_DIR}/exploitation/lfi",
        f"{EVIDENCE_DIR}/exploitation/command-injection",
        f"{EVIDENCE_DIR}/post-exploitation",
        f"{EVIDENCE_DIR}/screenshots",
        f"{EVIDENCE_DIR}/incident-response",
        f"{EVIDENCE_DIR}/scripts",
        f"{EVIDENCE_DIR}/final-report",
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print(c("green", f"[+] Evidence directory: {EVIDENCE_DIR}"))

def run_and_save(phase, tool, cmd, note=""):
    """Run a command and save its output with metadata."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_tool = tool.replace(" ", "_").lower()

    phase_dir = f"{EVIDENCE_DIR}/{phase}"
    os.makedirs(phase_dir, exist_ok=True)

    outfile = f"{phase_dir}/{timestamp}_{safe_tool}.txt"

    header = f"""{'='*70}
ApexPlanet Capstone — Evidence Log
Phase   : {phase}
Tool    : {tool}
Command : {cmd}
Date    : {datetime.datetime.now().isoformat()}
Note    : {note or 'None'}
{'='*70}

"""

    print(c("cyan", f"\n[*] Running: {cmd}"))
    print(c("yellow", f"[*] Saving to: {outfile}"))
    print(c("blue", "-" * 50))

    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=300
        )
        output = result.stdout + ("\n[STDERR]\n" + result.stderr if result.stderr else "")
    except subprocess.TimeoutExpired:
        output = "[TIMEOUT] Command exceeded 300 seconds."
    except Exception as e:
        output = f"[ERROR] {str(e)}"

    full_content = header + output

    with open(outfile, "w") as f:
        f.write(full_content)

    # Also update the evidence manifest
    manifest_path = f"{EVIDENCE_DIR}/evidence_manifest.json"
    manifest = []
    if os.path.exists(manifest_path):
        with open(manifest_path) as f:
            try:
                manifest = json.load(f)
            except Exception:
                manifest = []

    manifest.append({
        "timestamp": timestamp,
        "phase": phase,
        "tool": tool,
        "command": cmd,
        "file": outfile,
        "note": note
    })
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(output[:2000] + ("...[truncated]" if len(output) > 2000 else ""))
    print(c("green", f"\n[+] Evidence saved: {outfile}"))
    print(c("green", f"[+] Manifest updated: {manifest_path}"))

def list_evidence():
    """List all collected evidence."""
    manifest_path = f"{EVIDENCE_DIR}/evidence_manifest.json"
    if not os.path.exists(manifest_path):
        print(c("yellow", "No evidence collected yet."))
        return

    with open(manifest_path) as f:
        manifest = json.load(f)

    print(c("bold", f"\n{'='*70}"))
    print(c("bold", f"  Evidence manifest — {len(manifest)} entries"))
    print(c("bold", f"{'='*70}\n"))

    current_phase = None
    for entry in manifest:
        if entry["phase"] != current_phase:
            current_phase = entry["phase"]
            print(c("cyan", f"\n  [{current_phase.upper()}]"))

        print(f"  {entry['timestamp']}  {c('green', entry['tool']):<30} {entry['command'][:60]}")

    print()

def generate_readme():
    """Generate a README.md for the GitHub repo."""
    content = """# Capstone Pentest — ApexPlanet Internship

## Project Overview
Web Application Penetration Test on DVWA (Metasploitable 2) and bWAPP (bee-box).

**Tester:** [Your Name]  
**Duration:** Days 49–60  
**Methodology:** OWASP Testing Guide v4 + PTES  

## Lab Environment
| VM | IP | Role |
|---|---|---|
| Kali Linux | 192.168.56.10 | Attacker |
| Metasploitable 2 (DVWA) | 192.168.56.20 | Target 1 |
| bee-box (bWAPP) | 192.168.56.30 | Target 2 |

## Repository Structure
```
├── recon/            ← Nmap, Nikto, Dirb outputs
├── exploitation/     ← SQLi, XSS, CSRF, LFI, CMDi evidence
├── screenshots/      ← Visual evidence
├── scripts/          ← lab-check.sh, evidence-collect.py
├── incident-response/← Post-incident report
└── final-report/     ← Professional PDF report
```

## Vulnerabilities Tested
- [ ] SQL Injection (manual + SQLMap)
- [ ] XSS — Reflected
- [ ] XSS — Stored
- [ ] CSRF
- [ ] Local File Inclusion (LFI)
- [ ] Command Injection
- [ ] Brute Force (Burp Intruder)
- [ ] File Upload bypass

## Tools Used
Burp Suite · Metasploit · SQLMap · Nmap · Nikto · Wireshark · Gobuster · Python3

## Quick Start (Lab Setup)
```bash
# Run on Kali Linux
chmod +x scripts/lab-check.sh
./scripts/lab-check.sh

# Collect evidence
python3 scripts/evidence-collect.py --phase recon --tool nmap --cmd "nmap -sV 192.168.56.20"
```

## Disclaimer
All testing was performed in an isolated lab environment for educational purposes only.
"""
    readme_path = f"{EVIDENCE_DIR}/README.md"
    with open(readme_path, "w") as f:
        f.write(content)
    print(c("green", f"[+] README.md generated: {readme_path}"))

def main():
    parser = argparse.ArgumentParser(
        description="ApexPlanet Capstone — Evidence Collection Helper"
    )
    parser.add_argument("--phase", choices=PHASES, help="Pentest phase")
    parser.add_argument("--tool", help="Tool name (e.g. nmap, sqlmap)")
    parser.add_argument("--cmd",  help="Command to run and capture")
    parser.add_argument("--note", default="", help="Optional note about this run")
    parser.add_argument("--list", action="store_true", help="List all collected evidence")
    parser.add_argument("--init", action="store_true", help="Initialize repo structure + README")

    args = parser.parse_args()

    setup_dirs()

    if args.init:
        generate_readme()
        print(c("green", "\n[+] Repo initialized! Push to GitHub:"))
        print(c("yellow", "    cd ~/capstone-pentest && git init && git add . && git commit -m 'Initial lab setup'"))
        return

    if args.list:
        list_evidence()
        return

    if not all([args.phase, args.tool, args.cmd]):
        parser.print_help()
        print(c("yellow", "\nExample:"))
        print(c("cyan",   "  python3 evidence-collect.py --phase recon --tool nmap --cmd 'nmap -sV 192.168.56.20'"))
        sys.exit(1)

    run_and_save(args.phase, args.tool, args.cmd, args.note)

if __name__ == "__main__":
    main()
