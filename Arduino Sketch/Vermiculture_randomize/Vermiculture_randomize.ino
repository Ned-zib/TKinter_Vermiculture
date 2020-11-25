void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  // print a random number from 10 to 19
  float rand_temp = random(20, 31);
  float rand_humi = random(50, 65);
  int rand_heat = random(0, 2);
  int rand_fan  = random(0, 3);
  int rand_pump = random(0, 2);
  
  Serial.print("D");
  Serial.print(rand_temp*100,0);
  Serial.print(rand_humi*100,0);
  Serial.print(rand_heat);
  Serial.print(rand_fan);
  Serial.println(rand_pump);
  delay(5000);

}
