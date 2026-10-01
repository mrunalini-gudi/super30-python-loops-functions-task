#Vowel, Consonant, Digit and Space Counter
sentence = input("Enter a sentence: ")
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0
special_char_count = 0
for char in sentence:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == ' ':
        space_count += 1
    else:
        special_char_count += 1

print("Vowel count:", vowel_count)
print("Consonant count:", consonant_count)
print("Digit count:", digit_count)
print("Space count:", space_count)
print("Special character count:", special_char_count)
