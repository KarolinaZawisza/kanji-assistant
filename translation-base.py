ion-base.py

from googletrans import Translator

def translate_to_japanese(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='ja')
    return translated_text.text

# Get input from the user
input_text = input("Enter the text you want to translate to Japanese: ")

# Translate the input text to Japanese
translated_text = translate_to_japanese(input_text)
print("Translated text in Japanese:", translated_text)