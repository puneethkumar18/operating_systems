from threading import *
import time

sem = Semaphore(3)

def Task(name):
    sem.acquire()
    for i in range(5):
        print("() working ", format(name),'\n')
        time.sleep(5)
    sem.release()

def Task(name):
    sem.acquire()
    
    print("() working ", format(name),'\n')
    time.sleep(5)    
        
    sem.release()
if __name__ == "__main__":
    t1 = Thread(target=Task,args=('Thread-1',))
    t2 = Thread(target=Task,args=('Thread-2',))
    t3 = Thread(target=Task,args=('Thread-3',))
    t4 = Thread(target=Task,args=('Thread-4',))
    t5 = Thread(target=Task,args=('Thread-5',))


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    
