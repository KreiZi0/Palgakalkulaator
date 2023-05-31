


import time # Projektitöö Steven Mirontšuk

# Valem bruto netoks arvutamiseks
def valem(rida):
    arvutus = (rida * 3.6) / 100 # Arvutus, kui brutopalk on suurem kui 500 eurot, tulumaksuga
    arvutus1 = rida - arvutus
    if arvutus1 >= 500:
        arvutus2 = arvutus1 - 500
    else:
        arvutus2 = 0
    arvutus3 = (arvutus2 * 20) / 100 # Arvutus, kui brutopalk on väiksem kui 500 eurot, ilma tulumaksuta
    arvutus4 = arvutus1 - arvutus3
    return arvutus4
    
print("Teisendan brutopalgad netopalgaks etteantud failist.") # Programm väljastab lause ja annab kasutajale teada, mida programm tegema hakkab

nimi = input("Sisestage failinimi: ") # Küsib kasutajalt failinime

fail = open(nimi, encoding = "UTF-8") # Avab faili

järjend = [] # Kasutame järjendit

for rida in fail:
    järjend.append(rida) # Programm loeb failist teie palgad

fail.close() # Sulgeb faili

print("Brutopalgad teie failist:") # Ütleb lause "Brutopalgad teie failist:"

for rida in järjend:
    print(rida.strip() + " €") # Näitab brutopalkasid ja lisab nende taha € märgi
    
enter = input("Vajutage enter, et arvutada bruto netoks. ") # Küsib kasutajalt järgmist liigutust, et arvutada bruto netoks

print("Palgad arvutatakse, oodake.") # ütleb lause "Palgad arvutatakse, oodake"
time.sleep(2) #Programm ootab, enne kui hakkab midagi edasi tegema

print("Tulumaksuvabaks loeti alati kuni 500 eurot.")
print("Tulumaksumääraks oli 20%")
print("Tööstuskindlustusmakse oli 1,6%") # Programm annab kasutajale teada, kuidas arvutati ja mis protsendid maha läksid
print("Kogumispensionimakse oli 2%")

print("Netopalgad: ") # Ütleb lause "Netopalgad:"

for rida in järjend: 
    tulemus = round(valem(int(rida)), 2) # Arvutab valemiga brutopalgad netopalgaks ja lisab üksteise alla ning paneb netopalga taha veel € märgi
    print("{0:.2f}".format(tulemus) + " €")
    
input("Vajutage enter, et väljuda") # Küsib kasutajalt järgmist liigutust, et programm sulgeda
