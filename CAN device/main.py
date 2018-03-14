import pyb
import micropython
   
micropython.alloc_emergency_exception_buf(128)
   
can = pyb.CAN(1, pyb.CAN.NORMAL, prescaler=4, sjw=1, bs1=14, bs2=6)    # 500k baud
can.setfilter(0, pyb.CAN.LIST16, 0, (133, 134, 135, 136))

trig = 0

def tick1(timer):                # we will receive the timer object when being called
    global trig
    #print(trig)      # show current timer's counter value
    trig += 1
    #can.send(b'Message 1', 123)

if __name__ == "__main__":
    tim1 = pyb.Timer(10, freq=10)      # create a timer object using timer 10 - trigger at 1Hz
    tim1.callback(tick1)

    # Note: Timer(2) and Timer(3) are used for PWM to set the intensity of LED(3) and LED(4) respectively. 
    # But these timers are only configured for PWM if the intensity of the relevant LED 
    # is set to a value between 1 and 254. If the intensity feature of the LEDs is not used then 
    # these timers are free for general purpose use. Similarly, Timer(5) controls the servo driver, 
    # and Timer(6) is used for timed ADC/DAC reading/writing. 
    # It is recommended to use the other timers in your programs.
    trig_old = 0
    while(True):
        if trig != trig_old:
            if trig%10 == 0:
                can.send(b'Messa1', 153)
            if trig%20 == 0:
                can.send(b'Messa2', 154)
            if trig%30 == 0:
                can.send(b'Messa3', 155)
            if trig%40 == 0:
                can.send(b'Messa4', 156)
            trig_old = trig

        
        
        
        
        