#Program to view stores, menu, store timings for various eateries in the north spine canteen
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkmacosx import Button
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry
from tkinter.messagebox import showinfo
#the above import statements deal with creation and design of GUI using tkinter 

import sys
import datetime #python library to retrieve and manipulate system and user defined date and time

#=================================
#JONATHAN
#=================================
def popup_showinfo():#popup window to be displayed on erroneous input
    showinfo("Error", "Plese enter a valid input!")

def calcWaitTime(*args):#function to retrieve the number of people in queue and set the total wait time depending on user input
    try:
        value = int(numPeople.get())
        if value < 0:
            popup_showinfo()
        else:
            waitTime.set(value*1.5)
    except ValueError:
        popup_showinfo()

#=================================
#JONATHAN
#=================================
def place_widgets(background_label, calcButton, waittime_result, qEntry, backButton, endProg):#function to define the placement of widgets at each storefront page
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    calcButton.place(x=590, y=328, height=36, width=70)
    waittime_result.place(x=530,y=375, height=20, width=40)
    qEntry.place(x=525,y=330, height=30, width=50)
    backButton.place(x=30, y=400, height=50, width=50)
    endProg.place(x=740, y=20, height =34, width=40)

#=================================
#KIM
#=================================
#function to display the menu items of a particular store 
def display_menu(f, itemDict):
    line_str = f.readlines() #initialization of string which holds text file contents

    for i in line_str: #converts the contents of the string into a dictionary with the menu item as the key and the price as the value
        new_str = i.split(":")
        itemDict[new_str[0]] = new_str[1]

    final_str = "" #initialization of final string that will be used to display the menu label widget
    for key, value in itemDict.items():
        final_str += key + " : " + value

    itemLabel = ttk.Label(root, text = final_str, font=('Trattatello')) #menu items label initialization and styling
    itemLabel.place(x=280,y=180, width=250, height=125)

#=================================
#ANEEZ
#=================================
#Function to set the program to the current system date and time
def SetDateToCurr():
    global day_str
    global time_str
    global hour_int
    now = datetime.datetime.now()
    day_str = datetime.datetime.today().strftime("%A")
    time_str = now.strftime("%H:%M:%S")
    hour_int = int(now.hour)

#=================================
#ANEEZ
#=================================
#Function to set the program to a user defined date and time
def SetDateToCustom(cus_day, cus_hour, cus_min):
    global day_str
    global time_str
    global hour_int

    #Special case handling to display the user defined time properly when it is a single digit
    if int(cus_hour) < 10:
        cus_hour = "0" + cus_hour
        
    if int(cus_min) < 10:
        cus_min = "0" + cus_min

    day_str = cus_day
    hour_int = cus_hour
    time_str = cus_hour + ":" + cus_min + ":00" 
    hour_int = int(cus_hour)

#=================================
#KIM
#=================================
#Function to end program when user clicks exit
def leavePage():
    try: 
        root.destroy()
        exit()
    except: 
        pass    

#=================================
#KIM
#=================================
#noodle store GUI
def Noodle(*args):
    itemDict = {}#initialization of dictionary to hold store menu information

    #commands to retrive an image from the system which will be used to design the various widgets present in the GUI
    noodle_back_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/Noodles_main.png")
    closed_screen_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/Noodles_close.png")
    Noodles_main = ImageTk.PhotoImage(noodle_back_img)   
    Noodles_close = ImageTk.PhotoImage(closed_screen_img)

    #initialization block for the widgets to be displayes to the user. Defines the various widgets and places them at an arbitrary location on the window
    background_label = Label(root, image=Noodles_main)
    background_label.image = Noodles_main # this is to keep a copy of the image in the file 
    calcButton = Button(root, text = "Calculate", command = calcWaitTime, image=EnterButton)
    waittime_result = ttk.Label(root, textvariable = waitTime)
    qEntry = ttk.Entry(root, textvariable = numPeople)
    backButton = Button(root, text = "", command = curStoresPage, image = back_button)
    endProg = Button(root, text = "", command = leavePage, image = CloseButton)

    place_widgets(background_label, calcButton, waittime_result, qEntry, backButton, endProg)

    #the conditional statements retrieve store menu information from text files depending on the present or user defined date and time
    if hour_int >= 8 and hour_int < 20:
        if(day_str == "Monday" or day_str == "Wednesday" or day_str == "Friday"):
            f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/noodle_mwf.txt", "r")
        else:
            f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/noodle_tt.txt", "r")
    else:
        noodles_close_label = ttk.Label(root, image= Noodles_close)
        noodles_close_label.place(x=0, y=0, relwidth=1, relheight=1)
        backButton = Button(root, text = "", command = curStoresPage, image = back_button)
        backButton.place(x=30, y=400, height=50, width=50)
        endProg = Button(root, text = "", command = leavePage, image = CloseButton)
        endProg.place(x=740, y=20, height =34, width=40)

    display_menu(f, itemDict)

    root.bind('<Return>', calcWaitTime)#binds the caluclate wait time button to the enter key on the keyboard

