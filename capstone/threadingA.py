import multithreading
import time

def CalculateTime():
    print("sleep for 5 seconds \n")
    time.sleep(5)
    print("completed sleep\n")

t1 = threading.Thread(target=CalculateTime)
t2 = threading.Thread(target=CalculateTime)
t3 = threading.Thread(target=CalculateTime)
t4 = threading.Thread(target=CalculateTime)

t1.start()
t2.start()
t3.start()
t4.start()

