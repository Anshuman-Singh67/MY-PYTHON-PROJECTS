import os
import sys

# ANSI color codes for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Stage dictionary: Each difficulty has a series of levels.
# When a word is solved, the 'hint_for_next' is given to the player.
LEVEL_DATA = {
    "1": {
        "name": "Easy (4 Letters)",
        "length": 4,
        "attempts": 6,
        "stages": [
            {
                "word": "CODE",
                "hint_for_next": "A physical or digital device used to secure things."
            },
            {
                "word": "LOCK",
                "hint_for_next": "Raw information or facts processed by a computer."
            },
            {
                "word": "DATA",
                "hint_for_next": "A digital unit made up of 8 bits."
            },
            {
                "word": "BYTE",
                "hint_for_next": "An entrance or barrier in a fence or network."
            },
            {
                "word": "GATE",
                "hint_for_next": None  # Final stage
            }
        ]
    },
    "2": {
        "name": "Medium (6 Letters)",
        "length": 6,
        "attempts": 6,
        "stages": [
            {
                "word": "CIPHER",
                "hint_for_next": "A dedicated computer system providing services to clients."
            },
            {
                "word": "SERVER",
                "hint_for_next": "A math/physics term meaning quantity having direction and magnitude."
            },
            {
                "word": "VECTOR",
                "hint_for_next": "Base-2 numeric system used by modern computers."
            },
            {
                "word": "BINARY",
                "hint_for_next": "A small unit of network data sent across a connection."
            },
            {
                "word": "PACKET",
                "hint_for_next": None
            }
        ]
    },
    "3": {
        "name": "Hard (8 Letters)",
        "length": 8,
        "attempts": 7,
        "stages": [
            {
                "word": "FIREWALL",
                "hint_for_next": "Protection against danger, theft, or unauthorized access."
            },
            {
                "word": "SECURITY",
                "hint_for_next": "The command line interface console."
            },
            {
                "word": "TERMINAL",
                "hint_for_next": "Official rules/procedure governing transmission between devices."
            },
            {
                "word": "PROTOCOL",
                "hint_for_next": "The secret key or phrase used to log in."
            },
            {
                "word": "PASSWORD",
                "hint_for_next": None
            }
        ]
    }
}

def evaluate_guess(target, guess):
    """
    Compares the guess with the target word and returns color-coded feedback.
    Handles duplicate letters accurately.
    """
    target_chars = list(target)
    guess_chars = list(guess)
    feedback = [""] * len(target)

    # First pass: Identify exact position matches (Green)
    for i in range(len(target)):
        if guess_chars[i] == target_chars[i]:
            feedback[i] = f"{GREEN}[{guess_chars[i]}]{RESET}"
            target_chars[i] = None
            guess_chars[i] = None

    # Second pass: Identify letters in word but wrong position (Yellow) or missing (Gray)
    for i in range(len(target)):
        if guess_chars[i] is not None:
            if guess_chars[i] in target_chars:
                feedback[i] = f"{YELLOW}[{guess_chars[i]}]{RESET}"
                target_chars[target_chars.index(guess_chars[i])] = None
            else:
                feedback[i] = f"{GRAY}[{guess_chars[i]}]{RESET}"

    return "".join(feedback)

def play_game():
    print(f"\n{BOLD}{CYAN}=== PASSWORD BREACH: SYSTEM OVERRIDE ==={RESET}")
    print("1. Easy   (4-letter words, 6 attempts)")
    print("2. Medium (6-letter words, 6 attempts)")
    print("3. Hard   (8-letter words, 7 attempts)")
    
    choice = input("\nSelect Difficulty (1-3): ").strip()
    while choice not in LEVEL_DATA:
        choice = input("Invalid option. Enter 1, 2, or 3: ").strip()

    config = LEVEL_DATA[choice]
    stages = config["stages"]
    word_len = config["length"]
    max_attempts = config["attempts"]
    
    current_hint = None

    for stage_num, stage_info in enumerate(stages, start=1):
        target_word = stage_info["word"]
        solved = False

        print("\n" + "=" * 50)
        print(f"{BOLD}STAGE {stage_num}/{len(stages)} | Word Length: {word_len} letters{RESET}")
        
        # Display the hint unlocked from previous stage (if any)
        if current_hint:
            print(f"{CYAN}{BOLD}HINT UNLOCKED FROM PREVIOUS WORD:{RESET} {current_hint}")
        else:
            print(f"{GRAY}(No hint available for Stage 1 - crack it on your own!){RESET}")
        
        print("=" * 50)

        attempts_left = max_attempts
        guesses_history = []

        while attempts_left > 0:
            prompt = f"Attempt [{max_attempts - attempts_left + 1}/{max_attempts}] Guess: "
            guess = input(prompt).strip().upper()

            # Validation
            if len(guess) != word_len or not guess.isalpha():
                print(f"{YELLOW}Warning: Guess must be exactly {word_len} alphabetic letters.{RESET}")
                continue

            # Evaluate guess
            result_str = evaluate_guess(target_word, guess)
            guesses_history.append((guess, result_str))
            
            print(f"Feedback: {result_str}")
            print(f"Legend: {GREEN}Correct Spot{RESET} | {YELLOW}Wrong Spot{RESET} | {GRAY}Not in Word{RESET}")

            if guess == target_word:
                print(f"\n{GREEN}{BOLD}>>> ACCESS GRANTED! Password '{target_word}' cracked! <<<{RESET}")
                solved = True
                break
            
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Attempts remaining: {attempts_left}\n")

        if not solved:
            print(f"\n{BOLD}\033[91m>>> SYSTEM LOCKDOWN! You failed to crack the password. <<<{RESET}")
            print(f"The correct password was: {BOLD}{target_word}{RESET}")
            print("Game Over.\n")
            return

        # Prepare hint for next stage
        current_hint = stage_info["hint_for_next"]
        if current_hint:
            print(f"\n{CYAN}>>> INTEL DECRYPTED: You unlocked a hint for Stage {stage_num + 1}! <<<{RESET}")
            input("Press [Enter] to proceed to the next stage...")

    print(f"\n{BOLD}{GREEN}**************************************************")
    print("CONGRATULATIONS! ALL SECURITY LAYERS CLEARED!")
    print(f"**************************************************{RESET}\n")

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nSession terminated by user.")
        sys.exit(0)