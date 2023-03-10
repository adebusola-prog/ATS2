# Given a List of subject, objects and verbs, generate a sentence in which 
# at least one word from each item is included in the generated sentence

import random

# Given a List of subject, objects and verbs, generate a sentence in which 
# at least one word from each item is included in the generated sentence

def generate_sentence(n):
   subjects=["Ade", "Ola", "Ope", "Yemi", "She"]
   verbs=["goes", "comes", "rules", "decides", "fits"]
   objects=["there", "home", "her", "it", "beans"]
   sentences=set()

   for i in range(n):
      sentence_to_generate= f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}"
      sentences.add(sentence_to_generate)
      if len(sentences) != len(subjects) * len(verbs) * len(objects):
         print(sentence_to_generate)
      else:
         print("There are no more unique numbers to generate")
         break
      

generate_sentence(1000)
























