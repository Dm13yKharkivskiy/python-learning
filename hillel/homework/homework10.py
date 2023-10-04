import re


# Завдання №1

read_file = "text.txt"
write_file = "new_text.txt"
pattern = r'[A-z]+\'?[A-z]+'

with open(read_file, "r") as text:
    read_original_text = text.read().split()

with open(write_file, "w") as new_text:
    for word in read_original_text:
        word_alphabetic = re.search(pattern, word)

        if bool(word_alphabetic):
            word_for_write = word_alphabetic.group()

            if len(word_for_write) >= 7:
                new_text.write(word_for_write)
                new_text.write("\n")

    print(f"Wrote success from {read_file} to {write_file}")

# Завдання №2

count_words = 0

with open(read_file, "r") as text:
    read_text = text.read().split()


for word in read_text:
    word_alphabetic = re.search(pattern, word)

    if bool(word_alphabetic):
        count_words += 1

print(f"In file {read_file} count words - {count_words}")

# Додаткове завдання

count_replace = 0
old_word = "die"
new_word = "***"

with open(read_file, "r") as text:
    read_text = text.read().split()

    for i in range(len(read_text)):
        word = re.search(pattern, read_text[i])

        if bool(word):
            word_result = word.group()

            if word_result.lower() == old_word:
                read_text[i] = read_text[i].replace(old_word, new_word)
                count_replace += 1

print(" ".join(read_text))
print(f"{count_replace} replaces word - {old_word}")




