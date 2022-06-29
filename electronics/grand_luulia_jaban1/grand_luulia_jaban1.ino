// C++ code
//
#include <Servo.h>

int pressed = 0;

Servo servo_9;

void setup()
{
  pinMode(2, INPUT_PULLUP);
  servo_9.attach(9, 500, 2500);
}

void loop()
{
  pressed = digitalRead(2);
  if (pressed == 0) {
    servo_9.write(0);
  } else {
    servo_9.write(360
    );
  }
  delay(100); // Wait for 1000 millisecond(s)
}
