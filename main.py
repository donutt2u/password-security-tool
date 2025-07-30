# src/main.py

import sys
import os
# Add project root to sys.path so Python can find modules/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import re
import getpass
import subprocess
from termcolor import colored
from modules.zxcvbn_checker import evaluate_password_strength
from modules.logger import log_password_evaluation

def regex_password_check(password):
    issues = []
    if len(password) < 8:
        issues.append("Password is too short (minimum 8 characters).")
    if not re.search(r"[A-Z]", password):
        issues.append("Missing uppercase letter.")
    if not re.search(r"[a-z]", password):
        issues.append("Missing lowercase letter.")
    if not re.search(r"[0-9]", password):
        issues.append("Missing number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("Missing special character.")
    return issues

def evaluate_password():
    print(colored("\n🔍 Password Evaluation", "cyan"))
    print("-----------------------------")

    try:
        password = getpass.getpass("Enter the password to evaluate: ")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return

    print("\n[+] Running regex checks...")
    issues = regex_password_check(password)

    if not issues:
        print(colored("✅ Passed basic strength checks", "green"))
    else:
        print(colored("❌ Weak password:", "red"))
        for issue in issues:
            print(colored(f"  - {issue}", "yellow"))

    print("\n[+] Running zxcvbn analysis...")
    strength = evaluate_password_strength(password)

    print(colored(f"\nZxcvbn Score: {strength['score']} / 4", "cyan"))
    print(colored(f"Estimated Crack Time: {strength['crack_time']}", "cyan"))

    if strength['feedback']['warning']:
        print(colored(f"⚠️  Warning: {strength['feedback']['warning']}", "red"))
    if strength['feedback']['suggestions']:
        print(colored("💡 Suggestions:", "yellow"))
        for tip in strength['feedback']['suggestions']:
            print(colored(f"  - {tip}", "yellow"))

    log_password_evaluation(password, issues, strength)
    print(colored("\n📁 Evaluation saved to reports/password_evaluations.log", "green"))

def crack_password():
    print(colored("\n💥 Simulate Cracking with John the Ripper", "cyan"))
    print("----------------------------------------------")
    hash_path = input("Enter path to hash file: ")
    wordlist_path = input("Enter path to wordlist: ")

    if not os.path.exists(hash_path):
        print(colored("❌ Hash file not found!", "red"))
        return
    if not os.path.exists(wordlist_path):
        print(colored("❌ Wordlist file not found!", "red"))
        return

    print(colored("\n[+] Cracking started using John the Ripper...\n", "cyan"))
    try:
        subprocess.run([
            "john",
            f"--wordlist={wordlist_path}",
            "--format=sha512crypt",
            hash_path
        ])
    except Exception as e:
        print(colored(f"Error running john: {e}", "red"))
        return

    print(colored("\n[+] Showing cracked result...\n", "cyan"))
    subprocess.run(["john", "--show", hash_path])

def main_menu():
    while True:
        print(colored("\n🔐 Password Security Tool – CLI Dashboard", "blue"))
        print("==============================================")
        print("[1] Evaluate Password")
        print("[2] Simulate Crack with John the Ripper")
        print("[3] Exit")

        choice = input("Select an option [1-3]: ")

        if choice == "1":
            evaluate_password()
        elif choice == "2":
            crack_password()
        elif choice == "3":
            print(colored("👋 Exiting. Stay secure!", "green"))
            break
        else:
            print(colored("❌ Invalid choice. Try again.", "red"))

if __name__ == "__main__":
    main_menu()
