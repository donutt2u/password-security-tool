# modules/logger.py

import os
from datetime import datetime

def log_password_evaluation(password, regex_issues, zxcvbn_result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_path = os.path.join("reports", "password_evaluations.log")

    with open(report_path, "a") as log:
        log.write(f"\n--- Password Evaluation @ {timestamp} ---\n")
        log.write(f"Input Password: {'*' * len(password)}\n")
        
        if regex_issues:
            log.write("Regex Issues:\n")
            for issue in regex_issues:
                log.write(f"  - {issue}\n")
        else:
            log.write("Regex Check: Passed all criteria.\n")
        
        log.write(f"\nZxcvbn Score: {zxcvbn_result['score']} / 4\n")
        log.write(f"Estimated Crack Time: {zxcvbn_result['crack_time']}\n")

        if zxcvbn_result['feedback']['warning']:
            log.write(f"Warning: {zxcvbn_result['feedback']['warning']}\n")

        if zxcvbn_result['feedback']['suggestions']:
            log.write("Suggestions:\n")
            for tip in zxcvbn_result['feedback']['suggestions']:
                log.write(f"  - {tip}\n")

        log.write("-----------------------------------------------------\n")
