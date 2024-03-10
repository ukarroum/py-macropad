int volPin = A1;
int vol = 0;

int joyBtn = 2;
int joyXPin = A2;
int joyYPin = A3;

int x = 0;
int y = 0;

void setup()
{
  Serial.begin(9600);

  pinMode(joyXPin, INPUT);
  pinMode(joyYPin, INPUT);
  pinMode(joyBtn, INPUT_PULLUP);
  
}

void loop()
{
  vol = analogRead(volPin);

  //Serial.print("VOL ");
  //Serial.print(vol);
  //Serial.print("\n");

  x = analogRead(joyXPin);
  y = analogRead(joyYPin);
  
  Serial.print("JOYSTICK ");
  Serial.print(x);
  Serial.print(" ");
  Serial.print(y);
  Serial.print("\n");

  if(!digitalRead(joyBtn))
  {
    Serial.print("CLICK\n");
    delay(100);
  }

}
