import random
import threading
import time
from enum import Enum


class BankTerminal:
    def __init__(self, port, ip_address):
        self.port = port
        self.ip_address = ip_address
        self.protocol = Protocol(self.port, self.ip_address)
        self.protocol.message_received += self.on_message_received
        self.operation_signal = threading.Event()

    def on_message_received(self, status):
        print(f'Signalling for event: {status}')
        self.operation_signal.set()

    def purchase(self, amount):
        def process_purchase():
            purchase_op_code = 1
            self.protocol.send(purchase_op_code, amount)
            self.operation_signal.clear()
            print('\nWaiting for signal')
            self.operation_signal.wait()
            print('Purchase finished')

        t = threading.Thread(target=process_purchase)
        t.start()
        return t


class Event:
    def __init__(self):
        self.__handlers = []

    def __call__(self, *args, **kwargs):
        for f in self.__handlers:
            f(*args, **kwargs)

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self


class OperationStatus(Enum):
    FINISHED = 0
    FAULTED = 1


class Protocol:
    def __init__(self, port, ip_address):
        self.port = port
        self.ip_address = ip_address
        self.message_received = Event()

    def send(self, op_code, params):
        def process_sending():
            print(f'Operation is in action with params = {params}')
            result = self.process(op_code, params)
            self.message_received(result)

        t = threading.Thread(target=process_sending)
        t.start()

    def process(self, op_code, params):
        print(f'Processing operation = {op_code} with params = {params}')
        time.sleep(3)
        finished = random.randint(0, 1) == 1
        return OperationStatus.FINISHED if finished else OperationStatus.FAULTED


if __name__ == '__main__':
    bt = BankTerminal(10, '192.168.0.1')
    t = bt.purchase(20)
    print('Main decided to wait for purchase 1')
    t.join()
    t = bt.purchase(30)
    print('Main decided to wait for purchase 2')
    t.join()
    print('End of main')
