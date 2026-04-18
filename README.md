# Python Security Tools

Security scripts written from scratch while learning cybersecurity.
Each tool is built to understand how real security tools work at the code level.

## Tools in this repo

### first_script.py
First Python script ever written. Variables, loops, and user input.
Day 5 of training.

### port_scanner.py (coming Day 6)
Scans ports 1-1024 on any IP using Python socket library.

## Why am I building these
Writing tools from scratch teaches the underlying concepts that
Using pre-built tools does not. Understanding how a port scanner
Working at the code level makes me a better security professional
than just knowing how to run Nmap.

*Updated daily.*
Update README with port scanner documentation 


# Python Security Tools

Security tools built from scratch while learning cybersecurity.
Each tool is written to understand how real security tools work at the code level.

---

## Tools

### port_scanner.py (v2)
TCP port scanner. Scans ports 1-1024 on any IP or domain. Shows service name alongside port number.

**Run:** python3 port_scanner.py

**How it works:** socket.connect_ex() attempts a TCP connection on each port. Returns 0 if open. Dictionary maps port numbers to service names.

**What I learned:** Port scanning is simply "attempt connection, record result." All of Nmap's features build on this same operation.

---

### password_generator.py
Generates cryptographically strong passwords.

**Run:** python3 password_generator.py

**How it works:** random.choice() selects each character independently from the full set of uppercase, lowercase, digits, and symbols.

**What I learned:** Password complexity comes from independent random selection. True randomness makes brute force impractical.

---

### log_analyzer.py
Analyzes Linux auth.log to identify and rank failed SSH login attempts by source IP.

**Run:** sudo python3 log_analyzer.py

**How it works:** Reads log file line by line, finds "Failed password" entries, extracts source IP, uses Counter to rank by frequency.

**What I learned:** This is what SIEM tools do at enterprise scale. Understanding it at the code level makes tools like Splunk more intuitive.

**Tested on:** Real Kali Linux auth.log — found actual external IP addresses attempting SSH brute force.

---

## About

Learning cybersecurity from scratch. Documenting everything publicly.

Learning journal: github.com/narasimhamallegari/cybersecurity-notes
LinkedIn: https://www.linkedin.com/in/narasimha-mallegari-/

Updated weekly.
