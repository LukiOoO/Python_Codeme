def uppercase_decorator(func):
    def inside_func():
        txt = func()
        return txt.upper()

    return inside_func


@uppercase_decorator
def daily_news():
    return 'important!'

@uppercase_decorator
def smart_text():
    return 'smart...'

print(smart_text())

print(daily_news())

