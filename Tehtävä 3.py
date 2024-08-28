sukupuoli = input("Kumpi olet:")
hemoglobiiniarvo = int(input("Paljonko hemoglobiiniarvosi on:"))

if sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    if hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    if 134 <= hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvosi on normaali.")

if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    if hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    if 117 <= hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvosi on normaali.")