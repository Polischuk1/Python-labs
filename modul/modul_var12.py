    
DATA_FILE = 'MyData.json'

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                print("Некоректні дані у файлі.")
    return None

def write_data(a, b, x, y, lang):
    data = {
        "a": a,
        "b": b,
        "x": x,
        "y": y,
        "language": lang
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)
    print(f"Дані збережено в файл {DATA_FILE}")

def get_user_input():
    a, b = map(int, input("Введіть числа a, b: ").split())
    x, y = map(int, input("Введіть координати точки А(x, y): ").split())
    lang = input("Введіть мову інтерфейсу (uk/en): ").lower()
    if lang not in ['uk', 'en']:
        print("Некоректна мова, за замовчуванням встановлено українську.")
        lang = 'uk'
    write_data(a, b, x, y, lang)

def main():
    data = read_data()

    if data is None:
        get_user_input()
        return

    lang = data.get('language', 'uk')
    a, b = data['a'], data['b']
    x, y = data['x'], data['y']

 
    if lang == 'uk':
        print(f"Мова: Українська")
    else:
        print(f"Language: English")
    
    print(translate_text("Числа a, b:", lang), a, b)
    print(translate_text("Координати точки А(x,y):", lang), x, y)
    
    if is_point_in_triangle(a, b, x, y):
        print(translate_text(f"Точка A({x}, {y}) належить трикутнику.", lang))
    else:
        print(translate_text(f"Точка A({x}, {y}) не належить трикутнику.", lang))

if __name__ == "__main__":
    main()
