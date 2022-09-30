
#include <avr/io.h>
#include <util/delay.h>
#include <stdbool.h>

 
int main (void)
{
   bool A=1, B=1,C=0, D=1;
   bool W ;

 DDRB  = 0b00100000;
 PORTB = 0b00100000;

 //equation
 while(1)
 {       
        W=((A && !D )||(A && C)||(!B && C));
        
	PORTB &=(W<<5);
} 
  return 0;
}
