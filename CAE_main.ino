char relay_cmd; 

int relay1 = 3;
int relay2 = 4;
int relay3 = 5;
int relay4 = 6;

void setup() {
  Serial.begin(9600); // 시리얼 시작
  pinMode(relay1, OUTPUT); //릴레이모드 모두 출력으로 설정
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
}

void loop() {

  int relay2_bool = digitalRead(relay2);
  int relay3_bool = digitalRead(relay3);
  int relay4_bool = digitalRead(relay3);

  if(Serial.available())
  {

    relay_cmd = Serial.read();
    
    
    if(relay_cmd == 'a') //밸브 #1 ON (OPENED) , 열려있으면(led가 켜져있으면) 0 반환
    {
      digitalWrite(relay2,LOW);
      //Serial.println(relay2_bool);
    }
    else if(relay_cmd == 'b') //밸브 #1 OFF (CLOSED) , 닫혀있으면(led가 꺼져있으면) 1 반환
    {
      digitalWrite(relay2,HIGH);
      //Serial.println(relay2_bool);
    }
    else if(relay_cmd == 'c') //밸브 #2 ON (OPENED) , 열려있으면(led가 켜져있으면) 0 반환
    {
      digitalWrite(relay3,LOW);
      //Serial.println(relay3_bool);
    }
    else if(relay_cmd == 'd') //밸브 #2 OFF (CLOSED) , 닫혀있으면(led가 꺼져있으면) 1 반환
    {
      digitalWrite(relay3,HIGH);
      //Serial.println(relay3_bool);
    }
    else if(relay_cmd == 'e') //INTERVAL OPEN : 밸브 #1, #2 모두 OPEN, 펌프 정상 작동
    {
      digitalWrite(relay2,LOW);
      digitalWrite(relay3,LOW);
      //Serial.println("0");
    }
    else if(relay_cmd == 'f') //INTERVAL CLOSED : 밸브 #1, #2 모두 CLOSE, 펌프 정지
    {
      digitalWrite(relay2, HIGH);
      digitalWrite(relay3, HIGH);
      //Serial.println("1");
    }
  }

  // 각 밸브와, 구간 개폐여부 1초마다 쏴주기
  Serial.print(" Valve1:");
  Serial.print(relay2_bool);
  Serial.print(" Valve2:");
  Serial.print(relay3_bool);
  Serial.println("");
  delay(500);
  
}
