
/*
 * PiHome v1.0
 * http://pihome.harkemedia.de/
 *
 * PiHome Copyright (c) 2012, Sebastian Harke
 * Lizenz Informationen.
 * 
 * This work is licensed under the Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 3.0 Unported License. To view a copy of this license,
 * visit: http://creativecommons.org/licenses/by-nc-sa/3.0/.
 *
*/

int ledPin1 = 7;
int ledPin2 = 6;
int ledPin3 = 5;
int ledPin4 = 4;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
}

void loop() {
  if(Serial.available()){
    char c = Serial.read();
    
    if(c == 'A'){
      digitalWrite(ledPin1, HIGH);
      Serial.print(1);
    }
    if(c == 'B'){
      digitalWrite(ledPin1, LOW);
      Serial.print(0);
    }
    
    if(c == 'C'){
      digitalWrite(ledPin2, HIGH);
      Serial.print(1);
    }
    if(c == 'D'){
      digitalWrite(ledPin2, LOW);
      Serial.print(0);
    }
    
    if(c == 'E'){
      digitalWrite(ledPin3, HIGH);
      Serial.print(1);
    }
    if(c == 'F'){
      digitalWrite(ledPin3, LOW);
      Serial.print(0);
    }
    
    if(c == 'G'){
      digitalWrite(ledPin4, HIGH);
      Serial.print(1);
    }
    if(c == 'H'){
      digitalWrite(ledPin4, LOW);
      Serial.print(0);
    }
    
  }
}
