from deep_translator import GoogleTranslator
from langdetect import detect_langs

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

def transLate(text, lang):
    try:
        # Using deep_translator's GoogleTranslator for translation
        translated_text = GoogleTranslator(source='auto', target=lang).translate(text)
        return translated_text
    except Exception as e:
        print(f"Error in translation: {e}")
        return None

def LangDetect(text):
    try:
        # Using langdetect's detect_langs for language detection
        res = detect_langs(text)
        # res returns a list of detected languages with confidence scores
        return res[0].lang, res[0].prob
    except Exception as e:
        print(f"Error in language detection: {e}")
        return None, None

def CodeLang(lang):
    if lang.capitalize() in lang_dictionary:
        return lang_dictionary[lang.capitalize()]
    elif lang in lang_dictionary.values():
        for name, code in lang_dictionary.items():
            if code == lang:
                return name
    else:
        raise ValueError("Language not found in dictionary")
