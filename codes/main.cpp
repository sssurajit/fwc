
#include<Arduino.h>
int W,A=0,B=0,C=1,D=0;
void setup(){
	pinMode(13,OUTPUT);
}
void loop(){
	 W=((A && !D )||(A && C)||(!B && C));
	digitalWrite(13,W);
}

