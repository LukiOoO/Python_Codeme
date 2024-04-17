import colorama


def print_hang_man(try_number):
    if try_number == 10:
        print("")
    if try_number == 9:
        print(f_h1)
    if try_number == 8:
        print(f_h2)
    if try_number == 7:
        print(f_h3)
    if try_number == 6:
        print(f_h4)
    if try_number == 5:
        print(f_h5)
    if try_number == 4:
        print(f_h6)
    if try_number == 3:
        print(f_h7)
    if try_number == 2:
        print(f_h8)
    if try_number == 1:
        print(f_h9)
    if try_number == 0:
        print(colorama.Fore.RED + final_hangman)





final_hangman = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       ┌┴┐
       |                SORRY YOU'RE DEAD
    ___|___             
'''

f_h9 = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |      
       |                
    ___|___             
'''

f_h8 = '''
       ┌--------┐
       |        |
       |        O
       |       
       |      
       |                
    ___|___             
'''

f_h7 = '''
       ┌--------┐
       |        |
       |        
       |       
       |      
       |                
    ___|___             
'''

f_h6 = '''
       ┌--------┐
       |       
       |        
       |       
       |      
       |                
    ___|___             
'''

f_h5 = '''
     
       |       
       |        
       |       
       |      
       |                
    ___|___             
'''

f_h4 = '''

        
       |        
       |       
       |      
       |                
    ___|___             
'''

f_h3 = '''


    
       |       
       |      
       |                
    ___|___             
'''

f_h2 = '''



          
       |      
       |                
    ___|___             
'''

f_h1 = '''




       
       |                
    ___|___             
'''

if __name__ == '__main__':
    print_hang_man(1)