#=================================
#JONATHAN
#=================================
#western store GUI
def Western(*args):
    itemDict = {}#initialization of dictionary to hold store menu information

    #commands to retrive an image from the system which will be used to design the various widgets present in the GUI
    western_back_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/Western_main.png")
    store_closed_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/Western_close.png")
    Western_main = ImageTk.PhotoImage(western_back_img)
    Western_close = ImageTk.PhotoImage(store_closed_img)

    #initialization block for the widgets to be displayes to the user. Defines the various widgets and places them at an arbitrary location on the window
    background_label = Label(root, image=Western_main)
    background_label.image = Western_main # this is to keep a copy of the image in the file 
    calcButton = Button(root, text = "Calculate", command = calcWaitTime, image=EnterButton)
    waittime_result = ttk.Label(root, textvariable = waitTime)
    qEntry = ttk.Entry(root, textvariable = numPeople)
    backButton = Button(root, text = "", command = curStoresPage, image = back_button)
    endProg = Button(root, text = "", command = leavePage, image = CloseButton)

    place_widgets(background_label, calcButton, waittime_result, qEntry, backButton, endProg)

    #the conditional statements retrieve store menu information from text files depending on the present or user defined date and time
    if hour_int >= 8 and hour_int < 20:
        if(day_str == "Monday" or day_str == "Wednesday" or day_str == "Friday"):
            f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/western_mwf.txt", "r")
        else:
            f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/western_tt.txt", "r")
    else:
        Western_close_label = ttk.Label(root, image= Western_close)
        Western_close_label.place(x=0, y=0, relwidth=1, relheight=1)
        backButton = Button(root, text = "", command = curStoresPage, image = back_button)
        backButton.place(x=30, y=400, height=50, width=50)
        endProg = Button(root, text = "", command = leavePage, image = CloseButton)
        endProg.place(x=740, y=20, height =34, width=40)

    display_menu(f, itemDict)

    root.bind('<Return>', calcWaitTime)#binds the caluclate wait time button to the enter key on the keyboard

#=================================
#ANEEZ
#=================================
#Chinese store GUI
def Chinese(*args):
    itemDict = {}#initialization of dictionary to hold store menu information

    #commands to retrive an image from the system which will be used to design the various widgets present in the GUI
    miniwok_back_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/Miniwok_Main.png")
    store_closed_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/Miniwok_close.png")
    Miniwok_Main = ImageTk.PhotoImage(miniwok_back_img)
    Miniwok_close = ImageTk.PhotoImage(store_closed_img)

    #initialization block for the widgets to be displayes to the user. Defines the various widgets and places them at an arbitrary location on the window
    background_label = Label(root, image=Miniwok_Main)
    background_label.image = Miniwok_Main # this is to keep a copy of the image in the file 
    calcButton = Button(root, text = "Calculate", command = calcWaitTime, image=EnterButton)
    waittime_result = ttk.Label(root, textvariable = waitTime)
    qEntry = ttk.Entry(root, textvariable = numPeople)
    backButton = Button(root, text = "", command = curStoresPage, image = back_button)
    endProg = Button(root, text = "", command = leavePage, image = CloseButton)

    place_widgets(background_label, calcButton, waittime_result, qEntry, backButton, endProg)

    #the conditional statements retrieve store menu information from text files depending on the present or user defined date and time
    if hour_int >= 8 and hour_int < 20:
        if(day_str == "Monday" or day_str == "Wednesday" or day_str == "Friday"):
            f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/chinese_mwf.txt", "r")
        else:
            f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/chinese_tt.txt", "r")
    else:
        Miniwok_close_label = ttk.Label(root, image= Miniwok_close)
        Miniwok_close_label.place(x=0, y=0, relwidth=1, relheight=1)
        backButton = Button(root, text = "", command = curStoresPage, image = back_button)
        backButton.place(x=30, y=400, height=50, width=50)
        endProg = Button(root, text = "", command = leavePage, image = CloseButton)
        endProg.place(x=740, y=20, height =34, width=40)

    display_menu(f, itemDict)

    root.bind('<Return>', calcWaitTime)#binds the caluclate wait time button to the enter key on the keyboard

