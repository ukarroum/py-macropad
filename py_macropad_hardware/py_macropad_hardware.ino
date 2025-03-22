// Vol
int volPin = A1;
int vol = 0;

// Btn
int btnPin = 2;

void setup()
{
  Serial.begin(9600);

  pinMode(btnPin, INPUT);
}

void loop()
{
  vol = analogRead(volPin);

  Serial.print("VOL ");
  Serial.print(vol);
  Serial.print("\n");

  if(digitalRead(btnPin) == HIGH)
  {
    Serial.print("BTN\n");
    delay(200);
  }
    
}
