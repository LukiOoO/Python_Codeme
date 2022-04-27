import time
import timeit


def timepassed(function):
    def timed():
        t = timeit.timeit(lambda: function)
        print(t)
    return timed()





@timepassed
def print_whatever():
    print("Hello World")