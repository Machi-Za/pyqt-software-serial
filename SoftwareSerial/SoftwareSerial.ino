String b;

void setup()
{
  Serial.begin(9600);
}

void loop()
{ 
    
  while( Serial.available())
  {  
    b = Serial.readString();
    Serial.print("Arduino: ");
    Serial.println(b);    
  }
}
