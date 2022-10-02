import tkinter as tk
import thermostat

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = thermostat.app_damien(_top1)
    root.mainloop()

if __name__ == '__main__':
    thermostat.start_up()




