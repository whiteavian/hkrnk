from threading import (
    BoundedSemaphore,
    Condition,
    Event,
    Lock,
    RLock,
    Semaphore,
    Thread,
)


lock = Lock()
g = 0


def add_one():
    global g
    lock.acquire()
    print "Adding 1"
    g += 1
    lock.release()


def add_two():
    global g
    lock.acquire()
    print "Adding 2"
    g += 2
    lock.release()


threads = []

for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

for thread in threads:
    thread.join()

print g

def test_lock():
    lock = Lock()
    pass