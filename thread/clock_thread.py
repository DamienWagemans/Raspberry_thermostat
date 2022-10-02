import threading
import time
from datetime import datetime


class clock(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.window = window


    def run(self):
        while (1):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.window.Label_time.configure(text=current_time)
            time.sleep(1)