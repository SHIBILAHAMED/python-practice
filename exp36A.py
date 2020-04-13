print (""" MULTIPLICATION TABLE BETWEEN 1 & 1OO""")
print ("enter the which number multiplication table what display")

num=int(input(">>>>"))

while num!=0:
    
    table=range(0,100,num)
    list=['multiplication table of - {}'.format(num)]
    list.extend(table)
    print (list)
    exit()

if num==0:
    print("dont know how to type a number")

exit()
