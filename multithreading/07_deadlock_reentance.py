import threading

lock_obj = threading.RLock()

print('Acquire 1st time')
lock_obj.acquire()

print('Acquire 2nd time')
lock_obj.acquire()

print('Releasing')
lock_obj.release()


# def reentrance():
#     print('start')
#     lock_obj.acquire()
#     print('Acquired')
#     reentrance()
#
# reentrance()
