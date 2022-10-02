import threading
import time
from Utilities import temper


class date(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.window = window


    def run(self):
        while (1):
            temp = temper.Temper()
            resp = temp.read()

            int_temp = resp[0]['internal temperature']

            self.window.Label_temp_local.configure(text=str(int_temp))

            time.sleep(5)




