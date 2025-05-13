# Interactieve Feedback-installatie

Een fysieke installatie waarmee mensen kunnen stemmen door een bal door een hoepel te gooien. De stemmen worden gelezen via infraroodsensoren en live weergegeven op een tweede scherm met een Python GUI.

## Projectbeschrijving

Deze interactieve installatie combineert fysiek stemmen met digitale visualisatie. Gebruikers gooien een bal door een JA- of NEE-hoepel. Een Arduino registreert de onderbreking van een IR-sensor, telt de stem, en stuurt deze door via USB. Python leest deze data uit en toont het live op een extern scherm.

## Installatie

1. Sluit de Arduino Uno aan via USB-A
2. Upload de juiste code via de Arduino IDE (zie `sketch_may6a.ino`)
3. Zorg dat Python 3 is geïnstalleerd op je systeem
4. Installeer de benodigde libraries:
```bash
pip3 install pyserial pillow
```
5. Start de GUI met:
```bash
python3 feedback_display.py
```

## Gebruikte technologieën

- **Arduino Uno** met IR break beam sensoren
- **Python 3** met:
  - `tkinter` (voor GUI)
  - `pyserial` (voor seriële communicatie)
  - `Pillow` (voor het laden van het Fontys-logo)

## Structuur van de code

- `feedback_display.py`: hoofdscript voor het live tonen van de scores
- `arduino_score_counter.ino`: Arduino-code die de stemmen telt en via serial doorstuurt

## Wat leer je hiervan?

- Werken met seriële communicatie tussen Arduino en Python
- Data visualiseren in een GUI
- Input verwerken van fysieke interactie
- Versiebeheer toepassen met duidelijke structuur, commits en documentatie
