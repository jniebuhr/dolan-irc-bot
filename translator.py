import random
import json
import re

translate_dict = json.loads(open("dictionary.json").read())

def translate_word(word):
  if word in translate_dict:
    return random.choice(translate_dict[word])
  return word

def translate(text):
  new_text = []
  for word in text.lower().split():
    new_text.append( translate_word(word) )
  return " ".join(new_text)