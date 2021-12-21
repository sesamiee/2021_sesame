#include <wiringPi.h>
#define LED_R 13 //9
#define LED_Y 12 //10
#define LED_G 14 //11

int main (void)
{
  wiringPiSetup () ;
  pinMode (LED_R, OUTPUT) ;
  pinMode (LED_Y, OUTPUT) ;
  pinMode (LED_G, OUTPUT) ;
 
  
digitalWrite (LED_R, HIGH) ; delay (2000) ;
digitalWrite (LED_R,  LOW) ; 
digitalWrite (LED_Y, HIGH) ; delay (2000) ;
digitalWrite (LED_Y,  LOW) ; 
digitalWrite (LED_G, HIGH) ; delay (2000) ;
digitalWrite (LED_G,  LOW) ; 
  
  return 0 ;
}