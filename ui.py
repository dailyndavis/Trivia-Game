from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#B1DDC6"
BLOCK_COLOR = "#c6edf5"
RED = "#ff6961"
GREEN = "#77dd77"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score_label = Label(text="Score: 0", font=("Monaco", 13), bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canvas 
        self.canvas = Canvas(width=300, height=250, bg=BLOCK_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 126, text="Question text goes here", fill="black", font=("Monaco", 15, "italic"), width=275)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # True button
        self.true_image = PhotoImage(file="./images/newest_check.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, highlightbackground=THEME_COLOR, fg=THEME_COLOR, command=self.answer_is_true)
        self.true_button.grid(column=0, row=2)

        # False button 
        self.false_image = PhotoImage(file="./images/newest_x.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, highlightbackground=THEME_COLOR, fg=THEME_COLOR, command=self.answer_is_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # Tap into quiz brain and call next question
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Well done! 🎈 \nYou've reached the end of the quiz. 🏁")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
# ✨👩🏻‍💻 Challenge 👩🏻‍💻✨
# Create two new methods that you can add as a command
# to the buttons. 
# The methods need to call check_answer()
# from the quiz_brain, and pass of the string 
# "True" or "False". 
# This should print some feedback to the console

# This is what we're sending over as the user's answer. 

    def answer_is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        

    def answer_is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def change_bg_green(self):
        self.canvas.configure(bg=GREEN)

    def change_bg_red(self): 
        self.canvas.configure(bg=RED)

    def change_bg_normal(self):
        self.canvas.configure(bg=BLOCK_COLOR)
        self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.window.after(1000, self.change_bg_green)
        else:
            self.window.after(1000, self.change_bg_red)

        self.window.after(2000, self.change_bg_normal)



        
# ✨👩🏻‍💻 Challenge 👩🏻‍💻✨
# Change the canvas bg to green if is_right is True
# and red if is_right is False

# When a button has been pressed, display the next question after
# 1000 ms, but make sure to change the bg back to white 
