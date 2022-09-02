####################################################################
#           ______________________________________
#  ________|                0xMenu                |_______
#  \       |                                      |      /
#   \      |              @0x68616469             |     /
#   /      |______________________________________|     \
#  /__________)                                (_________\
#
# A Handy Package to Create 3 Different types of Menus
#
# Github repo : https://github.com/0x68616469/oxmenu
#
####################################################################

import sys
import termios
from oxansi import Short as a

class ArrowKeyMenu:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.subtitle = kwargs.get('subtitle', '')      
        self.options = []
    
    def getch(self):
        fd = sys.stdin.fileno()
        orig = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ICANON
        new[6][termios.VMIN] = 1
        new[6][termios.VTIME] = 0
        try:
            termios.tcsetattr(fd, termios.TCSAFLUSH, new)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, orig)
            
    def add(self, name=""):
        self.options.append(name)
    
    def display(self, selected):
        if self.title != "":
            print(f"{a.bld}{a.b}- {a.w}{self.title}{a.rst} {a.c}{self.subtitle}{a.rst}")
        select = 1
        for option in self.options:
            if selected == select:
                print(f"{a.bld}{a.c}>{a.rst} {option}")
            else:
                print(f"  {option}")
            select += 1

    def select(self):
        selected = 1
        print(a.sc,end="")
        while True:
            print(a.rc,end="")
            self.display(selected)
            c=""
            try:
                c = self.getch()
            except KeyboardInterrupt:
                print(f"{a.cll}{a.b}[{a.r}!{a.b}] {a.r}Error: {a.rst}Keyboard Interrupt.")
                sys.exit(1)
            print(a.cll)
            
            if (c == "j" or c == "A") and selected != 1:
                selected -= 1
            elif (c == "k" or c == "B") and selected != len(self.options):
                selected += 1
            elif c == "\n":
                print(a.rc, end="")
                for _ in range(len(self.options)+1):
                    print(a.cll)
                print(a.rc, end="")
                return selected
            
class NumberMenu:
    def __init__(self, **kwargs): 
        self.title = kwargs.get('title', '')
        self.subtitle = kwargs.get('subtitle', '')
        self.input_message = kwargs.get('input_message', 'Choose an option :')
        self.options = []
    
    def add(self, name=""):
        self.options.append(name)
        
    def select(self):
        print(a.sc,end="")
        if self.title != "":
            print(f"{a.bld}{a.b}- {a.w}{self.title}{a.rst} {a.c}{self.subtitle}{a.rst}")
        i = 0
        for option in self.options:
            i += 1
            print(f"{a.br.b}[{a.c}{i}{a.br.b}]{a.rst} {option}")
            
        choice = input(f"\n{a.br.b}[{a.g}?{a.br.b}]{a.rst} {self.input_message}")
        try:
            choice = int(choice)
        except:
            print(f"{a.br.b}[{a.r}x{a.br.b}]{a.rst} Error: \"{choice}\" is not a number.")
            sys.exit(1)
        
        if choice > i or choice < 1:
            print(f"{a.br.b}[{a.r}x{a.br.b}]{a.rst} Error: \"{choice}\" is out of index.")
            sys.exit(1)      

        print(a.rc, end="")
        for _ in range(len(self.options)+3):
            print(a.cll)
        print(a.rc, end="")
        return choice         

class CheckBox:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.subtitle = kwargs.get('subtitle', '')  
        self.min_options = kwargs.get('min_options', 0)
        self.max_options = kwargs.get('max_optios', -1)
        self.options = []
    
    def getch(self):
        fd = sys.stdin.fileno()
        orig = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ICANON
        new[6][termios.VMIN] = 1
        new[6][termios.VTIME] = 0
        try:
            termios.tcsetattr(fd, termios.TCSAFLUSH, new)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, orig)
            
    def add(self, name=""):
        self.options.append([name, False])

    def display(self, selected):
        if self.title != "":
            print(f"{a.bld}{a.b}- {a.w}{self.title}{a.rst} {a.c}{self.subtitle}{a.rst}")
        select = 1
        for option in self.options:

            if selected == select:
                print(f"{a.bld}{a.c}>{a.rst} ",end="")
            else:
                print("  ",end="")
                
            if option[1] == True:
                print(f"{a.b}[{a.bld}{a.y}*{a.rst}{a.b}]{a.rst} ",end="")
            else:
                print(f"{a.b}[ ]{a.rst} ",end="")
            print(f"{option[0]}")

            select += 1

    def select(self):
        selected = 1
        nb_selected = 0
        print(a.sc,end="")
        while True:
            print(a.rc,end="")
            self.display(selected)
            c=""
            try:
                c = self.getch()
            except KeyboardInterrupt:
                print(f"{a.cll}{a.b}[{a.r}!{a.b}] {a.r}Error: {a.rst}Keyboard Interrupt.")
                sys.exit(1)
            print(a.cll)
            
            if (c == "j" or c == "A") and selected != 1:
                selected -= 1
            elif (c == "k" or c == "B") and selected != len(self.options):
                selected += 1
            elif c == " ":
                if self.options[selected-1][1] == True:
                    self.options[selected-1][1] = False
                    nb_selected -= 1
                else:
                    self.options[selected-1][1] = True
                    nb_selected += 1
                    
            elif c == "\n":
                if nb_selected < self.min_options:
                    print(f"{a.cll}{a.b}[{a.r}!{a.b}] {a.r}Error: {a.rst}Select at least {self.min_options} option/s.")
                elif nb_selected > self.max_options and self.max_options != -1:
                    print(f"{a.cll}{a.b}[{a.r}!{a.b}] {a.r}Error: {a.rst}Select {self.max_options} or less option/s.")
                else:
                    print(a.rc, end="")
                    for _ in range(len(self.options)+1):
                        print(a.cll)
                    print(a.rc, end="")
                    return self.options 

    
    