vowel= 0
consonant = 0
var = input("Enter a string: ")
vowels = 'aeiouAEIOU'
for i in var:
    if i in vowels:
        vowel =vowel+ 1
    else:
        consonant += 1
print('Count of vowels:', vowel)
print('Count of consonants:', consonant)
