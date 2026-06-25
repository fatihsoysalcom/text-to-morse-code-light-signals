import time
import sys

# Dictionary mapping English alphabet and numbers to Morse code
# This represents the encoding of information into a signal format.
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/' # Special character for space between words
}

def text_to_morse(text):
    """Converts a given text string into its Morse code representation."""
    morse_output = []
    for char in text.upper(): # Convert to uppercase for dictionary lookup
        if char in MORSE_CODE_DICT:
            morse_output.append(MORSE_CODE_DICT[char])
        else:
            # For simplicity, ignore characters not in the dictionary
            # In a real system, these might be represented by an error signal or ignored.
            pass
    # Join individual letter Morse codes with a single space
    # This space represents the pause between letters (3 dot durations).
    return ' '.join(filter(None, morse_output))

def simulate_optical_morse(morse_string, dot_duration=0.1):
    """Simulates optical signals for a given Morse code string.
    
    - A dot ('.') is a short flash (⚡).
    - A dash ('-') is a long flash (💡), three times the duration of a dot.
    - A space (' ') between letters is a pause (three dot durations).
    - A slash ('/') between words is a longer pause (seven dot durations).
    """
    print("\nSimulating Morse Code Optical Signals:")
    print("⚡ = Short Flash (Dot), 💡 = Long Flash (Dash)")
    
    for char in morse_string:
        if char == '.':
            sys.stdout.write("⚡") # Represents a short light pulse
            sys.stdout.flush() # Ensure immediate output
            time.sleep(dot_duration) # Duration of a dot
        elif char == '-':
            sys.stdout.write("💡") # Represents a long light pulse
            sys.stdout.flush()
            time.sleep(dot_duration * 3) # Duration of a dash (3x dot)
        elif char == ' ':
            # Pause between letters (3 dot durations)
            sys.stdout.write(" ") 
            sys.stdout.flush()
            time.sleep(dot_duration * 3)
        elif char == '/':
            # Pause between words (7 dot durations)
            sys.stdout.write("   ") 
            sys.stdout.flush()
            time.sleep(dot_duration * 7)
        
    print("\nSimulation complete.")

if __name__ == "__main__":
    # Example message to convert and simulate
    message = "Merhaba Dunya" # "Hello World" in Turkish
    print(f"Original Message: '{message}'")

    # Step 1: Convert the text message into its Morse code equivalent
    morse_code = text_to_morse(message)
    print(f"Morse Code:       '{morse_code}'")

    # Step 2: Simulate the transmission of this Morse code using optical signals
    # This demonstrates the core concept of encoding information into light patterns.
    simulate_optical_morse(morse_code)
