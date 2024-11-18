# В большой текстовой строке подсчитать
# количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
from string import punctuation

text = """привет привет привет мир привет"""

text = text.lower()
clear_text = ""
for letter in text:
    if letter not in punctuation:
        clear_text += letter

clear_text = clear_text.replace("\n", " ")

freqs = {}
for word in clear_text.split():
    freqs[word] = freqs.get(word, 0) + 1
freqs_list = sorted(list(freqs.items()), key=lambda x: x[1], reverse=True)
for i in range(10):
    print(freqs_list[i])
