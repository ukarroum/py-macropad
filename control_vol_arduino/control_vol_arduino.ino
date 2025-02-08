int volPin = A1;
int vol = 0;


void setup()
{
  Serial.begin(9600);
}

void loop()
{
  vol = analogRead(volPin);

  Serial.print("VOL ");
  Serial.print(vol);
  Serial.print("\n");
}
