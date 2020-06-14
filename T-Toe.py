import random

def main():

  Boardarray = [[" "," " ," " ],\
                [" ", " ", " "],\
                [" ", " ", " "]]

  PlacerX = "x"
  PlacerO = "o"
  Counter = 0
  gameover = False

  while (Counter < 9) or (gameover is not True):
    Draw(Boardarray)
    Placer(Boardarray)
    AI(Boardarray)
    gameover = Checker(Boardarray)
    Counter += 1

def Checker(x):

  def ChkRow(a):
    for i in range(0, len(a)):
      if (a[i][0] is not " "):
        if (a[i][0] == a[i][1]) and (a[i][0] == a[i][2]):
          return True
    return False
   return ChkRow(x, y)


def AI(x):

  turnover = False
  while (turnover == False):
    a = random.randint(0, 2)
    y = random.randint(0, 2)
    if (x[a][y] == " "):
      x[a][y] = "o"
      turnover = True
      

   

def Placer(x):

  #if (y == 0):
  cordX = input("enter a \"x\" coordinate: ")
  cordY = input("enter a \"y\" coordinate: ")
  if (cordX <= 2 and cordY <= 2) and (cordX >= 0 and cordY >= 0) and (x[cordX][cordY] == " "):
    x[cordX][cordY] = "x"
  else:
    print "Please enter new coordinates"

  

def Draw(x):

  counterX = 0
  counterY = 0

  print "\n", "  0", "  1", "  2"
  for i in range(0, 3):
    print i,
    for y in range(0, len(x[i])):
      print x[i][y], 
      if (y < 2):
        print "|",
    if (i < 2):
      print "\n", "  __________"
  print "\n"


if __name__ == '__main__':
  main()


