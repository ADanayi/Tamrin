import threading
import time

ctr = 0

class Entity:
    L = threading.Lock()
    alive = False

    def __init__(self, sleep_dur):
        self.thd = threading.Thread(target=self.worker, daemon=True)
        self.__alive = True
        self.__sleep_dur = sleep_dur

    def start(self):
        self.thd.start()

    def worker(self):
        while True:
            self.perform()

    def perform(self):
        Entity.L.acquire()
        self.do()
        Entity.L.release()
        time.sleep(self.__sleep_dur)


class Writer(Entity):

    def __init__(self, sleep_dur):
        Entity.__init__(self, sleep_dur)

    def do(self):
        global ctr
        ctr += 1
        print('Writer @{} => CTR INC: {}'.format(str(self.thd), ctr))
        # time.sleep(self.__sleep_dur)

class Reader(Entity):

    def __init__(self, sleep_dur):
        Entity.__init__(self, sleep_dur)

    def do(self):
        global ctr
        print('Reader @{} => CTR = {}'.format(str(self.thd), ctr))
        # time.sleep(self.__sleep_dur)

W = Writer(1)
R1 = Reader(0.5)
R2 = Reader(0.5)

# R1.start()

# for entity in (W, R1, R2):
#     entity.start()

W.start()
R1.start()

time.sleep(10)
