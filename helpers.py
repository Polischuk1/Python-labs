def is_point_in_triangle(a, b, x, y):

    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    A = (a, 0)
    B = (0, b)
    C = (0, 0)
    P = (x, y)

    d1 = sign(P, A, B)
    d2 = sign(P, B, C)
    d3 = sign(P, C, A)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)

def translate_text(text, lang):
    translations = {
        'uk': {
            "Числа a, b:": "Числа a, b:",
            "Координати точки А(x,y):": "Координати точки А(x,y):",
            "Точка A належить трикутнику.": "Точка A належить трикутнику.",
            "Точка A не належить трикутнику.": "Точка A не належить трикутнику."
        },
        'en': {
            "Числа a, b:": "Numbers a, b:",
            "Координати точки А(x,y):": "Coordinates of point A(x,y):",
            "Точка A належить трикутнику.": "Point A belongs to the triangle.",
            "Точка A не належить трикутнику.": "Point A does not belong to the triangle."
        }
    }
    return translations.get(lang, translations['uk']).get(text, text)
