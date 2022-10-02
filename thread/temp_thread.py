import threading
import time
from Utilities import temper


class temp(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.window = window


    def run(self):
        temp = temper.Temper()
        while (1):
            resp = temp.read()
            int_temp = resp[0]['internal temperature']
            self.window.Label_temp_local.configure(text=str(int_temp))
            time.sleep(5)