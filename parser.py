from tkinter import *
import sys
import nltk
from nltk.tree import Tree
from nltk.draw.tree import TreeView
from customtkinter import *
from PIL import Image,ImageTk

#////////////////////////////////////////////////Define Variables////////////////////////////////////////////////
sentence = ""
split = []
i = -1
lookahead = ''
#///////////////////////////////////////////////////GUI Code/////////////////////////////////////////////////////

set_appearance_mode("dark-blue")

app = CTk()
app.geometry("800x600")
app.title("Parser")
app.iconbitmap("images/helwan.ico")
app.update()
def openFile():
    global sentence
    global split
    global i
    global lookahead

    sentence = ""
    split = []
    i = -1
    lookahead = ''
    types = [("Text Files", "*.txt"), ("All Files", "*.*")]
    filepath = filedialog.askopenfilename(filetypes=types, title="Read Code")
    file = open(filepath, "r")
    sentence = file.read()
    file.close()
    sentence = sentence.replace(";", " ; ")
    sentence = sentence.replace('=', ' = ')
    sentence = sentence.replace('(', ' ( ')
    sentence = sentence.replace(')', ' ) ')
    sentence = sentence.replace('*', ' * ')
    sentence = sentence.replace('+', ' + ')
    sentence = sentence.replace('-', ' - ')
    sentence = sentence.replace('/', ' / ')
    sentence = sentence.replace('>', ' > ')
    sentence = sentence.replace('<', ' < ')
    sentence = sentence.replace(">=", " >= ")
    sentence = sentence.replace("<=", " <= ")
    sentence = sentence.replace('!', ' ! ')
    sentence = sentence.replace("!=", " != ")
    split = sentence.split()
    textbox.configure(state="normal")
    textbox.delete(1.0, END)
    textbox.insert(INSERT, sentence)
    textbox.configure(state="disabled")

def checkSyntax():
    global lookahead
    global i

    try:
        lookahead = nextToken()
        stmts()
        print(split)
        notification_success.show_animation()
        i = -1
        parse(split).draw()
    except SyntaxError:
        notification_error.show_animation()
        i = -1

imgSyntax = Image.open("images/syntax_6674488.png")
imgRead = Image.open("images/read.png")


textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70", corner_radius=16, border_color="#FFCC70", width=400, height=300, state="disabled")
btnSyntax = CTkButton(master=app, text="Check Syntax", corner_radius=32, fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2, image=CTkImage(light_image=imgSyntax), command=checkSyntax)
btnRead = CTkButton(master=app, text="Upload Code", corner_radius=32, fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2, image=CTkImage(light_image=imgRead), command=openFile)
labelHeader = CTkLabel(master=app, text="Parser &", corner_radius=32, fg_color="transparent", text_color="#FFCC70", font=("roboto", 45, 'bold'))
labelHeader1 = CTkLabel(master=app, text="Parse Tree Generator", corner_radius=32, fg_color="transparent", text_color="#FFCC70", font=("roboto", 45, 'bold'))
textbox.place(relx=0.5, rely=0.5, anchor="center")
btnSyntax.place(relx=0.35, rely=0.8, anchor="center")
btnRead.place(relx= 0.65, rely=0.8, anchor="center")
labelHeader.place(relx=0.5, rely=0.1, anchor="center")
labelHeader1.place(relx=0.5, rely=0.18, anchor="center")

