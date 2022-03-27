# 9▹ Sprawdź jak wygląda kod modułu antigravity. Korzystając z tego samego sposobu otwarcia dowolnego url pozwól użytkownikowi podać adres www.
# Pamiętaj sprawdzić czy url jest prawidłowy może zaczynać się:
# https://
# http://
# www
# bez www
# Może się kończyć za pomocą:
# .pl
# .com
# Jeśli podany adres nie jest linkiem, podnieś wyjątek URLError, który będzie informował, że url jest nieprawidłowy.
#
# Nie masz dość? Swietnie! Przepisz to zadanie za pomocą wyrażeń regularnych (RegEx)

import webbrowser
from urllib.error import URLError

def ensure_correct_begining(url):
    return url.startswith("https://") or url.startswith("http://")

def ensure_correct_ending(url):
    return url.endswith(".pl") or url.endswith(".com")


def check_http_begeining(url):
    return url.startswith("www.")


def get_url():
    url = input('podaj dowolny url --> ')
    if ensure_correct_begining(url) or ensure_correct_ending(url):
        return url
    elif check_http_begeining(url):
        return 'http://' + url


    else:
        raise URLError ('URL w nieprawidłowym formacie')





def main():
    while True:
        try:
            url = get_url()
            break
        except URLError as message:
            print(message)
    webbrowser.open(f"{url}")


if __name__ == "__main__":
    main()

