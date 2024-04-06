import random
from tkinter import *
# from PIL import Image, ImageTk # type: ignore
# image_path = "./" + f"{player_choice.lower()}.jpg"
from PIL import Image, ImageTk;


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("800x500+300+170")
        self.root.resizable(False, False)

        image1 = Image.open("game.jpg")
        resize = image1.resize((800, 400))
        self.image_label = ImageTk.PhotoImage(resize)

        self.label = Label(self.root, image=self.image_label)
        self.label.place(x=0, y=0)

        btn = Button(self.root, text="START", font=("Arial", 16, "bold"), bd=2, relief=RIDGE, bg="brown", cursor="hand2", fg="gold", command=self.start)
        btn.place(x=350, y=435)

    def start(self):
        self.root.destroy()
        window = Tk()
        obj1 = Newwindow(window)
        window.mainloop()

class Newwindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Rock Paper Scissors")
        self.window.geometry("800x500+300+170")
        self.window.resizable(False, False)
        self.window.config(bg="ivory3")

        self.choices = ["Rock", "Paper", "Scissor"]

        lower_frame = Frame(self.window, bg="white", width=800, height=130)
        lower_frame.place(x=0, y=300)

        label1 = Label(lower_frame, text="Make your choice", font=("Arial", 16, "bold"), fg="black", width=50, bg="white")
        label1.place(x=80, y=10)

        rock = Button(lower_frame, text="Rock", font=("Arial", 16, "bold"), bd=2, relief=RIDGE, bg="dark slate gray", cursor="hand2", fg="white", width=10)
        rock.place(x=100, y=60)
        rock.config(command=lambda: self.choice_update("Rock"))

        paper = Button(lower_frame, text="Paper", font=("Arial", 16, "bold"), bd=2, relief=RIDGE, bg="dark slate gray", cursor="hand2", fg="white", width=10)
        paper.place(x=340, y=60)
        paper.config(command=lambda: self.choice_update("Paper"))

        scissor = Button(lower_frame, text="Scissor", font=("Arial", 16, "bold"), bd=2, relief=RIDGE, bg="dark slate gray", cursor="hand2", fg="white", width=10)
        scissor.place(x=580, y=60)
        scissor.config(command=lambda: self.choice_update("Scissor"))

        self.label_computer = Label(self.window, image=None)
        self.label_computer.place(x=500, y=90)

        self.label_player = Label(self.window, image=None)
        self.label_player.place(x=100, y=90)

        self.player_score = 0
        self.computer_score = 0
        self.player_score_label = Label(self.window, text="Player Score : 0", font=("Arial", 16, "bold"), fg="black", bg="ivory3")
        self.player_score_label.place(x=100, y=50)

        self.computer_score_label = Label(self.window, text="Computer Score : 0", font=("Arial", 16, "bold"), fg="black", bg="ivory3")
        self.computer_score_label.place(x=500, y=50)

        self.final_msg = Label(self.window, font=("Arial", 20, "bold"), bg="white", width=20)
        self.final_msg.place(x=230, y=440)

    def choice_update(self, player_choice):
        choice_computer = random.choice(self.choices)

        self.update_computer_choice(choice_computer)
        self.update_player_choice(player_choice)
        self.winner_check(player_choice, choice_computer)

    def update_computer_choice(self, computer_choice):
        image_path = f"{computer_choice.lower()}.jpg"
        image = Image.open(image_path).resize((200, 200))
        computer_choice_image = ImageTk.PhotoImage(image)
        self.label_computer.config(image=computer_choice_image)
        self.label_computer.image = computer_choice_image

    def update_player_choice(self, player_choice):
        image_path = f"{player_choice.lower()}.jpg"
        image = Image.open(image_path).resize((200, 200))
        player_choice_image = ImageTk.PhotoImage(image)
        self.label_player.config(image=player_choice_image)
        self.label_player.image = player_choice_image

    def msg_updation(self, message):
        self.final_msg.config(text=message)

    def Computer_update(self):
        self.computer_score += 1
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def Player_update(self):
        self.player_score += 1
        self.player_score_label.config(text=f"Player Score: {self.player_score}")

    def winner_check(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            self.msg_updation("It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissor") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissor" and computer_choice == "Paper"):
            self.msg_updation("Player wins!")
            self.Player_update()
        else:
            self.msg_updation("Computer wins!")
            self.Computer_update()

root = Tk()
obj = Game(root)
root.mainloop()
