# Interactieve Feedback-installatie

Dit project is een interactieve installatie waarmee mensen hun mening kunnen geven door een bal door een hoepel te gooien. Eén hoepel staat voor “JA”, de andere voor “NEE”. De installatie telt automatisch de stemmen en toont live de tussenstand op een groot scherm.

## Wat zit erin?
- **Arduino Uno** met IR-beams voor het registreren van stemmen  
- **Python GUI** (met Tkinter) die scores toont op een extern scherm  
- **Seriële communicatie** tussen Arduino en Python  
- **Kleurgebruik** afgestemd op de fysieke installatie (fel groen en oranje)

## Waarom?
Ik wilde een simpele, fysieke manier om feedback te verzamelen die leuk is om te gebruiken en direct duidelijkheid geeft. Het combineert techniek, design en interactie op een speelse manier.

## Hoe werkt het?
1. Arduino telt JA/NEE-stemmen via IR-sensoren.  
2. Data wordt doorgestuurd via USB naar een computer of Raspberry Pi.  
3. Python leest de data uit en toont dit fullscreen op een tweede scherm.  
4. Je ziet live de scores en de stelling erboven.
