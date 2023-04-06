from pynput.mouse import Button, Controller
#from pynput.keyboard import Key, Controller
import time
def test():
 while True:
     mouse = Controller()
    # Read pointer position
     print('The current pointer position is {0}'.format(
       mouse.position))
     time.sleep(1)
def test1():
  mouse = Controller()
  x = 230
  n = 0 
  for i in range(0,3):
   while True:
    mouse.position = (1174, x)
    x+=70
    #mouse.press(Button.left)
    #mouse.release(Button.left)
    time.sleep(1)
    n+=1
    o = 0
    n1 = 0
    o1 = 0
    if n %27 == 0:
      while True:
         mouse.position = (1594, 853)
         mouse.press(Button.left)
         mouse.release(Button.left)
         time.sleep(1)
         if n1 == 5:
           pass
         n1 +=1
         if o1 == 5:
           break

    if n %9 == 0:
     while True:
      mouse.position = (1594, 853)
      mouse.press(Button.left)
      mouse.release(Button.left)
      o+=1
      time.sleep(1)
      if o == 17:
        x =  230
        break
    if n == 35:
       break

     
test1()

  