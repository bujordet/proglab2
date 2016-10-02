

const int buttonPin = 8;
const int ledPin = 7;
const int ledPin2 = 9;
const int ledPin3 = 10;
const long debounce = 20;

int buttonState = 0;

void setup() {
  // put your setup code here, to run once:
  //initializing the button and the LED pins, as input and uoutput
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(buttonPin, INPUT);
  //digitalWrite(buttonPin, HIGH);

  
}

void loop() {
  int timer1 = millis();
  while (digitalRead(buttonPin) == LOW){
    int timer2 = millis();
    if ((timer2 - timer1) > 5000){
      digitalWrite(ledPin3, HIGH);
    }
  }
  int timer2 = millis();
  if ((timer2 - timer1) > 5000){
    Serial.println(3);
  }
  else if ((timer2 - timer1) > 800){
    Serial.println(2);
  }

  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin, LOW);

  while(digitalRead(buttonPin) == HIGH){
  
    
  }
  int timer3 = millis();
  if ((timer3 - timer2)>3000){
    Serial.println(4);
  }
  else if((timer3 - timer2) > 300){
    Serial.println(1);
    digitalWrite(ledPin2, HIGH);
  }
  else if((timer3 - timer2) > 50){
    Serial.println(0);
    digitalWrite(ledPin, HIGH);
  }
  digitalWrite(ledPin3, LOW);
}

