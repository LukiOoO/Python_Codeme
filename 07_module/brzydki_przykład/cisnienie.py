
import random
STALA_WARTOSC = 100

def pobierz():
    v1 = random.randint(100, 139)
    v2 = random.randint(60, 89)
    return (v1, v2)

def main():
    gorne, dolne = pobierz()
    print(f'{gorne}/{dolne}')

if __name__ == "__main__":
    main()