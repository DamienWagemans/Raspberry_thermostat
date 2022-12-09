import threading
import time
import requests

class enabler_temp(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.window = window

    def check_if_heat_is_needed(self):
        actual_temp = self.window.Label_temp_local.cget("text").replace(' °C', '')
        set_temp = self.window.Label_temp_set.cget("text").replace(' °C', '')
        print('Actual temp :' + (actual_temp))
        print('Set temp : ' + (set_temp))

        if float(actual_temp) < float(set_temp) :
            self.window.heat_needed = 1
            # self.window.Label_status_chauffe.configure(foreground="#00ff40", text="ON")
        else:
            self.window.heat_needed = 0
            # self.window.Label_status_chauffe.configure(foreground="#ff0000", text="OFF")

    def check_if_heat_needed_and_api(self):
        if (self.window.heat_needed == 1) & (self.window.connectivity == 1) & (self.window.heat_current_status == 0):
            try:
                print('Enable heat!')
                response = requests.post("http://192.168.0.4/ON", timeout=10)
                print('Dans enabling heat : Request done')
                if response.status_code == 200:
                    self.window.heat_current_status = 1
                    self.window.Label_status_chauffe.configure(foreground="#00ff40", text="ON")

            except:
                print('Dans enabling heat : Request error')


        else :
            if (self.window.heat_needed == 0) & (self.window.connectivity == 1) & (self.window.heat_current_status == 1):
                try:
                    print('Disabling heat!')
                    response = requests.post("http://192.168.0.4/OFF", timeout=10)
                    print('Dans disabling heat : Request done')
                    if response.status_code == 200:
                        self.window.heat_current_status = 0
                        self.window.Label_status_chauffe.configure(foreground="#ff0000", text="OFF")

                except:
                    print('Dans disabling heat : Request error')

    def run(self):
        while self.window.connectivity == 0 :
            time.sleep(1)

        print('Disabling heat!')
        response = requests.post("http://192.168.0.4/OFF", timeout=10)
        print('Dans disabling heat : Request done')
        if response.status_code == 200:
            self.window.heat_current_status = 0
            self.window.Label_status_chauffe.configure(foreground="#ff0000", text="OFF")

        while (1):
            self.check_if_heat_is_needed()
            self.check_if_heat_needed_and_api()
            time.sleep(1)

