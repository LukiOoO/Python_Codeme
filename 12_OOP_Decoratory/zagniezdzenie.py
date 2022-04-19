def show_stars():
    def inside_function(): # funkcja lokalna
        print('stars')

    return inside_function


returned_function_name = show_stars()

returned_function_name()