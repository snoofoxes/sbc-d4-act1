from random import choice #insted nga randint, gipili nako ang choice para direct nga string ang pilion

def players(P1, C2, C3):#function para hinlo ang code
    if P1 not in ["Hayang", "Kulob"]: #e validate nako kung ang word is "Hayang" or "Kulob" then kung dle mo exit siya gamit ang return
        print("Wrong Input!")
        return

    if P1 == C2 == C3: # e comparison kung niya kung same sila then pag True, e print niya ang "Draw"!
        print("Draw")
    elif P1 == C2: # e comparison niya kung si P1 ug C2 kay same value then ang daug si C3
        print("The winner is C3")
    elif C2 == C3: # e comparison niya kung si C2 ug C3 kay same value then ang daug si P1
        print("The winner is P1")
    elif C3 == P1: # e comparison niya kung si C3 ug P1 kay same value then ang daug si C2
        print("The winner is C2")
    else:
        ...

P1 = input("Enter 'Hayang' or 'Kulob': ").capitalize() # Dri mo input si user then e capitalize dayun kung iyang gi input is naka Upper or Lower
C2 = choice(["Hayang", "Kulob"]) #auto generated ang pag pili ni C2 gamit ang function na choice same kay C3
C3 = choice(["Hayang", "Kulob"])
players(P1, C2, C3)#gi gamit nako ang function then dri e print ang Winner
print(f"P1 = {P1}\nC2 = {C2}\nC3 = {C3}\n")#gi print nako ang gigunitan nila ang value