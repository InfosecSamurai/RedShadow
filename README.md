<p align="center">
  <strong>RedShadow - Ethical Hacking & Red Teaming Tool</strong>
</p>

<p align="center">
  <img src="https://i.imgur.com/FVqMoKZ.png" alt="RedShadow Banner" width="600">
</p>


**RedShadow** is an advanced ethical hacking and red teaming toolkit designed for elite penetration testers, cybersecurity professionals, and ethical hackers. It provides reconnaissance, exploitation, post-exploitation, and evasion capabilities in a modular and scalable fashion.

## **Table of Contents**  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Modules Overview](#modules-overview)  
- [Configuration](#configuration)  
- [Logging & Reporting](#logging--reporting)  
- [Updating](#updating)  
- [Contributing](#contributing)  
- [License](#license)  

---

## **Features**  
✅ Automated OSINT & reconnaissance  
✅ Exploitation & payload execution  
✅ Post-exploitation & privilege escalation  
✅ Evasion & anti-forensics techniques  
✅ Report generation & logging  
✅ Modular architecture for custom extensions  

---

## **Installation**  

### **Prerequisites**  
Ensure your system has the following installed:  
- Python 3.8+  
- Pip & virtualenv  
- Nmap, SQLmap, and Tor  

### **Install RedShadow**  

Run the following commands to set up RedShadow:  

```bash
git clone https://github.com/infosecsamurai/RedShadow.git  
cd RedShadow  
bash scripts/install.sh
```

Activate the virtual environment:
```bash
source env/bin/activate
```

---

## **Usage**

### **Basic Commands**

Run the tool interactively:

```bash
python3 redshadow.py
```

Run a specific module:

```bash
python3 redshadow.py -m recon
python3 redshadow.py -m exploit
python3 redshadow.py -m post
python3 redshadow.py -m evasion
python3 redshadow.py -m report
```

Exit interactive mode:

```bash
RedShadow > exit
```

---

## **Modules Overview**

### 1. Reconnaissance (recon)

Gather OSINT, find vulnerabilities, and enumerate targets.

```bash
python3 redshadow.py -m recon
```

**Features:**
- WHOIS lookup
- DNS & IP enumeration
- Subdomain scanning

---

### 2. Exploitation (exploit)

Scan and exploit known vulnerabilities.

```bash
python3 redshadow.py -m exploit
```

**Features:**
- Automated Nmap scanning
- SQL injection automation

---

### 3. Post-Exploitation (post)

Maintain access and escalate privileges.

```bash
python3 redshadow.py -m post
```

**Features:**
- Privilege escalation detection
- Credential extraction

---

### 4. Evasion (evasion)

Bypass security measures and remove traces.

```bash
python3 redshadow.py -m evasion
```

**Features:**
- Log cleaning
- Endpoint detection evasion

---

### 5. Reporting (report)

Generate attack logs and reports.

```bash
python3 redshadow.py -m report
```

**Features:**
- JSON/PDF report generation
- SIEM tool integration

---

## **Configuration**

Modify `core/config.py` to set API keys and logging paths.

Example:
```python
API_KEYS = {
    "shodan": "YOUR_SHODAN_API_KEY",
    "virustotal": "YOUR_VIRUSTOTAL_API_KEY"
}
```

---

## **Logging & Reporting**

RedShadow logs all actions in `redshadow.log` and stores reports in `reports/`.

Check logs:
```bash
cat redshadow.log
```
View reports:
```bash
cat reports/report.json
```

---

## **Updating**

Keep RedShadow up to date with:
```bash
python3 core/updater.py
```

---

## **Contributing**

Contributions are welcome! Follow these steps:

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit changes (`git commit -m "Description of changes"`)  
4. Push to GitHub (`git push origin feature-name`)  
5. Submit a pull request  

---

## **License**

**MIT License**  

```txt
MIT License

© 2025 InfosecSamurai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
