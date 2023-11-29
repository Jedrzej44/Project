def wiek():
    while True:
        wiek = input("Podaj swój wiek: ")
        if wiek.isdigit():
            print(wiek)
        return wiek

wiek()