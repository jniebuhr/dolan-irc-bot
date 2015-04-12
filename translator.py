import random
import json
import re
import nltk

translate_dict = json.loads(open("dictionary.json").read())

def untokenize(words):
    """
    Untokenizing a text undoes the tokenizing operation, restoring
    punctuation and spaces to the places that people expect them to be.
    Ideally, `untokenize(tokenize(text))` should be identical to `text`,
    except for line breaks.
    """
    text = ' '.join(words)
    step1 = text.replace("`` ", '"').replace(" ''", '"').replace('. . .', '...')
    step2 = step1.replace(" ( ", " (").replace(" ) ", ") ")
    step3 = re.sub(r' ([.,:;?!%]+)([ \'"`])', r"\1\2", step2)
    step4 = re.sub(r' ([.,:;?!%]+)$', r"\1", step3)
    step5 = step4.replace(" '", "'").replace(" n't", "n't").replace(
        "can not", "cannot")
    step6 = step5.replace(" ` ", " '")
    return step6.strip()

def translate_word(word):
  if word in translate_dict:
    return random.choice(translate_dict[word])
  return word

def translate(text):
  text = text.lower()
  tokens = nltk.word_tokenize(text)
  processed_tokens = []
  for t in tokens:
    processed_tokens.append( translate_word(t) )
  return untokenize(processed_tokens)


if __name__ == "__main__":
  print(translate("Hello Goofy! I am Donald! I like Children!"))
