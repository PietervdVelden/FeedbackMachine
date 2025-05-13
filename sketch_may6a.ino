const int irSensorJaPin = 2;
const int irSensorNeePin = 4;

int scoreJa = 0;
int scoreNee = 0;

bool vorigeJa = true;
bool vorigeNee = true;

unsigned long lastJaTrigger = 0;
unsigned long lastNeeTrigger = 0;

const unsigned long cooldown = 700; // in ms

void setup() {
  pinMode(irSensorJaPin, INPUT);
  pinMode(irSensorNeePin, INPUT);
  Serial.begin(9600);
}

void loop() {
  unsigned long now = millis();

  bool huidigeJa = digitalRead(irSensorJaPin);
  bool huidigeNee = digitalRead(irSensorNeePin);

  bool scoreChanged = false;

  if (vorigeJa == HIGH && huidigeJa == LOW && (now - lastJaTrigger > cooldown)) {
    scoreJa++;
    lastJaTrigger = now;
    scoreChanged = true;
  }

  if (vorigeNee == HIGH && huidigeNee == LOW && (now - lastNeeTrigger > cooldown)) {
    scoreNee++;
    lastNeeTrigger = now;
    scoreChanged = true;
  }

  vorigeJa = huidigeJa;
  vorigeNee = huidigeNee;

  if (scoreChanged) {
    Serial.println("COUNTING:");
    Serial.print("yes: ");
    Serial.println(scoreJa);
    Serial.print("no: ");
    Serial.println(scoreNee);
    Serial.println();
  }
}