#=================================
#JONATHAN, ANEEZ
#=================================
#McD store GUI
def McDRegular(*args):
    itemDict = {}#initialization of dictionary to hold store menu information
    
    #commands to retrive images from the system which will be used to design the various widgets present in the GUI
    mcd_back_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/MCD_main.png")
    store_closed_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/MCD_close.png")
    MCD_main = ImageTk.PhotoImage(mcd_back_img)
    MCD_close = ImageTk.PhotoImage(store_closed_img)


    #initialization block for the widgets to be displayes to the user. Defines the various widgets and places them at an arbitrary location on the window
    background_label = Label(root, image=MCD_main)
    background_label.image = MCD_main # this is to keep a copy of the image in the file 
    calcButton = Button(root, text = "Calculate", command = calcWaitTime, image=EnterButton)
    waittime_result = ttk.Label(root, textvariable = waitTime)
    qEntry = ttk.Entry(root, textvariable = numPeople)
    backButton = Button(root, text = "", command = curStoresPage, image = back_button)
    endProg = Button(root, text = "", command = leavePage, image = CloseButton)

    place_widgets(background_label, calcButton, waittime_result, qEntry, backButton, endProg)

    
    #the conditional statements retrieve store menu information from text files depending on the present or user defined date and time
    if(hour_int >= 7 and hour_int <= 10):
        f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/mcd_breakfast.txt", "r")
    elif hour_int >= 11 and hour_int < 22:
        f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/mcd_regular.txt", "r")
    else:
        MCD_close_label = ttk.Label(root, image= MCD_close)
        MCD_close_label.place(x=0, y=0, relwidth=1, relheight=1)
        backButton = Button(root, text = "", command = curStoresPage, image = back_button)
        backButton.place(x=30, y=400, height=50, width=50)
        endProg = Button(root, text = "", command = leavePage, image = CloseButton)
        endProg.place(x=740, y=20, height =34, width=40)

    display_menu(f, itemDict)

    root.bind('<Return>', calcWaitTime)#binds the caluclate wait time button to the enter key on the keyboard

#=================================
#ANEEZ, KIM
#=================================
#kfc store GUI
def kfcRegular(*args):
    itemDict = {}#initialization of dictionary to hold store menu information
    global time_str
    global day_str

    #commands to retrive an image from the system which will be used to design the various widgets present in the GUI
    kfc_back_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/KFC_main.png")
    store_closed_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/KFC_close.png")
    KFC_main = ImageTk.PhotoImage(kfc_back_img)
    KFC_close = ImageTk.PhotoImage(store_closed_img)


    #initialization block for the widgets to be displayes to the user. Defines the various widgets and places them at an arbitrary location on the window
    background_label = Label(root, image=KFC_main)
    background_label.image = KFC_main # this is to keep a copy of the image in the file 
    calcButton = Button(root, text = "Calculate", command = calcWaitTime, image=EnterButton)
    waittime_result = ttk.Label(root, textvariable = waitTime)
    qEntry = ttk.Entry(root, textvariable = numPeople)
    backButton = Button(root, text = "", command = curStoresPage, image = back_button)
    endProg = Button(root, text = "", command = leavePage, image = CloseButton)

    place_widgets(background_label, calcButton, waittime_result, qEntry, backButton, endProg)

    #the conditional statements retrieve store menu information from text files depending on the present or user defined date and time
    if(hour_int >= 6 and hour_int <= 10):
        f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/kfc_breakfast.txt", "r")
    elif hour_int >= 11 and hour_int < 22:
        f = open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/kfc_regular.txt", "r")
    else:
        KFC_close_label = ttk.Label(root, image= KFC_close)
        KFC_close_label.place(x=0, y=0, relwidth=1, relheight=1)
        backButton = Button(root, text = "", command = curStoresPage, image = back_button)
        backButton.place(x=30, y=400, height=50, width=50)
        endProg = Button(root, text = "", command = leavePage, image = CloseButton)
        endProg.place(x=740, y=20, height =34, width=40)

    display_menu(f, itemDict)

    root.bind('<Return>', calcWaitTime)#binds the caluclate wait time button to the enter key on the keyboard

