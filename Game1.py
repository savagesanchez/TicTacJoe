
print ("TIC TAC JOE")
print ("Its been stolen!! After years of trying to perfect it, you finally made it! But now it has been stolen! the perfect cup of coffee...")
print ("You have tracked the smell to the shed in the backyard. Time to get back what is rightfully yours. Many dangers await... but its worth it... for JOE")
ready = input("Are you ready?")
def start():
        if ready == "yes":
                return begin()
        elif ready != "yes" :
                print ("you coward, you dont deserve any joe")
        end
        
def begin():
        print ("You open the door to your backyard, and staring you in the face is your first threat... the notorious tabby cat!!")
        print ("there is only one way to settle this... TIC TAC TOE! Tabby has challenged you!")
        tabby = input("Do you accept?")
        if tabby == "yes":
                print ("tictac")
                return second()
        else :
                print  ("You scared of a little cat? You dont deserve coffee")
        end
def second():
        print ("you have defeated the tabby cat! and your quest continues.")
        print ("As you proceed on your journey you reach the pond...floating in it is your son")
        print ("HE CHALLENGES YOU TO TIC TAC TOE!")
        print ('"I should have given him up for adoption" you mutter') 
        son = input("do you accept the challenge?")
        if son == "yes":
                print ("tictac")
                return final()
        else :
                print ("your son is now your dad")
        end
def final():
        print ("You beat your son! (theoretically)")
        print ("You finally approachthe last boss... whatever is in the shed. What could it be... a monster? a dragon? cthulu?")
        print ("You open the shed... and gasp in horror as you see what monster stole your precious coffee.IT WAS YOUR WIFE! ")
        print ("Time to get back what is rightfullu yours")
        print ("Your wife has challenged you to TIC TAC TOE!!")
        wife = input("DO YOU ACCEPT??")
        if wife == "yes":
               print ("tictac")
        else :
               print ("You watch in horror as she drinks the coffee...")
               print (" 'ew its cold' ")
        end
start()
#A code by Alvaro Sanchez
