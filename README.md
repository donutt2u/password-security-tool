# 🔐 SentinelPass – Advanced Password Strength Checker & Cracking Simulation

**Internship Project @ NewtonAI Technologies**

`SentinelPass` is a command-line Python tool developed during a cybersecurity internship at **NewtonAI Technologies**. The tool evaluates the strength of passwords using both **regex-based logic** and the **zxcvbn** library, and simulates real-world password attacks using **John the Ripper (JtR)**. This dual-purpose utility aims to **raise awareness about password hygiene** while **educating users on attacker methodologies**.

---

## 🎯 Objectives

- ✅ Educate users about weak vs strong passwords through real-time feedback.
- ✅ Demonstrate dictionary-based cracking using **John the Ripper**.
- ✅ Promote cybersecurity awareness and responsible password practices.
- ✅ Provide a practical and educational example of penetration testing workflows.

---

## 🧠 Features

- 🔍 Regex-based static password strength evaluation  
- 📊 Dynamic password scoring via **zxcvbn** (entropy-based)  
- 🧪 Realistic cracking simulation using **John the Ripper**
- 🔐 Hidden password input using Python’s `getpass`
- 🎨 Color-coded CLI feedback (via `termcolor`)  
- 📝 Password evaluation logs saved in a structured `.log` file  
- 💻 Designed and tested in **Kali Linux** – ideal for ethical hacking labs

---

## 🛠️ Tech Stack

| Component               | Description                                      |
|------------------------|--------------------------------------------------|
| **Python 3.10+**        | Core language for development                   |
| **zxcvbn**              | Dropbox’s password strength estimator           |
| **termcolor**           | Terminal color feedback for better UX          |
| **getpass**             | Hides password input in CLI                    |
| **John the Ripper**     | Simulates dictionary attacks (sha512crypt)     |
| **Kali Linux**          | Penetration testing OS for realistic scenarios |

---

## 📁 Project Directory Structure

```plaintext
password-security-tool/
├── data/
│   └── john_test/
│       ├── shadow_hash.txt        # Hashed passwords (for JtR simulation)
│       └── wordlist.txt           # Dictionary for cracking
├── modules/
│   ├── zxcvbn_checker.py          # zxcvbn-based scoring module
│   └── logger.py                  # Logging utility for password evaluations
├── reports/
│   └── password_evaluations.log   # Output logs for evaluations
├── src/
│   └── main.py                    # CLI main script
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── venv/                          # Python virtual environment (excluded from Git)

---

## 🔧 Installation

### Step 1 – Clone the Repository
```bash
git clone https://github.com/donutt2u/password-security-tool.git
cd password-security-tool
```

### Step 2 – Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Usage

### Run Password Strength Checker
```bash
python3 src/main.py
```

- You’ll be prompted to enter a password.
- The strength is evaluated using regex and zxcvbn.
- Results are logged to: `reports/password_evaluations.log`

---

## ⚔️ Simulate Password Cracking (Kali Linux)

### Step 1 – Install John the Ripper (if not installed)
```bash
sudo apt update && sudo apt install john
```

### Step 2 – Launch Dictionary Attack
```bash
john --wordlist=data/john_test/wordlist.txt --format=sha512crypt data/john_test/shadow_hash.txt
```

### Step 3 – View Cracked Passwords
```bash
john --show data/john_test/shadow_hash.txt
```

---

## 📦 Sample `requirements.txt`
```txt
zxcvbn
termcolor
```

---

## 🛡️ Legal & Ethical Notice

This tool is for **educational and ethical purposes only**.  
Unauthorized use of password cracking tools is **illegal and unethical**. Always obtain **explicit written permission** before performing any security assessments.

**Compliant With:**
- [OWASP A07:2021 – Identification and Authentication Failures](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)
- [ISO/IEC 27001:2022 – Annex A.9: Access Control](https://www.iso.org/standard/27001.html)
- [NIST SP 800-63B – Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)

---

## 🤝 Acknowledgements

- Internship project supervised by **NewtonAI Technologies**
- Inspired by best practices from **OWASP**, **NIST**, and the **ethical hacking community**
- Built using open-source libraries and tools

---

## 📬 Contact

**Muhammad Arslan Akhtar**  
📧 [arslan@premiumhouseware.co.uk](mailto:arslan@premiumhouseware.co.uk)  
🔗 [LinkedIn](https://www.linkedin.com/in/donutt2u)  
🐙 [GitHub](https://github.com/donutt2u)  
🔐 [HackerOne](https://hackerone.com/donutt_2u)
