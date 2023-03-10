# import string
# letters = string.ascii_letters
vowel_letters ="aeiou"
consonant_letters="bcdfghjklmnpqrstvwxyz"

word= input("enter a word ").lower()
print([f"{word} starts with a consonant", f"{word} starts with a vowel"] [word[0] in vowel_letters])


# A program that takes 5 letter word and prints each letter and say if it
# is a vowel or a consonant(Do not use loop, you can try to avoid if and else)
word= input("enter a word").lower()
word_one=word[0]
word_two=word[1]
word_three=word[2]
word_four=word[3]
word_five=word[4]

print([f"{word[0]} starts with a consonant", f"{word[0]} starts with a vowel"] [word_one in vowel_letters])
print([f"{word[1]} starts with a consonant", f"{word[1]} starts with a vowel"] [word_two in vowel_letters])
print([f"{word[2]} starts with a consonant", f"{word[2]} starts with a vowel"] [word_three in vowel_letters])
print([f"{word[3]} starts with a consonant", f"{word[3]} starts with a vowel"] [word_four in vowel_letters])
print([f"{word[4]} starts with a consonant", f"{word[4]} starts with a vowel"] [word_five in vowel_letters])


