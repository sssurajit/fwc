
#include<Arduino.h>
#include<Wire.h>
int W,A,B,C,D;
void setup()
{
        pinMode(8,INPUT);
        pinMode(9,INPUT);
        pinMode(10,INPUT);
        pinMode(11,INPUT);
	pinMode(13,OUTPUT);
}
void loop()
{
        A=digitalRead(8);
        B=digitalRead(9);
        C=digitalRead(10);
        D=digitalRead(11);
	W=((A && !D )||(A && C)||(!B && C));
	
	digitalWrite(13,W);
}

