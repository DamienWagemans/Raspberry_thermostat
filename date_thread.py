import threading
import time
from datetime import datetime


class date(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.window = window


    def run(self):
        while (1):
            today = datetime.today().strftime('%d-%m-%Y')
            self.window.Label_date.configure(text=today)
            time.sleep(60)




