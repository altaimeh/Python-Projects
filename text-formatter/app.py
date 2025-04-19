print("TEXT CAPITALIZER")

text = input("Enter text to capitalize: ")

capitalized_text = text.upper()
lowered_text = text.lower()
title_text = text.title()
sentence_case_text = text.capitalize()

input_choice = input("Choose an option:\n1. Capitalized\n2. Lowered\n3. Title Case\n4. Sentence Case\n")

if input_choice == '1':
    print("Capitalized Text:", capitalized_text)
elif input_choice == '2':
    print("Lowered Text:", lowered_text)
elif input_choice == '3':
    print("Title Case Text:", title_text)
elif input_choice == '4':
    print("Sentence Case Text:", sentence_case_text)