#include <DHT.h>
#define DHTPIN 2     // Pin onde o sensor DHT está conectado
#define DHTTYPE DHT11   // Tipo do sensor DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float t = dht.readTemperature();

  // Verifica se a leitura falhou e tenta novamente
  if (  isnan(t)) {
    Serial.println("Falha ao ler do sensor DHT!");
    return;
  }

  // Envia os dados pela serial
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.print(" °C");

  delay(5000); //  Espera 2 hora (7200000 ms) antes da próxima leitura
}