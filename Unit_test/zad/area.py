def cheack_valeue(v):
    if not (isinstance(v, (int, float))):
        raise ValueError


def rectangle(a, b):
    cheack_valeue(a)
    cheack_valeue(b)

    return a * b

def triangle(a, h):
    cheack_valeue(a)
    cheack_valeue(h)

    return 0.5 * a * h



def trapezoid(a, b, h):
    cheack_valeue(a)
    cheack_valeue(b)
    cheack_valeue(h)

    return 0.5 * (a + b) * h




def is_active():
    return True