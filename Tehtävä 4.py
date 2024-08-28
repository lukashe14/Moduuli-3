vuosi = int(input("Vuosi:"))

if (vuosi % 4 == 0):
    if (vuosi % 100 == 0):
        if (vuosi % 400 == 0):
            print("Vuosi on karkaus vuosi.")
        else:
            print("Vuosi ei ole karkausvuosi.")
    else:
        print("Vuosi ei ole karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")