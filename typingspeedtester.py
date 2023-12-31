import time
import random

paragraphs = ["Start typing, this is to test your typing speed. Make sure you type fast and accurately."]

def typing_test():
    test_text = random.choice(paragraphs)
    print("Type the following:")
    print(test_text)
    input("Press Enter when ready...")

    start_time = time.time()
    user_text = input("Type here: ")
    end_time = time.time()

    time_taken = end_time - start_time 
    num_words = len(test_text.split())
    wpm = num_words/time_taken*60

    accuracy = calculate_accuracy(test_text, user_text)

    print(f"WPM: {wpm}")
    print(f"Accuracy: {accuracy}%")
    print("Keep practicing to improve your typing!")

def calculate_accuracy(test_text, user_text):
    errors = 0
    for i, char in enumerate(test_text):
        try:
            if user_text[i] != char:
                errors += 1
        except IndexError: 
            errors += 1
        
    letters = len(test_text.replace(" ", ""))
    accuracy = ((letters - errors)/letters)*100
    return accuracy
    
typing_test()