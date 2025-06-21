from smartphone import Smartphone

smartphone_1 = Smartphone("Самсунг", "1", "+79877")
smartphone_2 = Smartphone("Самсунг", "4", "5800")
smartphone_3 = Smartphone("LG", "3", "5899")
smartphone_4 = Smartphone("Моторолла", "1", "5877")
smartphone_5 = Smartphone("Моторолла", "5", "8976")

catalog = [
    smartphone_1,
    smartphone_2,
    smartphone_3,
    smartphone_4,
    smartphone_5
    ]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.num}")
