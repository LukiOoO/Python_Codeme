# 5▹ Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.


def get_text():
    with open("tekst.txt","r",encoding="utf-8") as f:
        content = f.read()
    return content


def clean_text(text):
    extracs = ".!,()-—"

    for i in extracs:
        text = text.replace(i, "")
    return text


def longest_word(text):
    content = text.split()
    longest_word = ""
    for word in content:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

text = get_text()
text = clean_text(text)



search_word = longest_word(text)


print(search_word, "o długości -",len(search_word))