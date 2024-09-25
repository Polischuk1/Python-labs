from lab_3.mod2 import transLate, LangDetect, CodeLang

def main():
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
            texttransl = input("Enter text to translate: ").strip()
            for lang, code in lang_dictionary.items():
                print(f"{lang}: {code}")

            chooselg = input("Enter the language you want to translate to (name or code): ").strip().capitalize()

            if chooselg in lang_dictionary:
                chooselg = CodeLang(chooselg)
            elif chooselg not in lang_dictionary.values():
                raise ValueError("Invalid language code. Please try again.")

            break  # Exit loop once valid input is entered

        except ValueError as ve:
            print(ve)

    # Perform the translation
    translated_text = transLate(texttransl, chooselg)
    if translated_text:
        print(f"Translated text: {translated_text}")

    # Language detection using langdetect
    detected_lang, confidence = LangDetect(texttransl)
    if detected_lang:
        print(f"Detected language: {detected_lang} with confidence: {confidence}")
    else:
        print("Language detection failed.")

    # Full name or code output
    print(f"Full name or code: {CodeLang(chooselg)}")


if __name__ == "__main__":
    main()
