//Thierry Nathan Pereira de Souza
//Caio Eduardo Silva
//Guilherme Macário Silva
//Kaique Silva
//C.K.G.T

#define BOBINA1    2                    
#define BOBINA2    3                    
#define BOBINA3    4                     
#define BOBINA4    5                     

int velocidadeRotacao = 250;

void setup() {
  pinMode(BOBINA1, OUTPUT);
  pinMode(BOBINA2, OUTPUT);
  pinMode(BOBINA3, OUTPUT);
  pinMode(BOBINA4, OUTPUT);
  
  digitalWrite(BOBINA1, HIGH);
  digitalWrite(BOBINA2, HIGH);
  digitalWrite(BOBINA3, HIGH);
  digitalWrite(BOBINA4, HIGH);
}

void loop() {  
  for (int i = 0; i < (2048) ; i++) {
    digitalWrite(BOBINA1, HIGH);
    digitalWrite(BOBINA2, LOW);
    digitalWrite(BOBINA3, LOW);
    digitalWrite(BOBINA4, LOW);
    delayMicroseconds (velocidadeRotacao);

    digitalWrite(BOBINA1, LOW);
    digitalWrite(BOBINA2, LOW);
    digitalWrite(BOBINA3, HIGH);
    digitalWrite(BOBINA4, LOW);
    delayMicroseconds (velocidadeRotacao);

    digitalWrite(BOBINA1, LOW);
    digitalWrite(BOBINA2, HIGH);
    digitalWrite(BOBINA3, LOW);
    digitalWrite(BOBINA4, LOW);
    delayMicroseconds (velocidadeRotacao);

    digitalWrite(BOBINA1, LOW);
    digitalWrite(BOBINA2, LOW);
    digitalWrite(BOBINA3, LOW);
    digitalWrite(BOBINA4, HIGH);
    delayMicroseconds (velocidadeRotacao);
  }
  
  delay(1000);  
  
  for (int i = 0; i < (2048) ; i++) {
    digitalWrite(BOBINA1, LOW);
    digitalWrite(BOBINA2, LOW);
    digitalWrite(BOBINA3, LOW);
    digitalWrite(BOBINA4, HIGH);
    delayMicroseconds (velocidadeRotacao);
    
    digitalWrite(BOBINA1, LOW);
    digitalWrite(BOBINA2, HIGH);
    digitalWrite(BOBINA3, LOW);
    digitalWrite(BOBINA4, LOW);
    delayMicroseconds (velocidadeRotacao);
    
    digitalWrite(BOBINA1, LOW);
    digitalWrite(BOBINA2, LOW);
    digitalWrite(BOBINA3, HIGH);
    digitalWrite(BOBINA4, LOW);
    delayMicroseconds (velocidadeRotacao);
    
    digitalWrite(BOBINA1, HIGH);
    digitalWrite(BOBINA2, LOW);
    digitalWrite(BOBINA3, LOW);
    digitalWrite(BOBINA4, LOW);
    delayMicroseconds (velocidadeRotacao);
  }
}