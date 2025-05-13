# Interactieve Feedback-installatie

Een fysieke installatie waarmee mensen kunnen stemmen door een bal door een hoepel te gooien. De stemmen worden geregistreerd via infraroodsensoren en live weergegeven op een extern scherm met een Python GUI.

## Projectbeschrijving

Deze interactieve installatie combineert fysiek stemmen met digitale visualisatie. Gebruikers gooien een bal door een JA- of NEE-hoepel. Een Arduino registreert de onderbreking van een IR-sensor, telt de stem, en stuurt deze door via USB. Python leest deze data uit en toont het live op een extern scherm.

## Installatie

1. Sluit de Arduino aan via USB
2. Upload de juiste code via de Arduino IDE (zie `arduino_score_counter.ino`)
3. Zorg dat Python 3 is geïnstalleerd op je systeem
4. Installeer de benodigde libraries:
```bash
pip3 install pyserial pillow
```
5. Zet het bestand `fontys_logo.png` in dezelfde map als `feedback_display.py`
6. Start de GUI met:
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
- `fontys_logo.png`: optioneel logo dat rechtsboven in beeld wordt getoond
- `arduino_score_counter.ino`: Arduino-code die de stemmen telt en via serial doorstuurt

## Wat leer je hiervan?

- Werken met seriële communicatie tussen Arduino en Python
- Data visualiseren in een GUI
- Input verwerken van fysieke interactie
- Installatie geschikt maken voor Raspberry Pi of dual screen
- Versiebeheer toepassen met duidelijke structuur, commits en documentatie

---

Door dit goed te documenteren en structureren, voldoet dit project aan de verwachtingen van versiebeheer, herbruikbaarheid en overdraagbaarheid.
