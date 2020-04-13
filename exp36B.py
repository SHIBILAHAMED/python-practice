print ("welcome to the game ")

print ("""
  _________________________
  |                        |
  |HOME ___________________|
  |____________________    |
  |   _____________________|   _______
  |__________     _________|   |      |
  |_________________________   |OFFICE|
                               |______|

""")

print ("find the way to home")
print ("give the direction in a order to reach home, use l for left, r for right, m for middle turn, u for upward(seperated by space), E for exiting the game ")

#input_key=input(">>>>")
l=[]
l.extend(input(">>>"))

if l =="E":
    print ("CLOSING THE GAME")
    exit()
else:
    print ("YOUR ANSWER IS {}".format(l))
    game_key=["m"," ","u"," " ,"l"," " ,"r"]

    if l==game_key:
        print ("MISSION PASSED")
        exit()
    else:
        print ("MISSION FAILED")
        exit()

