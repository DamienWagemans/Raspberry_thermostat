import threading
import time
from Utilities import temper
import math

class temp(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.window = window


    def run(self):
        while(1):
            try:
                temp = temper.Temper()
                while (1):
                    resp = temp.read()
                    int_temp = resp[0]['internal temperature']
                    int_temp = round(int_temp,1)
                    int_temp = int_temp - 4
                    self.window.Label_temp_local.configure(text=str(int_temp) + " °C")
                    self.window.check_if_heat_is_needed()
                    self.window.check_if_heat_needed_and_api()
                    time.sleep(1)
            except:
                print("error with temp sensor")
                time.sleep(5)