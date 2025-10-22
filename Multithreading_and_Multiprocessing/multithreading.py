import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
        
def print_letter():
    for letter in"abcde":
        time.sleep(2)
        print(f"Letter:{letter}")

##create 2 threads
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

t=time.time()
##start theh thread
t1.start()
t2.start()


# wait for threads to compleet
t1.join()
t2.join()
finshed_time = time.time() - t
print(finshed_time)