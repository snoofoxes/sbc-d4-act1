from random import randint
#Swertress 
bet = (input("Enter your bet: ")) #ngayo siyag input ni user
result = str(randint(100,999))#auto generated ang value sa result gamit ang randint nga function
while len(bet) != len(result):#gi identify niya if isa ra ka number or 2 or more than 3 iyang gi input
    bet = (input("Enter your bet: "))#then pag nag True mangayo siya ug input utro
print(f"Result = {result}")#then e print ang winner numbers
if bet == result:#gi identify kung same sila ug value
    print("You Win!")# pag nag true e print niya nga "win"
elif sorted(bet) == sorted(result):#gi sort niya ang duha ka variable then e comparison kung same sila
    print("Partially Win")#pag nag true e print niya nga "partially win"
else: 
    print("You Loss!")#if dle mag true tong statement e print niya "you lose"