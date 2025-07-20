import threading
import os

def first_task():
    print("First task assigned to thread:" \
    "{}".format(threading.current_thread().name))

    print("ID of process running task 1: {}".format(os.getpid()))

def second_task():
    print("Second task assigned to thread:" \
    "{}".format(threading.current_thread().name))

    print("ID of process running task 2: {}".format(os.getpid()))

if __name__ == "__main__":
    print("ID of process running main programm: {}".format(os.getpid()))

    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=first_task, name='t1')
    t2 = threading.Thread(target=second_task, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()