#///////////////////////////////////////////////////Parser Code/////////////////////////////////////////////////////
# CFG
grammar = nltk.CFG.fromstring("""
    stmts -> stmt stmts |
    stmt -> assign_stmt | if_stmt | while_stmt   
    assign_stmt -> id '=' expr ';'            
    if_stmt -> 'if' '(' cond ')' stmt 'else' stmt                        
    while_stmt -> 'while' '(' cond ')' '{' stmts '}'

    cond -> id rel_op factor

    expr -> term rest
    rest -> '+' term rest | '-' term rest |
    term -> factor rest1
    rest1 -> '*' factor rest1  | '/' factor rest1 |

    factor -> id  | digit
    rel_op -> '<' | '>' | '<=' | '>=' | '==' | '!='                            
    id -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
    digit -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

def nextToken():
    global i
    global lookahead
    global split

    i = i + 1
    if(i == len(split)):
        return ''
    return split[i]

def match(t):
    global i
    global lookahead

    if (lookahead == t):
        lookahead = nextToken()
    else:
        error()

def error():
    global i
    global lookahead

    print(i)
    print(lookahead)
    print("Syntax Error")
    raise SyntaxError

def parse(sent):
    a = []
    parser = nltk.ChartParser(grammar)
    for tree in parser.parse(sent):
        a.append(tree)
    return (a[-1])
####################################################
def stmts():
    global i
    global lookahead
    global flag

    if(lookahead.isidentifier() or lookahead == "if" or lookahead == "while"):
        stmt()
        stmts()
    else:
        return

def stmt():
    global i
    global lookahead
    if (lookahead.isidentifier() and lookahead != "if" and lookahead != "while"):
        assign_stmt()
    elif (lookahead == "if"):
        if_stmt()
    elif (lookahead == "while"):
        while_stmt()
    else:
        error()

def assign_stmt():
    global i
    global lookahead
    id()
    match("=")
    expr()
    match(";")

def if_stmt():
    global i
    global lookahead

    match("if")
    match("(")
    cond()
    match(")")
    stmt()
    match("else")
    stmt()


def while_stmt():
    global i
    global lookahead
    match("while")
    match("(")
    cond()
    match(")")
    match("{")
    stmts()
    match("}")

def expr():
    global i
    global lookahead
    if(lookahead.isidentifier() or lookahead.isnumeric()):
        term()
        rest()
    else:
        error()

def rest():
    global i
    global lookahead
    if(lookahead == "+"):
        match("+")
        term()
        rest()
    elif(lookahead == "-"):
        match("-")
        term()
        rest()
    else:
        return

def term():
    global i
    global lookahead

    factor();
    rest1()

def rest1():
    global i
    global lookahead
    if(lookahead == "*"):
        match("*")
        factor()
        rest1()
    elif(lookahead == "/"):
        match("/")
        factor()
        rest1()
    else:
        return

def factor():
    if(lookahead.isidentifier()):
        id()
    elif(lookahead.isnumeric()):
        digit()
    else:
        error()


def cond():
    global i
    global lookahead
    id()
    relop()
    digit()



def relop():
    global i
    global lookahead

    if (lookahead == "<"):
        match("<")
    elif (lookahead == ">"):
        match(">")
    elif (lookahead == "<="):
        match("<=")
    elif (lookahead == ">="):
        match(">=")
    elif(lookahead == "!"):
        match("!")
    elif(lookahead == "!="):
        match("!=")
    else:
        error()
def id():
    global i
    global lookahead

    if (lookahead.isidentifier()):
        lookahead = nextToken()
    else:
        error()


def digit():
    global i
    global lookahead

    if (lookahead.isnumeric()):
        lookahead = nextToken()
    else:
        error()


#////////////////////////////////////////////Notification Bar//////////////////////////////////////////
class Notification(Frame):
    def __init__(self, master, width, height, bg, image, text, close_img, img_pad, text_pad, font, y_pos):
        super().__init__(master, bg=bg, width=width, height=height)
        self.pack_propagate(0)

        self.y_pos = y_pos

        self.master = master
        self.width = width

        right_offset = 8

        self.cur_x = self.master.winfo_width()
        self.x = self.cur_x - (self.width + right_offset)

        img_label = Label(self, image=image, bg=bg)
        img_label.image = image
        img_label.pack(side="left", padx=img_pad[0])

        message = Label(self, text=text, font=font, bg=bg, fg="black")
        message.pack(side="left", padx=text_pad[0])

        close_btn = Button(self, image=close_img, bg=bg, relief="flat", command=self.hide_animation, cursor="hand2")
        close_btn.image = close_img
        close_btn.pack(side="right", padx=5)

        self.place(x=self.cur_x, y=y_pos)

    def show_animation(self):
        if self.cur_x > self.x:
            self.cur_x -= 1
            self.place(x=self.cur_x, y=self.y_pos)

            self.after(1, self.show_animation)

    def hide_animation(self):
        if self.cur_x < self.master.winfo_width():
            self.cur_x += 1
            self.place(x=self.cur_x, y=self.y_pos)

            self.after(1, self.hide_animation)

sim = Image.open("images/success.png")
sim = sim.resize((25, 25), Image.LANCZOS)
sim = ImageTk.PhotoImage(sim)

cim = Image.open("images/close.png")
cim = cim.resize((10, 10), Image.LANCZOS)
cim = ImageTk.PhotoImage(cim)

eim = Image.open("images/error.png")
eim = eim.resize((25, 25), Image.LANCZOS)
eim = ImageTk.PhotoImage(eim)

img_pad = (5, 0)
text_pad = (5, 0)
notification_success = Notification(app, 230, 55, "white", sim, "Correct Syntax", cim, img_pad, text_pad, "cambria 11", 8)
notification_error = Notification(app, 230, 55, "white", eim, "Syntax Error", cim, img_pad, text_pad, "cambria 11", 8)

app.mainloop()