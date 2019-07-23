import threading
import time
class ThreadExample(threading.Thread):
    def run(self):
        for i in range(1,11):
            time.sleep(1)  #waiting state
            print(i)



            
t=ThreadExample()  #init state
t.start()  #running state
t.join()
t1=ThreadExample()  #init state
t1.start()  #running state

