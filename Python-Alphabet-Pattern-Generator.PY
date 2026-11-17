
# ==========================================
# PYTHON ALPHABET & PATTERN GENERATOR
# Created by: Heena
# ==========================================

# COLOR CODES
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

rainbow = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PROJECT TITLE
print(RED + "=" * 55 + RESET)
print(YELLOW + BOLD +
      "       PYTHON ALPHABET & PATTERN GENERATOR" + RESET)
print(GREEN + "=" * 55 + RESET)

# USER INPUT
word = input(CYAN + "\nEnter Your Name or Word: " + RESET)
word = word.upper()

# 1. ALPHABET NUMBER WITH RAINBOW EMOJIS
print(RED + "\n1. ALPHABET NUMBER GENERATOR" + RESET)
print(GREEN + "=" * 40 + RESET)

for letter in word:
    for number in range(26):
        if letter == alphabet[number]:

            print(rainbow[number % 6] + letter + RESET,
                  "=", number + 1, end=" ")

            for i in range(number + 1):
                print(rainbow[i % 6] + "😊" + RESET, end="")

            print()

# 2. PRINT LETTERS WITH STARS
print(RED + "\n2. LETTER PATTERN GENERATOR" + RESET)
print(GREEN + "=" * 40 + RESET)

for letter in word:
    print(YELLOW + letter + RESET, GREEN + "😊" + RESET)

# 3. REVERSE THE WORD
print(RED + "\n3. REVERSE WORD GENERATOR" + RESET)
print(GREEN + "=" * 40 + RESET)

reverse = ""

for letter in word:
    reverse = letter + reverse

print(PURPLE + "Original Word: " + RESET, word)
print(CYAN + "Reverse Word: " + RESET, reverse)

# 4. CHARACTER COUNT
print(RED + "\n4. CHARACTER COUNTER" + RESET)
print(GREEN + "=" * 40 + RESET)

count = 0

for letter in word:
    count = count + 1

print(YELLOW + "Total Characters: " + RESET, count)

# 5. ALPHABET PATTERN A TO Z
print(RED + "\n5. ALPHABET PATTERN A TO Z" + RESET)
print(GREEN + "=" * 40 + RESET)

for row in range(1, 27):
    for col in range(row):
        print(rainbow[row % 6] +
              chr(64 + row) + RESET, end=" ")
    print()

# 6. COMPLETE ALPHABET
print(RED + "\n6. COMPLETE ALPHABET A TO Z" + RESET)
print(GREEN + "=" * 40 + RESET)

for letter in alphabet:
    print(YELLOW + letter + RESET, end=" ")

print()

# PROJECT COMPLETED
print(RED + "\n" + "=" * 55 + RESET)
print(GREEN + BOLD +
      "       PROJECT COMPLETED SUCCESSFULLY!" + RESET)
print(YELLOW + "       THANK YOU FOR USING MY PROJECT!" + RESET)
print(RED + "=" * 55 + RESET)
