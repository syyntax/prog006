#####################################################
#                                                   #
#                       PROG 30                     #
#               Written by Jason Scott              #
#               jason.scott@mcpa-stl.org            #
#                                                   #
#                 Cyber Patriot 2016                #
#                                                   #
#              Composed in Python 2.7.12            #
#                   PEP 8 Compliant                 #
#                                                   #
#####################################################

# IMPORTS
import Tkinter as tk
import socket
import getpass as gp
import binascii as ba
import hashlib as ha

# VARIABLES
prgmWidth = 550
prgmHeight = 480
states = ['normal', 'white', 'black', 'red', 'yellow', 'blue', 'enabled', 'true', 'false', 'disabled', 'on', 'off']


def chkit(my_string):
    m = ha.md5()
    m.update(my_string)
    return m.hexdigest()


# CLASSES
class prgm(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.lbl_code = None
        self.tb_code = tk.Entry(self.step_one, width=50)
        self.tb_code.grid(row=0, column=1, columnspan=3, pady=5, sticky='WE')
        self.tb_code.configure(state="{}".format(states[9]))
        self.code_val = None
        self.main_text = None
        self.sub_text = None
        self.lower_text = None
        self.detail_text = None
        self.header = None
        self.btn_ok = None
        self.step_one = None
        self.frame_header = None

    def initialize(self):
        self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(file='img/icoMCPA.gif'))
        self.grid()
        self.step_one = tk.LabelFrame(self, text="", bg='#FFFFFF', width=500, relief="flat")
        self.step_one.grid(row=0, columnspan=7, sticky='W', padx=20, pady=5, ipadx=5, ipady=5)
        self.lbl_code = tk.Label(self.step_one, text="Flag:", justify="left", bg='#FFFFFF')
        self.lbl_code.grid(row=0, column=0, sticky='E', padx=5, pady=5)
        self.step_one.place(x=45, y=325)
        self.btn_ok = tk.Button(self.step_one, text='Submit', command=self.submit, width=20, bg='#003399', fg='#FFFFFF')
        self.btn_ok.grid(row=4, column=2, sticky='W', padx=5, pady=2)

    def submit(self):
        self.code_val = self.tb_code.get()
        if self.tb_code.get() == "":
            print("ERROR")

        else:
            print("FLAG: {}".format(chkit(self.code_val)))

        if self.code_val == "":
            win2 = tk.Tk()
            win2.withdraw()

    def draw_header(self):
        self.grid()
        self.frame_header = tk.LabelFrame(self, bg='#FFFFFF', relief="flat")
        self.frame_header.grid(row=0, columnspan=1, sticky='E')
        self.header = tk.Label(self.frame_header, image=img_header, bg='#FFFFFF')
        self.header.grid(row=0, column=0, sticky='E')
        self.frame_header.place(x=50, y=40)
        self.main_text = tk.Label(self,
                                  text="FLAG GENERATOR",
                                  justify='center',
                                  fg='#003399',
                                  font=('Helvetica', 20),
                                  bg='#FFFFFF')
        self.main_text.place(x=210, y=80)
        self.sub_text = tk.Label(self,
                                 text="Just plug in a string and get a flag!",
                                 justify='left',
                                 font=('Helvetica', 10),
                                 bg='#FFFFFF')
        self.sub_text.place(x=210, y=110)

    def draw_text(self):
        self.lower_text = tk.Label(self,
                                   text="{}".format(
                                       '''To generate a flag, simply enter a string into the box below. The flag
will return inside an IDE, and not in this window.  Try it out!'''
                                   ),
                                   justify='left',
                                   bg='#FFFFFF',
                                   fg='#000000'
                                   )
        self.lower_text.place(x=50, y=200)
        self.detail_text = tk.Label(self,
                                    justify='left',
                                    text="USER:\t{}@{}\nIP ADDR:\t{}\nTITLE:\t{}".format(
                                        gp.getuser(),
                                        socket.gethostname(),
                                        socket.gethostbyname(socket.gethostname()),
                                        ba.unhexlify('43796265722050617472696f74')
                                    ), bg='#FFFFFF')
        self.detail_text.place(x=50, y=245)


# FUNCTIONS


# MAINLOOP
if __name__ == '__main__':
    app = prgm(None)
    app.title('Flag Generator')
    app.configure(background='#FFFFFF')
    app.resizable(width=False, height=False)
    app.geometry('%dx%d+%d+%d' % (
        prgmWidth,
        prgmHeight,
        (app.winfo_screenwidth() / 2) - (prgmWidth / 2),
        (app.winfo_screenheight() / 2) - (prgmHeight / 2)))
    img_header = tk.PhotoImage(file='img/logoMCPA.png')
    app.draw_header()
    app.draw_text()
    app.mainloop()

