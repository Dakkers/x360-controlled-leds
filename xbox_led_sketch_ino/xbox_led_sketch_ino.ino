int led_A = 2;
int led_B = 3;
int led_X = 4;
int led_Y = 5;
//int motorA = 10;
//int motorB = 11;

int counter, buttonID, value;
char incomingByte;

void setup() {
  Serial.begin(300);
  
  pinMode(led_A, OUTPUT);
  pinMode(led_B, OUTPUT);
  pinMode(led_X, OUTPUT);
  pinMode(led_Y, OUTPUT);
}

void loop() {
  counter = 0;
  
  while (Serial.available() > 0) {
    incomingByte = Serial.read();
    value = incomingByte - '0';
    
    if (counter%2 == 0) {
      buttonID = value-4;
    } else {
      digitalWrite(buttonID, value);
    }
    
    counter++;
  }
}
