#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Sep 27, 2022 03:52:24 PM CEST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import test_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1

class app_damien:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("480x320+137+198")
        top.minsize(120, 1)
        top.maxsize(1698, 984)
        top.resizable(1,  1)
        top.title("Thermostat par Damien Wagemans")
        top.configure(relief="raised")
        top.configure(background="#2d3844")
        top.configure(highlightbackground="#d6dae2")
        top.configure(highlightcolor="#d6dae2")
        top.configure(highlightthickness="8")

        self.top = top

        self.Button_temp_up = tk.Button(self.top)
        self.Button_temp_up.place(relx=0.771, rely=0.281, height=84, width=87)
        self.Button_temp_up.configure(activebackground="#4f6080")
        self.Button_temp_up.configure(activeforeground="#d6dae2")
        self.Button_temp_up.configure(background="#2c3945")
        self.Button_temp_up.configure(borderwidth="1")
        self.Button_temp_up.configure(compound='left')
        self.Button_temp_up.configure(cursor="arrow")
        self.Button_temp_up.configure(disabledforeground="#4f6080")
        self.Button_temp_up.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Button_temp_up.configure(foreground="#d6dae2")
        self.Button_temp_up.configure(highlightbackground="#d6dae2")
        self.Button_temp_up.configure(highlightcolor="#d6dae2")
        self.Button_temp_up.configure(highlightthickness="10")
        self.Button_temp_up.configure(overrelief="flat")
        self.Button_temp_up.configure(pady="0")
        self.Button_temp_up.configure(relief="solid")
        self.Button_temp_up.configure(text='''+''')

        self.Button_temp_down = tk.Button(self.top)
        self.Button_temp_down.place(relx=0.771, rely=0.594, height=84, width=87)
        self.Button_temp_down.configure(activebackground="#4f6080")
        self.Button_temp_down.configure(activeforeground="#d6dae2")
        self.Button_temp_down.configure(background="#2c3945")
        self.Button_temp_down.configure(borderwidth="1")
        self.Button_temp_down.configure(compound='left')
        self.Button_temp_down.configure(cursor="arrow")
        self.Button_temp_down.configure(disabledforeground="#4f6080")
        self.Button_temp_down.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Button_temp_down.configure(foreground="#d6dae2")
        self.Button_temp_down.configure(highlightbackground="#d6dae2")
        self.Button_temp_down.configure(highlightcolor="#d6dae2")
        self.Button_temp_down.configure(highlightthickness="10")
        self.Button_temp_down.configure(overrelief="flat")
        self.Button_temp_down.configure(pady="0")
        self.Button_temp_down.configure(relief="solid")
        self.Button_temp_down.configure(text='''-''')

        _style_code()
        self.TSeparator1 = ttk.Separator(self.top)
        self.TSeparator1.place(relx=0.021, rely=0.156,  relwidth=0.979)

        self.Label_time = tk.Label(self.top)
        self.Label_time.place(relx=0.792, rely=0.063, height=21, width=84)
        self.Label_time.configure(activebackground="#f9f9f9")
        self.Label_time.configure(anchor='w')
        self.Label_time.configure(background="#2c3945")
        self.Label_time.configure(compound='left')
        self.Label_time.configure(disabledforeground="#a3a3a3")
        self.Label_time.configure(font="-family {Calibri} -size 16 -weight bold")
        self.Label_time.configure(foreground="#d6dae2")
        self.Label_time.configure(highlightbackground="#d9d9d9")
        self.Label_time.configure(highlightcolor="black")
        self.Label_time.configure(text='''10:00:34''')

        self.Label_date = tk.Label(self.top)
        self.Label_date.place(relx=0.333, rely=0.063, height=21, width=154)
        self.Label_date.configure(activebackground="#f9f9f9")
        self.Label_date.configure(anchor='w')
        self.Label_date.configure(background="#2c3945")
        self.Label_date.configure(compound='left')
        self.Label_date.configure(disabledforeground="#a3a3a3")
        self.Label_date.configure(font="-family {Calibri} -size 16 -weight bold")
        self.Label_date.configure(foreground="#d6dae2")
        self.Label_date.configure(highlightbackground="#d9d9d9")
        self.Label_date.configure(highlightcolor="black")
        self.Label_date.configure(text='''27 - Sept - 2022''')

        self.TSeparator2 = ttk.Separator(self.top)
        self.TSeparator2.place(relx=0.258, rely=0.028,  relheight=0.938)
        self.TSeparator2.configure(orient="vertical")

        self.Label_info = tk.Label(self.top)
        self.Label_info.place(relx=0.292, rely=0.219, height=21, width=184)
        self.Label_info.configure(activebackground="#f9f9f9")
        self.Label_info.configure(anchor='w')
        self.Label_info.configure(background="#2c3945")
        self.Label_info.configure(compound='left')
        self.Label_info.configure(disabledforeground="#a3a3a3")
        self.Label_info.configure(font="-family {Calibri} -size 12 -weight bold")
        self.Label_info.configure(foreground="#d6dae2")
        self.Label_info.configure(highlightbackground="#d9d9d9")
        self.Label_info.configure(highlightcolor="black")
        self.Label_info.configure(text='''Température ambiante :''')

        self.Label_info_1 = tk.Label(self.top)
        self.Label_info_1.place(relx=0.292, rely=0.656, height=21, width=184)
        self.Label_info_1.configure(activebackground="#f9f9f9")
        self.Label_info_1.configure(anchor='w')
        self.Label_info_1.configure(background="#2c3945")
        self.Label_info_1.configure(compound='left')
        self.Label_info_1.configure(disabledforeground="#a3a3a3")
        self.Label_info_1.configure(font="-family {Calibri} -size 12 -weight bold")
        self.Label_info_1.configure(foreground="#d6dae2")
        self.Label_info_1.configure(highlightbackground="#d9d9d9")
        self.Label_info_1.configure(highlightcolor="black")
        self.Label_info_1.configure(text='''Température souhaitée :''')

        self.Label_temp_local = tk.Label(self.top)
        self.Label_temp_local.place(relx=0.313, rely=0.281, height=71, width=214)

        self.Label_temp_local.configure(activebackground="#f9f9f9")
        self.Label_temp_local.configure(anchor='w')
        self.Label_temp_local.configure(background="#2c3945")
        self.Label_temp_local.configure(compound='left')
        self.Label_temp_local.configure(disabledforeground="#a3a3a3")
        self.Label_temp_local.configure(font="-family {Calibri} -size 48 -weight bold")
        self.Label_temp_local.configure(foreground="#d6dae2")
        self.Label_temp_local.configure(highlightbackground="#d9d9d9")
        self.Label_temp_local.configure(highlightcolor="black")
        self.Label_temp_local.configure(text='''25.3 °C''')

        self.Label_temp_set = tk.Label(self.top)
        self.Label_temp_set.place(relx=0.313, rely=0.719, height=71, width=214)
        self.Label_temp_set.configure(activebackground="#f9f9f9")
        self.Label_temp_set.configure(anchor='w')
        self.Label_temp_set.configure(background="#2c3945")
        self.Label_temp_set.configure(compound='left')
        self.Label_temp_set.configure(disabledforeground="#a3a3a3")
        self.Label_temp_set.configure(font="-family {Calibri} -size 48 -weight bold")
        self.Label_temp_set.configure(foreground="#d6dae2")
        self.Label_temp_set.configure(highlightbackground="#d9d9d9")
        self.Label_temp_set.configure(highlightcolor="black")
        self.Label_temp_set.configure(text='''25.3 °C''')

        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.358, rely=0.584,  relwidth=0.258)

        self.Label_info_2 = tk.Label(self.top)
        self.Label_info_2.place(relx=0.042, rely=0.188, height=21, width=84)
        self.Label_info_2.configure(activebackground="#f9f9f9")
        self.Label_info_2.configure(anchor='w')
        self.Label_info_2.configure(background="#2c3945")
        self.Label_info_2.configure(compound='left')
        self.Label_info_2.configure(disabledforeground="#a3a3a3")
        self.Label_info_2.configure(font="-family {Calibri} -size 12 -weight bold")
        self.Label_info_2.configure(foreground="#d6dae2")
        self.Label_info_2.configure(highlightbackground="#d9d9d9")
        self.Label_info_2.configure(highlightcolor="black")
        self.Label_info_2.configure(text='''Connection''')

        self.Label_info_2_1 = tk.Label(self.top)
        self.Label_info_2_1.place(relx=0.052, rely=0.25, height=31, width=94)
        self.Label_info_2_1.configure(activebackground="#f9f9f9")
        self.Label_info_2_1.configure(anchor='w')
        self.Label_info_2_1.configure(background="#2c3945")
        self.Label_info_2_1.configure(compound='left')
        self.Label_info_2_1.configure(disabledforeground="#a3a3a3")
        self.Label_info_2_1.configure(font="-family {Calibri} -size 12 -weight bold")
        self.Label_info_2_1.configure(foreground="#d6dae2")
        self.Label_info_2_1.configure(highlightbackground="#d9d9d9")
        self.Label_info_2_1.configure(highlightcolor="black")
        self.Label_info_2_1.configure(text='''chaudière''')

        self.Label_status_chaudiere = tk.Label(self.top)
        self.Label_status_chaudiere.place(relx=0.083, rely=0.344, height=31
                , width=64)
        self.Label_status_chaudiere.configure(activebackground="#f9f9f9")
        self.Label_status_chaudiere.configure(anchor='w')
        self.Label_status_chaudiere.configure(background="#2c3945")
        self.Label_status_chaudiere.configure(compound='left')
        self.Label_status_chaudiere.configure(disabledforeground="#a3a3a3")
        self.Label_status_chaudiere.configure(font="-family {Calibri} -size 18 -weight bold")
        self.Label_status_chaudiere.configure(foreground="#00ff40")
        self.Label_status_chaudiere.configure(highlightbackground="#d9d9d9")
        self.Label_status_chaudiere.configure(highlightcolor="black")
        self.Label_status_chaudiere.configure(text='''OK''')

        self.TSeparator4 = ttk.Separator(self.top)
        self.TSeparator4.place(relx=0.06, rely=0.584,  relwidth=0.167)

        self.Label_status_chauffe_1 = tk.Label(self.top)
        self.Label_status_chauffe_1.place(relx=0.042, rely=0.688, height=31
                , width=104)
        self.Label_status_chauffe_1.configure(activebackground="#f9f9f9")
        self.Label_status_chauffe_1.configure(anchor='w')
        self.Label_status_chauffe_1.configure(background="#2c3945")
        self.Label_status_chauffe_1.configure(compound='left')
        self.Label_status_chauffe_1.configure(disabledforeground="#a3a3a3")
        self.Label_status_chauffe_1.configure(font="-family {Calibri} -size 18 -weight bold")
        self.Label_status_chauffe_1.configure(foreground="#00ff40")
        self.Label_status_chauffe_1.configure(highlightbackground="#d9d9d9")
        self.Label_status_chauffe_1.configure(highlightcolor="black")
        self.Label_status_chauffe_1.configure(text='''CHAUFFE''')

        self.Label_status_chauffe_2 = tk.Label(self.top)
        self.Label_status_chauffe_2.place(relx=0.042, rely=0.781, height=31
                , width=94)
        self.Label_status_chauffe_2.configure(activebackground="#f9f9f9")
        self.Label_status_chauffe_2.configure(anchor='w')
        self.Label_status_chauffe_2.configure(background="#2c3945")
        self.Label_status_chauffe_2.configure(compound='left')
        self.Label_status_chauffe_2.configure(disabledforeground="#a3a3a3")
        self.Label_status_chauffe_2.configure(font="-family {Calibri} -size 18 -weight bold")
        self.Label_status_chauffe_2.configure(foreground="#00ff40")
        self.Label_status_chauffe_2.configure(highlightbackground="#d9d9d9")
        self.Label_status_chauffe_2.configure(highlightcolor="black")
        self.Label_status_chauffe_2.configure(text='''ACTIVE''')

def start_up():
    test_support.main()

if __name__ == '__main__':
    test_support.main()




