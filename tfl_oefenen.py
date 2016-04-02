#!/usr/bin/python

import random
import time
import sys


def main(naam = ""):
  TOTAAL_AANTAL_SOMMEN = 20
  STREEFTIJD_PER_SOM = 1.8

  aantalGoed = 0
  maxDoelTijd = STREEFTIJD_PER_SOM * TOTAAL_AANTAL_SOMMEN
  straf = STREEFTIJD_PER_SOM * 2
  vorigeTafel = -1
  vorigeLoper = -1
  fouteTafel = []
  fouteLoper = []

  if naam == "":
    naam = raw_input("Naam: ")
  print "Welkom " + naam

  startTijd = time.time()

  for aantal in range(1, TOTAAL_AANTAL_SOMMEN + 1):

    tafel = getRandomNumbers(range(3,5), vorigeTafel)
    vorigeTafel = tafel
    loper = getRandomNumbers(range(1,10), vorigeLoper)
    vorigeLoper = loper
    som = str(loper) + " x " + str(tafel) + " = "
    poging = getNumericInput(som)
    if (poging ==  loper * tafel):
      aantalGoed = aantalGoed + 1
    else:
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
  print "Totaal oefen tijd: " + str(totaalOefenTijd)
  teLangzaamTijd = totaalOefenTijd - maxDoelTijd
  print "Voorlopig te langzame tijd: " + str(teLangzaamTijd)
  if (totaalOefenTijd <= maxDoelTijd):
      print "====>>>>>>>> Goed Gedaan !!!!!!"
  else:
    if (totaalFout != 0):
      print "=================================\n"
      print "Herkansing voor foutieven"
      herkansdeGoede = 0
      for index in range(0,len(fouteTafel)):
        som = str(fouteLoper[index]) + " x " + str(fouteTafel[index]) + " = "
        poging = getNumericInput(som)
        if (poging == fouteLoper[index] * fouteTafel[index]):
          print "Goed"
          herkansdeGoede = herkansdeGoede + 1
        else:
          print "Fout, antwoord is: " + str(fouteLoper[index] * fouteTafel[index])
      if herkansdeGoede != 0:
        print "Bonus tijd vanwege goede herkansing: " + str(herkansdeGoede) + " seconden"
      teLangzaamTijd = teLangzaamTijd - herkansdeGoede
  print str(teLangzaamTijd) + " seconden te langzaam"
  print "==========================================="
  if (teLangzaamTijd < 0):
    print " Je ben klaar voor vandaag"
  elif (teLangzaamTijd < 10):
    print " Je mag 2 spelletjes doen"
  elif (teLangzaamTijd < 20):
    print " Je mag 1 spelletje doen"
  elif (teLangzaamTijd < 30):
    print " Bijna voldoende voor een spelletje"
  else:
    print " Probeer maar eens overnieuw"
  print "==========================================="
  with open("tfl_resultaten.txt", "a") as resultsFile:
    resultsFile.write(naam + ":" + str(teLangzaamTijd) + "\n")

def getNumericInput(som):
  poging = -1
  try:
    poging = raw_input(som)
    while poging == "":
      poging = raw_input(som)
    poging = int(poging)
  except ValueError:
    print "geen getal"
  return poging


def getRandomNumbers(reeks, previous):
  rnd = random.choice(reeks)
  while (rnd == previous):
    rnd = random.choice(reeks)
  return rnd

if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1])
  else:
    main("")