#=================================
#ANEEZ
#=================================
#Defines a page that allows users to input custom date and time preferences
def dateEntryPage(*args):
    hourString = StringVar()
    minString = StringVar()

    #Function to retrieve the custom date and time values from the user
    def getDateValues():
        try:
            day = cal.selection_get()
            hour = hourString.get()
            minute = minString.get()
            SetDateToCustom(day.strftime("%A"), hour, minute)
        except ValueError:
            pass

    global flag
    flag = True

    today = datetime.date.today()
    mindate = datetime.date(today.year, today.month, today.day)#sets minimum date on the calendar as todays date
    maxdate = datetime.date(year = 2030, month = 12, day = 30)#sets maximum date on the calendar

    #commands to retrive an image from the system which will be used to design the various widgets present in the GUI
    selDate_back_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/OtherDates/selectdate.png")
    Enter_Button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/OtherDates/Enter_Button.png")
    set_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/OtherDates/Set_Button.png")
    selDate_Background = ImageTk.PhotoImage(selDate_back_img)
    Enter_Button = ImageTk.PhotoImage(Enter_Button_img)
    Set_Button = ImageTk.PhotoImage(set_button_img)
    
    s = ttk.Style()
    s.theme_use('clam')

    #initialization block for the widgets to be displayes to the user. Defines the various widgets and places them at an arbitrary location on the window
    customFrame = ttk.Frame(root, padding = "0")
    background_label = Label(root, image=selDate_Background)
    background_label.image = selDate_Background # this is to keep a copy of the image in the file 
    enterButton = Button(root, text = "", command = curStoresPage, image = Enter_Button)
    setButton = Button(root, text = "Set", command = getDateValues, image = Set_Button)
    backButton = Button(root, text = "Go Back", command = mainScreen, image = back_button)
    cal = Calendar(root, font="Arial 14", selectmode='day', locale='en_US', mindate=mindate, maxdate=maxdate, disabledforeground='red', cursor="hand1", year=2018, month=2, day=5)
    hourEntry = ttk.Combobox(root, values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23), width = 10, textvariable = hourString, state="readonly")
    hourEntry.current(9)#sets the default value of the combobox
    minuteEntry = ttk.Combobox(root, values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59), width = 10, textvariable = minString, state="readonly")
    minuteEntry.current(29)#sets default value of combobox
    endProg = Button(root, text = "", command = leavePage, image = CloseButton)

    #Placement block for the widgets to be displayed to the user. Defines the coordinates on the window at which each widget should be placed
    customFrame.place()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    enterButton.place(x=650, y=340, height = 146, width = 128)
    setButton.place(x=520, y=340, height=146, width=128)
    backButton.place(x=30, y=400, height=50, width=50)
    cal.pack(expand=False)
    cal.place(x = 250, y = 150)
    hourEntry.place(x=250, y=380)
    minuteEntry.place(x=420, y=380)
    endProg.place(x=740, y=20, height =34, width=40)

#=================================
#KIM
#=================================
def curStoresPage(*args):
    global flag
    if flag == False:
        SetDateToCurr()
    else:
        pass

    #commands to retrieve an image from the system which will be used to design the various widgets present in the GUI
    availableStores_back_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/CurrStores/AvailStores.png")
    kfc_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/CurrStores/KFC.png")
    McD_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/CurrStores/McD.png")
    noodles_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/CurrStores/Noodles.png")
    western_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/CurrStores/Western.png")
    miniwok_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/CurrStores/Miniwok.png")
    AvailStores = ImageTk.PhotoImage(availableStores_back_img)
    KFC = ImageTk.PhotoImage(kfc_button_img)
    McD = ImageTk.PhotoImage(McD_button_img)
    Noodles = ImageTk.PhotoImage(noodles_button_img)
    PorkChop = ImageTk.PhotoImage(western_button_img)
    Miniwok = ImageTk.PhotoImage(miniwok_button_img)

    style = ttk.Style()#style tag to define the label style and font color
    style.configure("TLabel", foreground = 'black')

    background_label = Label(root, image=AvailStores)
    background_label.image = AvailStores # this is to keep a copy of the image in the file 
    store1 = Button(root, text = "KFC", command = kfcRegular, image = KFC)
    store2 = Button(root, text = "McDonald's", command = McDRegular, image = McD)
    store3 = Button(root, text = "Mini Wok", command = Chinese, image = Miniwok)
    store4 = Button(root, text = "Noodle", command = Noodle, image = Noodles)
    store5 = Button(root, text = "Western", command = Western, image = PorkChop)
    backButton = Button(root, text = "", command = mainScreen, image = back_button)
    endProg = Button(root, text = "", command = leavePage, image = CloseButton)

    #placement block for the widgets to be displayed to the user. Defines the coordinates on the window at which each widget should be placed
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    store1.place(x=350,y=175, height=46, width=190)
    store2.place(x=350,y=230, height=46, width=190)
    store3.place(x=350, y=405, height=46, width=190)
    store4.place(x=350, y=290, height=46, width=190)
    store5.place(x=350, y=348, height=46, width=190)
    backButton.place(x=30, y=400, height=50, width=50)
    endProg.place(x=740, y=20, height =34, width=40)

