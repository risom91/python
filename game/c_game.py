from tkinter import *

import mysql.connector
import random
import time


class guess_color:
    #colors to be used
    colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
               'Yellow', 'Orange', 'White', 'Purple', 'Brown']

    score = 0

    # the game time left, initially 30 seconds.
    timeleft = 30

    #list of top 3 scorers
    topScorers=""

    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="color guess")
        self.mycursor = self.conn.cursor()

        # login and register option window
        self.root = Tk()
        self.root.title("Guessing Game")
        self.root.iconbitmap(r'clr.ico')

        self.root.minsize(300, 250)
        self.root.maxsize(300, 250)
        self.root.configure(background="#65A3BC")

        label1 = Label(self.root, text="LOGIN & REGISTRATION", bg="#65A3BC", fg="#ffffff")
        label1.configure(font=("segoe script", 15, "bold"))
        label1.pack(pady=(15, 4))

        #button for login window
        click = Button(self.root, text="LOGIN",fg="#904C01", bg="#ffffff", width=18, height=2,font=("segoe script", 8, "bold"), command=lambda: self.login())

        click.pack(pady=(30, 20))

        #button for registration window
        click = Button(self.root, text="REGISTER",fg="#904C01", bg="#ffffff", width=18, height=2,font=("segoe script", 8, "bold"), command=lambda: self.register())
        click.pack(pady=(10, 20))

        self.root.mainloop()

    def login(self):
        # login window
        self.root = Tk()
        self.root.title("login")
        self.root.minsize(300, 400)
        self.root.maxsize(300, 400)
        self.root.configure(background="#65A3BC")
        self.root.iconbitmap(r'clr.ico')
        


        label1 = Label(self.root, text="EMAIL", bg="#65A3BC", fg="#904C01")
        label1.configure(font=("segoe script", 15, "bold"))
        label1.pack(pady=(15, 4))

        self.Email = Entry(self.root)
        self.Email.pack(ipadx=40, ipady=8, pady=(15, 20))

        label1 = Label(self.root, text="PASSWORD", bg="#65A3BC", fg="#904C01")
        label1.configure(font=("segoe script", 15, "bold"))
        label1.pack(pady=(15, 5))

        self.password = Entry(self.root)
        self.password.pack(ipadx=40, ipady=8, pady=(15, 20))

        click = Button(self.root, text="LOGIN", bg="#ffffff",font=("segoe script", 8, "bold"),fg="black", width=18, height=2, command=lambda: self.Login())
        click.pack(pady=(20, 20))

        self.result = Label(self.root, bg="#65A3BC", fg="#ffffff")
        self.result.configure(font=("MV Boli", 14))
        self.result.pack(pady=(5, 10))

        self.root.mainloop()

    def register(self):
        # register window
        self.root = Tk()
        self.root.title("register")
        self.root.minsize(300, 510)
        self.root.maxsize(300, 510)
        self.root.configure(background="#65A3BC")
        self.root.iconbitmap(r'clr.ico')

        
        label1 = Label(self.root, text="Enter name", bg="#65A3BC", fg="#904C01")
        label1.configure(font=("segoe script", 15, "bold"))
        label1.pack(pady=(15, 4))

        #name entry
        self.name = Entry(self.root)
        self.name.pack(ipadx=30, ipady=8, pady=(15, 20))

        label1 = Label(self.root, text="Enter email", bg="#65A3BC", fg="#904C01")
        label1.configure(font=("segoe script", 15, "bold"))
        label1.pack(pady=(15, 4))

        #email entry
        self.email = Entry(self.root)
        self.email.pack(ipadx=30, ipady=8, pady=(15, 20))

        label1 = Label(self.root, text="Enter password", bg="#65A3BC", fg="#904C01")
        label1.configure(font=("segoe script", 15, "bold"))
        label1.pack(pady=(15, 4))

        #password entry
        self.password = Entry(self.root)
        self.password.pack(ipadx=30, ipady=8, pady=(15, 20))

        click = Button(self.root, text="REGISTER", bg="#ffffff", fg="black",width=18, height=2,font=("segoe script", 9, "bold"), command=lambda: self.Register())
        click.pack(pady=(10, 10))

        self.result = Label(self.root, bg="#65A3BC", fg="#ffffff")
        self.result.configure(font=("MV Boli", 14))
        self.result.pack(pady=(5, 10))


        self.root.mainloop()

    def Register(self):
        # register button commands
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()

        self.mycursor.execute("SELECT email FROM color_users WHERE email LIKE '{}' ".format(email))
        reg_email_list = self.mycursor.fetchall()

        # checking if email already exists
        if reg_email_list != []:

            self.result.configure(text="email already registered")

        # checking if all the details are filled
        elif len(name) == 0 or len(email) == 0 or len(password) == 0:
            self.result.configure(text="Enter All The credentials")

        # inserting into the database
        else:
            self.mycursor.execute(
                "INSERT INTO color_users(user_id,name,email,password) VALUES(NULL,'{}','{}','{}')".format(name, email,
                                                                                                          password))
            self.conn.commit()

            self.result.configure(text="Registration Successful")

    def Login(self):
        Email = self.Email.get()
        password = self.password.get()

        # checking on the database if the provided info's correct-
        self.mycursor.execute(
            "SELECT * FROM color_users WHERE email LIKE '{}' AND password LIKE '{}'".format(Email, password))

        if len(self.mycursor.fetchall()) == 0:
            self.result.configure(text="Invalid Credentials")

        # starting the game if info's correct
        else:
            self.game()


    def game(self):

        global timeleft

        self.root = Tk()


        
        self.root.title("COLORGAME")

        # set the size
        self.root.minsize(750,250)
        self.root.maxsize(750,250)
        
        self.root.iconbitmap(r'clr.ico')

        #ranking label
        self.leaderboardTitle = Label(self.root, text="RANKING-\n",font=('Segoe Print',14,"bold"),fg='#65A3BC')
        self.leaderboardTitle.pack(padx=0, pady=10, side=LEFT)

        #label for top 3 high scorers
        self.leaderboard= Label(self.root, font=('Helvetica', 12))
        self.leaderboard.pack(padx=0, pady=10,side=LEFT)


        # instructions label
        instructions = Label(self.root, text="Type in the COLOUR of the words, and not the word text!",font=('segoe script', 12),underline=0)
        self.leaderboard.pack(padx=0, pady=10)
        instructions.pack()

        #  score label
        self.scoreLabel = Label(self.root, text="Press ENTER to start",font=('Segoe Script', 12,"bold"))
        self.leaderboard.pack(padx=0, pady=10)
        self.scoreLabel.pack()

        # time left label
        self.timeLabel = Label(self.root, text="TIME LEFT: " + str(self.timeleft)+ "  sec  ", font=('Segoe Script', 12,'bold'))
        self.leaderboard.pack(padx=0, pady=10)

        self.timeLabel.pack()

        #  label for displaying  colours
        self.label = Label(self.root, font=('segoe script', 50,'bold'))
        self.leaderboard.pack(padx=0, pady=10)
        self.label.pack()

        # entry box for typing in colours
        self.e = Entry(self.root)
        self.leaderboard.pack(padx=0, pady=10)

        # run the 'startGame' function when the enter key is pressed
        self.root.bind('<Return>', self.startGame)
        self.e.pack()

        # set focus on the entry box
        self.e.focus_set()

        self.root.mainloop()

    def startGame(self,strt):

        if self.timeleft == 30:    # start the countdown timer.
            self.countdown()

            # run the function to
        # choose the next colour.
        self.nextColour()
        self.highScore()

    # Countdown timer function
    def countdown(self):
        global timeleft


        # if a game is in play
        if self.timeleft > 0:
            # decrement the timer.
            self.timeleft -= 1

            # update the time left label
            self.timeLabel.config(text="Time left: "
                                  + str(self.timeleft))

            # run the function again after 1 second.
            self.timeLabel.after(1000, self.countdown)


    # Function to choose and
    # display the next colour.
    def nextColour(self):
        # use the globally declared 'score'
        # and 'play' variables above.
        global score
        global timeleft

        # if a game is currently in play
        if self.timeleft > 0:

            # make the text entry box active.
            self.e.focus_set()

            # if the colour typed is equal
            # to the colour of the text
            if self.e.get().lower() == self.colours[1].lower():
                self.score += 1

            # clear the text entry box.
            self.e.delete(0,END)

            random.shuffle(self.colours)

            # change the colour to type, by changing the
            # text _and_ the colour to a random colour value
            self.label.config(fg=str(self.colours[1]), text=str(self.colours[0]))

            # update the score.
            self.scoreLabel.config(text="Score: " + str(self.score))

        elif self.timeleft==0:
            
            time.sleep(2)
            self.timeleft=30
            self.score=0
            

    def highScore(self):
        global score
        global topScorers


        email = self.Email.get()
        #getting the highest  score of the user from the  database
        self.mycursor.execute("SELECT score FROM color_users WHERE email LIKE '{}' ".format(email))
        a = self.mycursor.fetchall()
        for i in a[0]:
            userScore=int(i)

        if self.score>userScore:
            self.mycursor.execute("UPDATE color_users SET score='{}' WHERE email LIKE '{}' ".format(self.score,email))
            self.conn.commit()

        else:
            pass

        #finding the top 3 players and their scores
        self.mycursor.execute("SELECT UPPER(CONCAT(name,': :',score)) FROM `color_users` ORDER BY score DESC LIMIT 3 ")
        LB= self.mycursor.fetchall()



        #display the leaderboard
        self.leaderboard.config(text=str(LB[0][0])+'\n'+str(LB[1][0])+'\n'+str(LB[2][0]),fg="#904C01",font=('Segoe Script',12,'italic'))









obj=guess_color()
