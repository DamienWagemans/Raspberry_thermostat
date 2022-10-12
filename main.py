import thermostat
import tkinter as tk
from thread import check_connectivity_thread, clock_thread, date_thread, temp_thread, enabler_temp_thread
import logging
from Utilities import logger
import sys


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()

    root.protocol('WM_DELETE_WINDOW', root.destroy)
    global _top1,_w1
    _top1 = root
    _w1 = thermostat.app_damien(_top1)

    root.attributes('-fullscreen', True)

    clock = clock_thread.clock(_w1)
    date = date_thread.date(_w1)
    temp = temp_thread.temp(_w1)
    check_connectivity = check_connectivity_thread.check_connectivity(_w1)
    enabler_temp = enabler_temp_thread.enabler_temp(_w1)

    clock.start()
    date.start()
    check_connectivity.start()
    temp.start()
    enabler_temp.start()

    _w1.init()

    root.mainloop()

    stdout_logger = logging.getLogger('STDOUT')
    sl = logger.StreamToLogger(stdout_logger, logging.INFO)
    sys.stdout = sl

    stderr_logger = logging.getLogger('STDERR')
    sl = logger.StreamToLogger(stderr_logger, logging.ERROR)
    sys.stderr = sl

if __name__ == '__main__':
    main()