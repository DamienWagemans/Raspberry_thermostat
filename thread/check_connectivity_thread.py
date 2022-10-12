import threading
import time
import requests

class check_connectivity(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.window = window


    def run(self):
        while (1):
            try:
                print('Dans check_connectivity ')
                response = requests.get("http://192.168.0.29:5000/api/v1/status", timeout=10)
                print('Dans check_connectivity : Request done')
                if response.status_code == 200:
                    self.window.Label_status_chaudiere.configure(text='OK', foreground="#00ff40")
                    self.window.connectivity = 1
                time.sleep(15)


            except:
                print('Dans check_connectivity : Request error')
                self.window.Label_status_chaudiere.configure(text='NOK', foreground="#ff0000")
                self.window.connectivity = 0






