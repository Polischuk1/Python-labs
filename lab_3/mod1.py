from googletrans import Translator  # type: ignore

translator = Translator(service_urls=['translate.googleapis.com'])

def transLate(text, lang):
    try:
        res = translator.translate(text, dest=lang)
        return res.text
    except Exception as e:
        print(f"Error in translation: {e}")
        return None


def LangDetect(text):
    try:
        res = translator.detect(text)
        return res.lang, res.confidence
    except Exception as e:
        print(f"Error in language detection: {e}")
        return None, None


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

def CodeLang(lang):
    if lang.capitalize() in lang_dictionary:
        return lang_dictionary[lang.capitalize()]
    elif lang in lang_dictionary.values():
        for name, code in lang_dictionary.items():
            if code == lang:
                return name
    else:
        raise ValueError("Language not found in dictionary")
