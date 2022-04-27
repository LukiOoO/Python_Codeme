# 3▹ Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki
# , sprawdzenie czy jest pusta, dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).
#
# Utwórz kilka obiektów klasy Queue z różnymi parametrami.

class quene():
    def __init__(self,fifo):
        self.fifo = fifo

    def show(self):
        return self.fifo

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self,element):
        self.fifo.append(element)

    def get(self):
        element = self.fifo.pop(0)
        return element


example_queue = quene([])
print(example_queue.show())
print(example_queue.is_empty())

example_queue.put(6)
example_queue.put(21)
example_queue.put(33)
print(example_queue.show())

example_queue.get()

print(example_queue.show())
