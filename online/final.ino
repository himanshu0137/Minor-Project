const int seat_no = 2;
const char *ssid = "MotoG3 5345";
const char *passwd = "12345678";
const char *ip = "192.168.43.250";
const int port = 55056;
const int threshold = 100;

String op;
int i, a, data_size;
void setup() {
  Serial.begin(9600);
  Serial1.begin(115200);
  Serial.println("Starting ESP8266");

  Serial1.print("AT+CWJAP=\"");
  Serial1.print(ssid);
  Serial1.print("\",\"");
  Serial1.print(passwd);
  Serial1.print("\"\r\n");
  while (1) {
    if (Serial1.available()) {
      Serial.println(Serial1.read());
      break;
    }
    else {
      Serial.println("Wait1");
      delay(500);
    }
  }

  Serial1.print("AT+CWMODE=1\r\n");
  while (1) {
    if (Serial1.available()) {
      Serial.println(Serial1.read());
      break;
    }
    else {
      Serial.println("Wait2");
      delay(500);
    }
  }

  Serial1.print("AT+CIPMUX=0\r\n");
  while (1) {
    if (Serial1.available()) {
      Serial.println(Serial1.read());
      break;
    }
    else {
      Serial.println("Wait3");
      delay(500);
    }
  }

  Serial1.print("AT+CIPSTART=\"UDP\",\"");
  Serial1.print(ip);
  Serial1.print("\",");
  Serial1.print(port);
  Serial1.print("\r\n");
  while (1) {
    if (Serial1.available()) {
      Serial.println(Serial1.read());
      break;
    }
    else {
      Serial.println("Wait4");
      delay(500);
    }
  }
}
void loop() {
  op = "{\"seat_status\":[";
  for (i = 0; i < seat_no; i++) {
    a = analogRead(i);
    if (a > threshold) {
      op += "\"0\"";
      Serial.println("0");
    }
    else {
      op += "\"1\"";
      Serial.println("1");
    }
    if (i < seat_no - 1)
      op += ",";
  }
  op += "]}";
  data_size = op.length();
  Serial1.print("AT+CIPSEND=");
  Serial1.print(data_size+2);
  Serial1.print("\r\n");
  delay(1000);

  for (i = 0; i < data_size; i++)
    Serial.print(op[i]);
  Serial.println();
    
  for (i = 0; i < data_size; i++)
    Serial1.print(op[i]);
  Serial1.print("\r\n");
  while (1) {
    if (Serial1.available()) {
      break;
    }
    else {
      Serial.println("Sending");
      delay(500);
    }
  }
  
  delay(5000);
}
