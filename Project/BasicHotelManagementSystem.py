#A Simple Rock Paper Scissor Game
import random
print "Rock, Per Scissor Game"
print "Welcome, Pal"
print " Choose one of the option"
print "1 Rock"
print "2 Paper"
print "3 Scissor"
z=0
pointplayer=0
pointpc=0
for i in range(1,6):
    x=raw_input("Enter One Of The Option: - ")
    if x=="1":
        thegame1=["Paper","Scissor"]
        c=random.choice(thegame1)
        if c=="Paper":
            print "Your Option is Rock"
            print "Computer's gives Paper"
            print "So You Loose Hard Luck"
            pointpc+=1
        else:
            print "Your Option is Rock"
            print "Computer's gives Scissor"
            print "So You Win Congratultion!!!"
            pointplayer+=1
    elif x=="2":
        thegame2=["Rock","Scissor"]
        c=random.choice(thegame2)
        if c=="Rock":
            print "Your Option is Paper"
            print "Computer's gives Rock"
            print "So You Win Congratualation!!!"
            pointplayer+=1
        else:
            print "Your Option is Paper"
            print "COmputer's gives Scissor"
            print "So You Loose HArd Luck"
            pointpc+=1
    elif x=="3":
        thegame=["Rock","Paper"]
        c=random.choice(thegame)
        if c=="Paper":
            print "Your Option is Scissor"
            print "Computer's gives Paper"
            print "So You Win Congratualation!!!"
            pointplayer+=1
        else:
            print "Your Option is Scissor"
            print "Computer's gives Rock"
            print "So You Loose Hard Luck"
            pointpc+=1
    else:
        print "INcalid Option"
        i=i-1
        continue
print "Your Score",pointplayer
print "Computer Score", pointpc
if pointpc>pointplayer:
    print "Computer wins the Game with Point Difference", pointpc-pointplayer
else:
    print"You Win The Game With Point Difference",pointplayer-pointpc
    
        
        
