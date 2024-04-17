#Przekopiuj zawartość import this do zmiennej.
#
#import this
#Policz liczbę wystąpień słowa better.
#
#Usuń z tekstu symbol gwiazdki
#
#Zamień jedno wystąpienie explain na understand
#
#Usuń spacje i połącz wszystkie słowa myślnikiem
#
#Podziel tekst na osobne zdania za pomocą kropki
#



import this

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
<module 'this' from 'X:\\programowanie\\python\\lib\\this.py'>

Process finished with exit code 0"""
print()
t1 = text.count("better")
print("better występuje",t1)
print()
t2 = text.replace("*","")
print(t2)


t3 = text.replace("explain", "understand",1)

print(t3)

t4 = text.replace(" ","-")
print(t4)







