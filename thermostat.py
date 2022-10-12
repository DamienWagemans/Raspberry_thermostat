import sys
import tkinter as tk
import tkinter.ttk as ttk
import os.path
import requests



_script = sys.argv[0]
_location = os.path.dirname(_script)


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

        self.heat_needed = 0
        self.connectivity = 0
        self.heat_current_status = 0

        top.geometry("440x320+459+206")
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
        self.Button_temp_up.place(relx=0.795, rely=0.281, height=74, width=77)
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
        self.Button_temp_up.bind('<Button-1>', lambda e:self.button_up(e))

        self.Button_temp_down = tk.Button(self.top)
        self.Button_temp_down.place(relx=0.795, rely=0.688, height=74, width=77)
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
        self.Button_temp_down.bind('<Button-1>', lambda e:self.button_down(e))

        _style_code()
        self.TSeparator1 = ttk.Separator(self.top)
        self.TSeparator1.place(relx=0.02, rely=0.156,  relwidth=0.98)

        self.Label_time = tk.Label(self.top)
        self.Label_time.place(relx=0.727, rely=0.063, height=21, width=107)
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
        self.Label_date.place(relx=0.318, rely=0.063, height=21, width=161)
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
        self.TSeparator2.place(relx=0.259, rely=0.028,  relheight=0.938)
        self.TSeparator2.configure(orient="vertical")

        self.Label_info = tk.Label(self.top)
        self.Label_info.place(relx=0.291, rely=0.219, height=21, width=209)
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
        self.Label_info_1.place(relx=0.291, rely=0.656, height=21, width=219)
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
        self.Label_temp_local.place(relx=0.318, rely=0.281, height=71, width=196)

        self.Label_temp_local.configure(activebackground="#f9f9f9")
        self.Label_temp_local.configure(anchor='w')
        self.Label_temp_local.configure(background="#2c3945")
        self.Label_temp_local.configure(compound='left')
        self.Label_temp_local.configure(disabledforeground="#a3a3a3")
        self.Label_temp_local.configure(font="-family {Calibri} -size 32 -weight bold")
        self.Label_temp_local.configure(foreground="#d6dae2")
        self.Label_temp_local.configure(highlightbackground="#d9d9d9")
        self.Label_temp_local.configure(highlightcolor="black")
        self.Label_temp_local.configure(text='''25.3 °C''')

        self.Label_temp_set = tk.Label(self.top)
        self.Label_temp_set.place(relx=0.314, rely=0.719, height=71, width=196)
        self.Label_temp_set.configure(activebackground="#f9f9f9")
        self.Label_temp_set.configure(anchor='w')
        self.Label_temp_set.configure(background="#2c3945")
        self.Label_temp_set.configure(compound='left')
        self.Label_temp_set.configure(disabledforeground="#a3a3a3")
        self.Label_temp_set.configure(font="-family {Calibri} -size 32 -weight bold")
        self.Label_temp_set.configure(foreground="#d6dae2")
        self.Label_temp_set.configure(highlightbackground="#d9d9d9")
        self.Label_temp_set.configure(highlightcolor="black")
        self.Label_temp_set.configure(text='''25 °C''')

        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.359, rely=0.584,  relwidth=0.257)

        self.Label_info_2_1 = tk.Label(self.top)
        self.Label_info_2_1.place(relx=0.023, rely=0.219, height=31, width=96)
        self.Label_info_2_1.configure(activebackground="#f9f9f9")
        self.Label_info_2_1.configure(anchor='w')
        self.Label_info_2_1.configure(background="#2c3945")
        self.Label_info_2_1.configure(compound='left')
        self.Label_info_2_1.configure(disabledforeground="#a3a3a3")
        self.Label_info_2_1.configure(font="-family {Calibri} -size 12 -weight bold")
        self.Label_info_2_1.configure(foreground="#d6dae2")
        self.Label_info_2_1.configure(highlightbackground="#d9d9d9")
        self.Label_info_2_1.configure(highlightcolor="black")
        self.Label_info_2_1.configure(text='''Chaudière''')

        self.Label_status_chaudiere = tk.Label(self.top)
        self.Label_status_chaudiere.place(relx=0.045, rely=0.313, height=31
                , width=59)
        self.Label_status_chaudiere.configure(activebackground="#f9f9f9")
        self.Label_status_chaudiere.configure(anchor='w')
        self.Label_status_chaudiere.configure(background="#2c3945")
        self.Label_status_chaudiere.configure(compound='left')
        self.Label_status_chaudiere.configure(disabledforeground="#a3a3a3")
        self.Label_status_chaudiere.configure(font="-family {Calibri} -size 16 -weight bold")
        self.Label_status_chaudiere.configure(foreground="#ff0000")
        self.Label_status_chaudiere.configure(highlightbackground="#d9d9d9")
        self.Label_status_chaudiere.configure(highlightcolor="black")
        self.Label_status_chaudiere.configure(text='''NOK''')


        self.TSeparator4 = ttk.Separator(self.top)
        self.TSeparator4.place(relx=0.059, rely=0.584,  relwidth=0.168)

        self.Label_status_chauffe = tk.Label(self.top)
        self.Label_status_chauffe.place(relx=0.045, rely=0.781, height=31
                , width=46)
        self.Label_status_chauffe.configure(activebackground="#f9f9f9")
        self.Label_status_chauffe.configure(anchor='w')
        self.Label_status_chauffe.configure(background="#2c3945")
        self.Label_status_chauffe.configure(compound='left')
        self.Label_status_chauffe.configure(cursor="fleur")
        self.Label_status_chauffe.configure(disabledforeground="#a3a3a3")
        self.Label_status_chauffe.configure(font="-family {Calibri} -size 16 -weight bold")
        self.Label_status_chauffe.configure(foreground="#00ff40")
        self.Label_status_chauffe.configure(highlightbackground="#d9d9d9")
        self.Label_status_chauffe.configure(highlightcolor="black")
        self.Label_status_chauffe.configure(text='''ON''')

        self.Label_info_2_1_1 = tk.Label(self.top)
        self.Label_info_2_1_1.place(relx=0.023, rely=0.688, height=31, width=95)
        self.Label_info_2_1_1.configure(activebackground="#f9f9f9")
        self.Label_info_2_1_1.configure(anchor='w')
        self.Label_info_2_1_1.configure(background="#2c3945")
        self.Label_info_2_1_1.configure(compound='left')
        self.Label_info_2_1_1.configure(disabledforeground="#a3a3a3")
        self.Label_info_2_1_1.configure(font="-family {Calibri} -size 12 -weight bold")
        self.Label_info_2_1_1.configure(foreground="#d6dae2")
        self.Label_info_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Label_info_2_1_1.configure(highlightcolor="black")
        self.Label_info_2_1_1.configure(text='''Chauffage''')

    def button_down(self, *args):
        print('Button down')
        temp = self.Label_temp_set.cget("text")
        temp = str(temp).replace(' °C', '')
        temp = float(temp)
        temp = temp - 1
        temp = str(temp) + " °C"
        self.Label_temp_set.configure(text=temp)

    def button_up(self, *args):
        print('Button UP')
        temp = self.Label_temp_set.cget("text")
        temp = str(temp).replace(' °C', '')
        temp = float(temp)
        temp = temp + 1
        temp = str(temp) + " °C"
        self.Label_temp_set.configure(text=temp)






    def init(self):
        pass





