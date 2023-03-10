# A program that takes a word and prints if it starts with a vowel or a consonant
vowel_letters ="aeiou"
consonant_letters="bcdfghjklmnpqrstvwxyz"

word= input("enter a word").lower()
if word[0] in vowel_letters:
   print(f"{word} starts with vowel")
if word[0] in consonant_letters:
   print(f"{word} starts with a consonant")
if word[0] not in vowel_letters and word[0] not in consonant_letters:
   print(f"{word} is not starting with a letter")


#  A program that takes 5 letter word and prints each letter and say if it
#  is a vowel or a consonant(Do not use loop, you can try to avoid if and else)
word= input("enter a word").lower()
if len(word) == 5:
   word_one=word[0]
   # print(word_one)
   word_two=word[1]
   word_three=word[2]
   word_four=word[3]
   word_five=word[4]

   if word_one in vowel_letters:
      print(f"{word_one} is a vowel")
   if word_one in consonant_letters:
      print(f"{word_one} is a consonant")
   if word_one not in vowel_letters and word_one not in consonant_letters:
      print(f"{word_one} is neither a vowel nor a consonant")

   if word_two in vowel_letters:
      print(f"{word_two} is a vowel")
   if word_two in consonant_letters:
      print(f"{word_two} is a consonant")
   if word_two not in vowel_letters and word_two not in consonant_letters:
      print(f"{word_two} is neither a vowel nor a consonant")

   if word_three in vowel_letters:
      print(f"{word_three} is a vowel")
   if word_three in consonant_letters:
      print(f"{word_three} is a consonant")
   if word_three not in vowel_letters and word_three not in consonant_letters:
      print(f"{word_three} is neither a vowel nor a consonant")

   if word_four in vowel_letters:
      print(f"{word_four} is a vowel")
   if word_four in consonant_letters:
      print(f"{word_four} is a consonant")
   if word_four not in vowel_letters and word_four not in consonant_letters:
      print(f"{word_four} is neither a vowel nor a consonant")

   if word_five in vowel_letters:
      print(f"{word_five} is a vowel")
   if word_five in consonant_letters:
      print(f"{word_five} is a consonant")
   if word_five not in vowel_letters and word_five not in consonant_letters:
      print(f"{word_five} is neither a vowel nor a consonant")

else:
   print("Your word should be five characters")



