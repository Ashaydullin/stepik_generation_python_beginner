def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return not text

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))