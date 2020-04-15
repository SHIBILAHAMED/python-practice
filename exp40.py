class S_ong(object):

    def __init__(self,lyrics):
       
         self.lyrics =lyrics
         #print ("self word in __init__",self)
         #print ("Lyrics word in __init__",lyrics)

    def sing_me_a_song(self):
        for i in self.lyrics:
            print (i)


happy_bday= S_ong(["Happy brithday to you",
"I dont want to get sued",
"So i'll stop right there"])

bulls_on_parade=S_ong(["they rally around tha family",
"with pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

            
