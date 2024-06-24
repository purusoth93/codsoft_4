from tkinter import *
from tkinter import messagebox
from random import choice, randint
from PIL import Image,ImageTk
class rps(Tk):
    def __init__(self):
        super().__init__()
        self.i=0
        self.j=0
        self.geometry("450x400")
        self.title("Rock Paper Scissor")
        self.configure(bg="black")
        self.create_widgets()
        
    def create_widgets(self):
        #heeading 
        self.head_label=Label(text="ROCK PAPER SCISSOR",font=("bold",15),fg="yellow",bg="black")
        self.head_label.grid(padx=100,pady=10,row=0,column=0,columnspan=5)
        
        #default image
        self.user_canvas=Canvas(height=100,width=100,bg="white")
        self.user_canvas.grid(row=1,column=0)
        
        self.computer_canvas=Canvas(height=100,width=100,bg="white")
        self.computer_canvas.grid(row=1,column=2)

        
        #Label for computer and player
        self.player_label=Label(text="Player",font=("bold",10),fg="yellow",bg="black")
        self.player_label.grid(row=4,column=0,padx=10,pady=10)
        
        self.computer_label=Label(text="computer",font=("bold",10),fg="yellow",bg="black")
        self.computer_label.grid(row=4,column=2)
        
        #score label
        self.score_label=Label(text=f"PLAYER:{self.i}/10   COMPURTER:{self.j}/10",font=("bold",10),fg="yellow",bg="black")
        self.score_label.grid(row=6,column=1,pady=10)
        
        #choice buttons
        self.rock_butn=Button(self,text="ROCK",font=("bold",10),fg="yellow",bg="red",command=lambda t="rock":self.score(t))
        self.rock_butn.grid(row=8,column=1,pady=5)
        
        self.paper_butn=Button(self,text="PAPER",font=("bold",10),fg="yellow",bg="red",command=lambda t="paper":self.score(t))
        self.paper_butn.grid(row=9,column=1,pady=5)
        
        self.sissor_butn=Button(self,text="SCISSOR",font=("bold",10),fg="yellow",bg="red",command=lambda t="scissor":self.score(t))
        self.sissor_butn.grid(row=10,column=1,pady=5)
         
        #restart button
        
        self.play_butn=Button(self,text="PLAY AGAIN",font=("bold",10),fg="yellow",bg="black",command=self.restart,width=40)
        self.play_butn.grid(row=11,column=0,columnspan=3,padx=60,pady=5)
        
     #score calculation   
    def score(self,player):
        choi=["rock","paper","scissor"]
        computer=choice(choi)
        
        
        if self.i>10 or self.j>10:
            messagebox.showinfo(title="GAME OVER!",message="click play again to play!")
        else:
            #changing photo of player
            if player=="rock":
                self.change1_img("rock.png")
            elif player=="paper":
                self.change1_img("paper.png")
            elif player=="scissor":
                self.change1_img("scissor.png")
            #changing photo of computer
            if computer=="rock":
                self.change2_img("rock.png")
            elif computer=="paper":
                self.change2_img("paper.png")
            elif computer=="scissor":
                self.change2_img("scissor.png")
            #calculating and displaying score
            if player==computer:
                pass
            elif player=="rock" and computer=="paper":
                self.j=self.j+1
                self.score_label.config(text=f"PLAYER:{self.i}/10   COMPURTER:{self.j}/10")
            elif player=="paper" and computer=="rock":
                self.i=self.i+1
                self.score_label.config(text=f"PLAYER:{self.i}/10   COMPURTER:{self.j}/10")
            elif player=="rock" and computer=="scissor":
                self.i=self.i+1
                self.score_label.config(text=f"PLAYER:{self.i}/10   COMPURTER:{self.j}/10")
            elif player=="scissor" and computer=="rock":
                self.j=self.j+1
                self.score_label.config(text=f"PLAYER:{self.i}/10   COMPURTER:{self.j}/10")
            elif player=="paper" and computer=="scissor":
                self.j=self.j+1
                self.score_label.config(text=f"PLAYER:{self.i}/10   COMPURTER:{self.j}/10")
            elif player=="scissor" and computer=="paper":
                self.i=self.i+1
                self.score_label.config(text=f"PLAYER:{self.i}/10   COMPURTER:{self.j}/10")
                        
            if self.i==10:
                messagebox.showinfo(title="winner",message="player won!\n click ok to continue")
                self.i +=1
            elif self.j==10:
                messagebox.showinfo(title="looser",message="computer won!\n click ok to continue")
                self.j +=1
    #restart
    def restart(self):
        self.i=0
        self.j=0  
        self.score_label.config(text=f"PLAYER:{self.i}/10   COMPURTER:{self.j}/10")
        self.user_canvas=Canvas(height=100,width=100,bg="white")
        self.user_canvas.grid(row=1,column=0)
        
        self.computer_canvas=Canvas(height=100,width=100,bg="white")
        self.computer_canvas.grid(row=1,column=2)   
        
    def change1_img(self,path):
        pil_image=Image.open(path)
        self.tk_image=ImageTk.PhotoImage(pil_image)
        self.user_canvas.create_image(50,50,image=self.tk_image)
            
    def change2_img(self,path):
        pil_image1=Image.open(path)
        self.tk_image1=ImageTk.PhotoImage(pil_image1)
        self.computer_canvas.create_image(50,50,image=self.tk_image1)      
app=rps()
app.mainloop()