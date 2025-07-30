# modules/zxcvbn_checker.py

from zxcvbn import zxcvbn

def evaluate_password_strength(password):
    result = zxcvbn(password)
    
    score = result['score']
    crack_time = result['crack_times_display']['offline_fast_hashing_1e10_per_second']
    feedback = result['feedback']

    return {
        "score": score,
        "crack_time": crack_time,
        "feedback": feedback
    }
