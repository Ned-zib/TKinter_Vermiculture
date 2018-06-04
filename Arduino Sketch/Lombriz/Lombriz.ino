#include "DHT.h" //cargamos la librería DHT
#define DHTPIN 2 //Seleccionamos el pin en el que se //conectará el sensor
#define DHTTYPE DHT11 //Se selecciona el DHT11 (hay //otros DHT)
DHT dht(DHTPIN, DHTTYPE); //Se inicia una variable que será usada por Arduino para comunicarse con el sensor
#include <math.h>
#include <stdio.h>
//  Datos para las ecuaciones algoritmo termistor
float Vin=5.0;       // [V]       Voltage de entrada en el divisor de tension
float Raux=10000;    // [ohm]     Valor de la resistencia del divisor de tension
float Rntc=10000;   // [ohm]     Valor de resistencia del termistor (NTC) a 25ºC
float T0=298.15;     // [K] (25ºC)
 
float Vout=0.0;      // [V]        Voltage given by the Voltage-Divider
float Rout=0.0;      // [ohm]      Resistencia actual del Termistor (NTC)

float Beta=0.0;      // [K]        Parametro Beta
float Rinf=0.0;      // [ohm]      Parametros Rinf
float TempK=0.0;     // [K]        Temperatura de salida en grados Kelvin
float TempC=0.0;     // [ºC]       Temperatura de salida en grados Celsius
int duty; 
int iCont;            // Contador de ciclos, para calculo de temperatura media
float cTemp1;         // Variable temporal para acumular las temperaturas leidas
int V;
int R;
int B;
void setup() {
 Serial.begin(9600); //Se inicia la comunicación serial 
 dht.begin(); //Se inicia el sensor 
 // Configuramos el pin del Arduino en entrada
 pinMode(A0, INPUT);
 pinMode(13, OUTPUT);
 pinMode(4, OUTPUT);
 pinMode(5, OUTPUT);
 // Parametros de calculo
 Beta = 4038.0;
 Rinf=Rntc*exp(-Beta/T0);
 digitalWrite(4,LOW);
 digitalWrite(5,LOW);
 duty=0;
 }
 
void loop() {
float h = dht.readHumidity(); //Se lee la humedad
double TempC;
double temp = Termistor(analogRead(A1));  // Read sensor
TempC=temp;


if(temp<=28.0){
  digitalWrite(4,HIGH); R=1;}
else{digitalWrite(4,LOW); R=0;}

if(temp>32.0){
  analogWrite(13, 255); V=1;}
else{analogWrite(13,90); V=0;}

if(h<=75.0){
  digitalWrite(5,HIGH); B=1;}
else{digitalWrite(5,LOW); B=0;}

if(h>80.0){
  analogWrite(13, 255); V=2; digitalWrite(4,HIGH); R=1;}

Serial.print("D");
Serial.print(TempC,1);
Serial.print(h,1);
Serial.print(R);
Serial.print(V);
Serial.println(B);
delay(100);




}

double Termistor(int RawADC) {
    // Cálculo del valor de la resistencia termistor (NTC) a través de Vout
    Vout=Vin*((float)(RawADC)/1024.0);
    Rout=(Raux*Vout/(Vin-Vout));
    // Calculo de la temperatura en grados Kelvin
    TempK=(Beta/log(Rout/Rinf));
    // Calculo de la temperatura en grados Celsius
    TempC=TempK-273.15;
    // Almacenamos la temperatura (Celsius) actual para después obtener la media
    cTemp1 = cTemp1 + TempC;
    // Hacemos una pausa de 10 milisegundos   
    delay(10);
    return TempC;
    }
