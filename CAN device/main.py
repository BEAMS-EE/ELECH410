import pyb
import micropython
import schedule
import utime
   
micropython.alloc_emergency_exception_buf(128)
   
can = pyb.CAN(1, pyb.CAN.NORMAL, prescaler=4, sjw=1, bs1=14, bs2=6)    # 500k baud
can.setfilter(0, pyb.CAN.LIST16, 0, (133, 134, 135, 136))


if __name__ == "__main__":
    
    scheduler = schedule.Scheduler()
    scheduler.add_job(1000, lambda :can.send(b'The', 153))
    scheduler.add_job(2000, lambda :can.send(b'cake', 154))
    scheduler.add_job(3000, lambda :can.send(b'is a', 155))
    scheduler.add_job(4000, lambda :can.send(b'lie', 156))
        
    while(True):
        utime.sleep(0.01)
        scheduler.run_pending()
