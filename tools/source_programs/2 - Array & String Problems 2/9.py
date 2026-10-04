# Count Vowels and Consonants in a string :

str_val = "Hello World"
vowels = 0
consonants = 0
str_val = str_val.lower()

for ch in str_val:
    if 'a' <= ch <= 'z':
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}, Consonants: {consonants}")


# Output : 

# Vowels: 3, Consonants: 7