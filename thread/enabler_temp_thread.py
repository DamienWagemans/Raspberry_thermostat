import threading
import time
import requests

class enabler_temp(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.window = window

    def check_if_heat_is_needed(self):
        actual_temp = self.Label_temp_local.cget("text").replace(' °C', '')
        set_temp = self.Label_temp_set.cget("text").replace(' °C', '')
        print('Actual temp :' + (actual_temp))
        print('Set temp : ' + (set_temp))

        if float(actual_temp) < float(set_temp) :
            self.heat_needed = 1
        else:
            self.heat_needed = 0

    def check_if_heat_needed_and_api(self):
        if (self.heat_needed == 1) & (self.connectivity == 1) & (self.heat_current_status == 0):
            try:
                print('Enable heat!')
                response = requests.post("http://192.168.0.29:5000/api/v1/power/on", timeout=10)
                print('Dans enabling heat : Request done')
                if response.status_code == 200:
                    self.heat_current_status = 1
                    self.Label_status_chauffe.configure(foreground="#00ff40", text="ON")

            except:
                print('Dans enabling heat : Request error')


        else :
            if (self.heat_needed == 0) & (self.connectivity == 1) & (self.heat_current_status == 1):
                try:
                    print('Disabling heat!')
                    response = requests.post("http://192.168.0.29:5000/api/v1/power/off", timeout=10)
                    print('Dans disabling heat : Request done')
                    if response.status_code == 200:
                        self.heat_current_status = 0
                        self.Label_status_chauffe.configure(foreground="#ff0000", text="OFF")

                except:
                    print('Dans disabling heat : Request error')

    def run(self):
        try:
            time.sleep(1)
            if self.window.connectivity == 1:
                print('Disabling heat!')
                response = requests.post("http://192.168.0.29:5000/api/v1/power/off", timeout=10)
                print('Dans disabling heat : Request done')
                if response.status_code == 200:
                    self.heat_current_status = 0
        except:
            print('Erreur lors de la desactivation initiale de la chaudiere')
            self.heat_current_status == 0



        while (1):
            self.check_if_heat_is_needed()
            self.check_if_heat_needed_and_api()
            time.sleep(1)