#=================================
#JONATHAN
#=================================
def mainScreen(*args):
    global flag
    flag = False

    style = ttk.Style()#style tag to define the label style and font color
    style.configure("TLabel", foreground = 'white')

    #commands to retrive an image from the system which will be used to design the various widgets present in the GUI
    main_back_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/MainPage/MainBackground.png")
    currStores_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/MainPage/CurrentStore.png")
    otherDates_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/MainPage/OtherDates.png")
    image3 = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/MainPage/black.png")
    MainBackground = ImageTk.PhotoImage(main_back_img)
    CurrentStore = ImageTk.PhotoImage(currStores_button_img)
    OtherDates = ImageTk.PhotoImage(otherDates_button_img)
    black_background = ImageTk.PhotoImage(image3)

    current_time = time_str
    day = day_str

    #initialization block for the widgets to be displayes to the user. Defines the various widgets and places them at an arbitrary location on the window
    background_label = Label(root, image=MainBackground)
    background_label.image = MainBackground # this is to keep a copy of the image in the file 
    dayLabel = ttk.Label(root, text = day, image = black_background, compound=CENTER)
    timeLabel = ttk.Label(root, text = current_time, image = black_background, compound=CENTER)
    currDate = Button(root, text = "Current Stores", command = lambda : curStoresPage(), image = CurrentStore)
    otherDate = Button(root, text = "View stores by other dates", command = lambda: dateEntryPage(), image = OtherDates)
    endProg = Button(root, text = "", command = leavePage, image = CloseButton)

    #placement block for the widgets to be displayed to the user. Defines the coordinates on the window at which each widget should be placed
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    dayLabel.place(x=100, y=20, height = 30, width = 100)
    timeLabel.place(x=400, y=20, height = 30, width = 100)
    currDate.place(x=252, y=270, height=54, width=292)
    otherDate.place(x=252, y=350, height=54, width=292)
    endProg.place(x=740, y=20, height =34, width=40)

    root.mainloop()

flag = False #flag variable to check if the store should display the current date and time or the custom date and time

now = datetime.datetime.now()
day_str = datetime.datetime.today().strftime("%A")#Returns the current day as a string
time_str = now.strftime("%H:%M:%S")#Returns the current time as HH:MM:SS
hour_int = int(now.hour)

root = Tk()#intial root window on which information and widgets will be displayed
root.title("NTU North Spine Canteen System")
root.geometry("800x504+325+175")#sets the position of the window on execution of the program
root.maxsize(800,500)#sets the maximum size of the GUI window to prevent resizing 
root.minsize(800,500)#sets the minimum size of the GUI window to prevent resizing

waitTime = StringVar()#initializes a string that will store the waiting time at the store
numPeople = StringVar()#initializes a string that will retrieve the number of people in queue at the store 

#public declaration and retrieval of images that will be used in every page of the GUI
back_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/back_button.png")
close_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/CloseButton.png")
enter_button_img = Image.open("/Users/aneez.jah/Desktop/Y1S1 Coursework/Introduction to Computational Thinking/Mini Project/NSCanteenSystem/Stores/Enter.png")
back_button = ImageTk.PhotoImage(back_button_img)
CloseButton = ImageTk.PhotoImage(close_button_img)
EnterButton = ImageTk.PhotoImage(enter_button_img)

mainScreen()