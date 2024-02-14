import math
import turtle as turt
import time
import colorsys
def heart():
      def hearta(k):
            return 15*math.sin(k)**3
      def heartb(k):
            return 12*math.cos(k)-5*\
                     math.cos(2*k)-2*\
                     math.cos(3*k)-\
                     math.cos(4*k)
      turt.speed(10)
      turt.bgcolor("black")
      for i in range(500):
            turt.goto(hearta(i)*20,heartb(i)*20)
            turt.color("purple")
            for j in range(5):
                  turt.color("purple")
            turt.goto(0,0)
      
      turt.color("white")
      turt.write("I love you Khloe" , move=True,align='Center',font=('Comic Sans',15,'bold'))
      turt.hideturtle()
      turt.done()

def flower():
      turt.speed(0)
      turt.bgcolor("black")
      h = 0
      for i in range(16):
            for j in range(18):
                  c = colorsys.hsv_to_rgb(h, 1, 1)
                  turt.color(c)
                  h += 0.005
                  turt.rt(90)
                  turt.circle(150 - j * 6, 90)
                  turt.lt(90)
                  turt.circle(150 - j * 6, 90)
                  turt.rt(180)
            turt.circle(40, 24)
      turt.color("white")
      turt.done()

