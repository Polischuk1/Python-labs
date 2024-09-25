
import translators as ts # type: ignore
from googletrans import Translator # type: ignore

from lab_3.mod1 import transLate,LangDetect,CodeLang
translator = Translator(service_urls=['translate.googleapis.com'])
lang_dictionary = {
    "English": "en",
    "Ukrainian": "uk",
    "German": "de",
    "French": "fr",
    "Spanish": "es",
    "Chinese": "zh",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko"
}

while True:
    try:   
        texttransl = input("Enter text to translate: ").lower().strip()
        for lang,code in lang_dictionary.items():
            print(f"{lang}:{code}")  
                
        chooselg = input("Enter the language you want to translate to: ").strip().capitalize()

        if chooselg in lang_dictionary:
            chooselg = CodeLang(chooselg)
            break   
        elif chooselg in lang_dictionary.values():
            break
        else:
            raise ValueError("Invalid language code. Please try again.")
    
    except ValueError as ve:
        print(ve)
        

print(transLate(texttransl,chooselg))

detected_lang, confidence = LangDetect(texttransl)
print(f"Detected language: {detected_lang} with confidence: {confidence}")

print("full name or code: ", CodeLang(chooselg))