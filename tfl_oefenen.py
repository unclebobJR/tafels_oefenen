#!/usr/bin/python

import random
import time

TOTAAL_AANTAL_SOMMEN = 10
STREEFTIJD_PER_SOM = 1.8

aantalGoed = 0
startTijd = time.time()
maxDoelTijd = STREEFTIJD_PER_SOM * TOTAAL_AANTAL_SOMMEN
straf = STREEFTIJD_PER_SOM
vorigeTafel = -1
vorigeLoper = -1
fouteTafel = []
fouteLoper = []

naam = raw_input("Naam: ")

for aantal in range(1, TOTAAL_AANTAL_SOMMEN + 1):
  tafel = random.randint(3,5)
  while (tafel == vorigeTafel):
    tafel = random.randint(3,5)
  vorigeTafel = tafel
  loper = random.randint(1,10)
  while (loper == vorigeLoper):
    loper = random.randint(1,10)
  vorigeLoper = loper
  som = str(loper) + " x " + str(tafel) + " = "
  try:
    poging = raw_input(som)
    while poging == "":
      poging = raw_input(som)
    poging = int(poging)
    if (poging ==  loper * tafel):
      aantalGoed = aantalGoed + 1
    else:
      fouteTafel.append(tafel)
      fouteLoper.append(loper)
  except ValueError:
      print "Geen getal"
      fouteTafel.append(tafel)
      fouteLoper.append(loper)
      

eindTijd = time.time() - startTijd
totaalFout = TOTAAL_AANTAL_SOMMEN - aantalGoed
print "Totaal aantal sommen: " + str(TOTAAL_AANTAL_SOMMEN)
print "Totaal goed: " + str(aantalGoed)
print "Totaal fout: " + str(totaalFout)
print "Eind Tijd: " + str(eindTijd)
print "Doel Tijd: " + str(maxDoelTijd)
strafTijd = straf * totaalFout
print "Straf Tijd: " + str(strafTijd)
totaalOefenTijd = strafTijd  + eindTijd
teLangzaamTijd = totaalOefenTijd - maxDoelTijd
if (totaalOefenTijd <= maxDoelTijd):
    print "====>>>>>>>> Goed Gedaan !!!!!!"
else:
    print str(teLangzaamTijd) + " seconden te langzaam"
with open("tfl_resultaten_" + naam + ".txt", "a") as resultsFile:
  resultsFile.write(str(teLangzaamTijd) + "\n")

for index in range(0,len(fouteTafel)):
  som = str(fouteLoper[index]) + " x " + str(fouteTafel[index]) + " = "
  poging = raw_input(som)
  poging = int(poging)
  if (poging == fouteLoper[index] * fouteTafel[index]):
    print "Goed"
  else:
    print "Fout, antwoord is: " + str(fouteLoper[index] * fouteTafel[index])
  
