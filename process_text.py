import re
import regex
import string

def remove_user_mention(text):
  return re.sub('@[^\s]+', '', text)

def remove_url(text):
  return re.sub('http\S+|www\S+', '', text)

def remove_hashtag(text):
  return re.sub('#\w+', '', text)

def remove_english_chars(text):
    english_chars_pattern = re.compile(r'[a-zA-Z]')
    cleaned_text = english_chars_pattern.sub('', text)
    return cleaned_text

def normalize_text(text):
  text = re.sub('[ى]', 'ي', text)
  text = re.sub('[إأٱآا]', 'ا', text)
  text = re.sub('[ؤئ]', 'ء', text)
  text = re.sub('[ة]', 'ه', text)
  text = re.sub('گ', 'ك', text)
  text = re.sub(r'(.)\1+', r'\1', text) # remove repeated characters 'هههههه', 'جوول'
  return text

def remove_diacritics(text):
    arabic_diacritics = re.compile('''
                 ّ    | # Tashdid
                 َ    | # Fatha
                 ً    | # Tanwin Fath
                 ُ    | # Damma
                 ٌ    | # Tanwin Damm
                 ِ    | # Kasra
                 ٍ    | # Tanwin Kasr
                 ْ    | # Sukun
                 ـ     # Tatwil/Kashida
             ''', re.VERBOSE)
    return re.sub(arabic_diacritics, '', text)

def remove_numbers(text):
    """
    Removes arabic and english numbers from text
    """
    # Remove English numbers
    text = re.sub(r'[\d]', '', text)

    # Remove Arabic numbers
    text = re.sub('١|٠|٢|٣|٤|٥|٦|٧|٨|٩', '', text)
    return text



def remove_emojis(text):
    # define a regex pattern to match all emojis
    emoji_pattern = regex.compile('[\p{Emoji}]')
    # substitute emojis with an empty string
    cleaned_text = emoji_pattern.sub("", text)
    return cleaned_text

def remove_newlines_and_tabs(text):
    cleaned_text = text.replace('\n', '').replace('\t', '')
    return cleaned_text

def remove_extra_spaces(text):
    words = text.split()
    cleaned_text = ' '.join(words)
    return cleaned_text


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    text = re.sub(r'[^\w\s]', '', text)
    return text

def pre_process_text(text):
  text = remove_user_mention(text)
  text = remove_url(text)
  text = remove_hashtag(text)
  text = remove_english_chars(text)
  text = normalize_text(text)
  text = remove_diacritics(text)
  text = remove_numbers(text)
  text = remove_emojis(text)
  text = remove_newlines_and_tabs(text)
  text = remove_punctuation(text)
  text = remove_extra_spaces(text)
  return text