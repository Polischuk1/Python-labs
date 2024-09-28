
import translators as ts # type: ignore
from googletrans import Translator # type: ignore


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



def transLate(text,lang):
    try:
        res = ts.google(text, to_language=lang)
        return res
    except Exception as e:
        print(f"Error in translation: {e}")
        return None

def LangDetect(text):
    res = translator.detect(text)
    return res.lang, res.confidence  

def CodeLang(lang):
     # Перевірка, чи lang є назвою мови
    if lang.capitalize() in lang_dictionary:
        return lang_dictionary[lang.capitalize()]
    # Перевірка, чи lang є кодом мови
    elif lang in lang_dictionary.values():
        # Пошук назви мови за кодом
        for name, code in lang_dictionary.items():
            if code == lang:
                return name
    else:
        raise ValueError("Language not found in dictionary")
                
    
            
        

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