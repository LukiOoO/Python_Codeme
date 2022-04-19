def show_stars():
    num = 2

    def inside_function(txt): # funkcja lokalna
        print(txt * num)

    return inside_function


returned_function_name = show_stars()

returned_function_name('ahahah')