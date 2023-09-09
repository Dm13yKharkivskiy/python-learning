# Завдання № 1
try:
    input_string_text = input("Enter a string of any text for English: ")
    count_letters = 0
    count_digits = 0

    for symbol in input_string_text:
        if symbol.isdigit():
            count_digits += 1
        elif symbol.isalpha():
            count_letters += 1

    print("Count letters: {}".format(count_letters))
    print("Count digits: {}".format(count_digits))
except Exception as error:
    print(f"Error: {error}")

# Завдання № 2
try:
    entered_string_text = input("Enter a string of any text length from 10 characters: ")
    entered_search_character = input("Enter some one character for search: ")
    count_search_character = 0
    if len(entered_string_text.strip()) > 9 and len(entered_search_character.strip()) == 1:
        for character in entered_string_text:
            if character == entered_search_character:
                count_search_character += 1
        print(f"Found count of symbol \"{entered_search_character}\": {count_search_character}")
    else:
        print("Incorrect entered text or search character!")
except Exception as error:
    print(f"Error: {error}")


# Завдання № 3
try:
    entered_string_text = input("Enter a string of any text length from 10 characters: ")
    entered_search_word = input("Enter some one word for search from 3 characters: ")
    entered_replace_word = input("Enter some one word for replace 3 characters: ")
    if len(entered_string_text.strip()) > 9 and len(entered_search_word.strip()) > 2 and len(entered_replace_word.strip()) > 2:
        replace_text = entered_string_text.lower().replace(entered_search_word.lower(), entered_replace_word.lower())
        print(f"Entered text: {entered_string_text}")
        print(f"Text with replace word: {replace_text}")
    else:
        print("Incorrect entered text or search or replace characters!")
except Exception as error:
    print(f"Error: {error}")


# Завдання № 4
text_line = "Summer is the most colourful season"
print(f"Text line: {text_line}")
print(f"Third character: {text_line[2]}")
print(f"Penultimate character: {text_line[-2]}")
print(f"First five characters: {text_line[:6]}")
print(f"Text line without the last two characters: {text_line[:len(text_line)-2]}")
print(f"Characters with paired indices: {text_line[::2]}")
print(f"Characters with unpaired indices: {text_line[1::2]}")
print(f"Characters in reverse order: {text_line[::-1]}")
print(f"Characters in reverse order in one: {text_line[::-2]}")
print(f"Length text line: {len(text_line)} characters")

# Додаткове завдання
text = ("summer is the most colourful season! there are a lot of flowers at this time. it is the best time to travel, "
        "to spend several weeks at the seaside or in a village. autumn brings all kinds of fruits and vegetables. We "
        "may also enjoy some warm and pleasant days in september.")
text_edited = ""
prev_index = 0
count_exclamation_marks = 0
count_punctuation_marks = 0
count_digits = 0

print(f"Origin text:\n {text}")

for i in range(len(text)):
    if text[i] in (".?!"):
        if prev_index == 0:
            text_edited = text[prev_index:i + 1].capitalize()
        else:
            text_edited = text_edited + " " + text[prev_index + 1:i + 1].capitalize()
        prev_index = i + 1

print(f"Text with sentences with capital letters:\n {text_edited}")

for character in text:
    if character.isdigit():
        count_digits += 1
    if character == "!":
        count_exclamation_marks += 1
    if character in (",.?:-:!"):
        count_punctuation_marks += 1
print(f"Count digits in text: {count_digits}")
print(f"Count punctuation marks in text: {count_punctuation_marks}")
print(f"Count exclamation marks in text: {count_exclamation_marks}")
