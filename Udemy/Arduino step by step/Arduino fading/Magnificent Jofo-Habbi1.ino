// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 9;
int brightness = 0;
int fade = 5;

// the setup routine runs once when you press reset:
void setup() {
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  analogWrite(led, brightness);
  brightness += fade;
  if(brightness == 0 || brightness == 255){fade = -fade;}
  delay(10);
}