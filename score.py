from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__( )
        self.score=0
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.hideturtle()
        self.score_board()

    def score_board(self):
            self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.score_board()