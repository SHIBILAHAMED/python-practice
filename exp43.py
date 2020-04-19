from sys import exit
from random import randint
from textwrap import dedent


class scene(object):
    
    def enter(self):
        print ("this scene is not yet configured.")
        print ("subclass it and implement enter ().")
        exit(1)


class engine (object):
  
    def __init__(self,scene_map):
            self.scene_map = scene_map
         #   print("class engine ...scene map--",scene_map)# giving reference to class map
            

    def play(self):
        
        current_scene = self.scene_map.opening_scene()
        last_scene= self.scene_map.next_scene('finished')

        while current_scene!= last_scene:

            next_scene_name= current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()
        
            

class Death(scene):

    quips = [
        " You died. You kinda suck at this.",
        "your mom would be proud..if she were smater.",
        "such  a luser.",
        "i have a small puppy that's better at this .",
        "you're worse than your Dad's jokes."
    ]

    def enter(self):

        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)
        
class CentralCoridor(scene):

    def enter(self):
        print(dedent("""The Gothons of Plant Parcal #25 have invaded your strip and destroyed your entire crew. You are the last surviving member and your last mission is to get the neutron dstruct bomb from the weapons armory, put it in the bridge, and blow the ship up after geting into an escape pod.

        You're running down the central corridor to the Weapons armory whena Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume the flowing around his hate filled body. He's blocking the door to the armory and about to pull a weapon to blast you."""))

        action = input(">>>")
        if action =="shoot!":
            print (dedent("""Quick on the draw you yankout your blaster and fire it at the Gothon. His clown costume is flowing and moving around his body,which throws off your aim. Your laser hits costume but misses him entirely. This completely ruins his brand new costume his mother bought him, which makes him fly into an suume rage and blast you repeatedly in the face untill you are dead. Then he eats you.
"""))
            return 'death'

        elif action =="dodge!":
                              print(dedent("""
            Like a world class boxer you dodge,weave,slip and slide right as the Gothan's blatter cranks a laser past your head. In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your head and eats you."""))
                              return "death."
        elif action =="tell a joke":
                                   print(dedent(""" Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothan joke you know: Lbhe zbgure vf fb sng, jur fur fvgf nebhaq gur ubhfr, fur fvgf neghaq gur ubhfr. The Gothon stops, tries not to laugh,then busts out laughing and can't move. While he's laughing you run up and shoot him square in the head putting him down, then jump through the Wepon armory door."""))
                                   return "laser_weapon_armory"
        else:
            print("Does not compute!")
            return "central_corridor"
                  
                  
                  
class Laserweapon(scene):

    def enter(self):

        print(dedent(""" You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hidding. It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container. There's  a keypad lock in the box and you need the code to get the bomb out. If you get the code wrong 10 times then the lockcloses forever and you can't get the bomb. The code is 3 digits."""))

        code =f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]>>>>")
        guesses =0
                  
        while guess != code and guesses<10:
              print("BZZZZZEDDD!")
              guesses+=1
              guess=input("[keypad]>")

        if guess == code:
              print(dedent("""
              The container clicks open and the seal breaks,letting gas out. You grab the neutron bomb and run as fast as you can to the bridge where you must place itin the right spot."""))
              return "the_bridge"
        else:
            print (dedent("""
            The lock buzzesone last time and then you hear a sickening melting sound as the mechanism is fused together. YOu decide to sit there, and finally the Gothons blow up the ship from their ship and you die."""))

            return "death"
                  
                  


class TheBridge(scene):

     def enter(self):
            print(dedent("""You burst onto the Bridge with the netron destruct bomb under your arm and surpise 5 Gothons who are trying to take control of the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet, as they see the active bomb under your arm and dont want to set it off.
"""))
            action= input (">>>>")

            if action == "throw the bomb":
                  print(dedent("""
In a panic you throw the bomb at the group of Gothons nd make a leap for the door. Right as you drop it a Gothon shoot you right in the bck killing ypu. As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probbly blow up when it goes off."""))
                  return "death"
            elif action == "slowly place the bomb":

                  print (dedent(""" You point your blaster at the bomb under your arm and the Gothon put their hands up start to sweat. You inch backwrd to the door,open it, and then carefully place the bomb onthe door, punch the close button and blast the lock so the Gothons can't get out.Now that the bomb is placed you run to the escape pod to get off this tin can."""))
                  return"excape pod"
            else:

                  print("Does not compute!")
                  return "the_bridge"
                  


class EscapePod(scene):

    def enter(self):
        print(dedent("""
        You rush through the shio desperately trying to make it to the escape pod before the whole ship explodes. It seems likehardly any Gothon are on the ship, so your run is clear of interference. You get to the chamber with the escape pods,and now need to pick one to take. Some of them could be damaged but you dont have time to look. There's 5 pods,which one do you take?"""))
        good_pad=randint(1,5)
        guess = input("[pod#]>")

        if int(guess)!= good_pod:
            print (dedent(""" 
            You jump into pod{guess} nd hit the eject button. The pod escapes out into space, then impoldes as  the hull ruptures, crushing your body intojam jelly"""))
            return "death"
        else:

            print (dedent("""You jump into pod{guess}nd hit the eject button. The pod easily slides out into space heaidng tothe planet below.As it files to the planet, yoou look back and see your ship implode then explode like a bright star, taking out the Gothon ship at at the same tume. You Won !"""))
            return "finished "

                  
class Finished(scene):

        def enter(self):

                print ("You won! Good job.")
                return "finished"
                  
          


class Map(scene):

    scenes = {"central_corridor": CentralCoridor(),
              "laser_weapon_armory": Laserweapon(),
              "the_bridge":TheBridge(),
              "excape_pod":EscapePod(),
              "death":Death(),
              "finished":Finished(),}

    def __init__(self,start_scene):
            self.start_scene = start_scene
          #  print("map class start_scence ",start_scene)
                  

    def next_scene(self,scene_name):
            val =Map.scenes.get(scene_name)
           # print ("self.next_scene@@@@@ printing val values",self.next_scene,"val is ",val)
          #  print("scene_name of class map",scene_name)## here scene_name central coridor
            
            return val
                  
    def opening_scene(self):
          #  print("class map ..opening_scene...self.start_scene",self.start_scene)  #so self.start_scene== central_corridor
            return self.next_scene(self.start_scene)

a_map=Map('central_corridor')#given a_map as start_scene
a_game= engine(a_map)#given an object to class engine named start_scene
a_game.play()
