Print "Welcome to my Game"
sport = raw_input("What's your favorite sport?")
actor =raw_input("Who's your favorite actor?")
rapper = raw_input("Who's your childhood rapper?")
birthyear =raw_input("What year were you born?")
grad = raw_input("What year did you graduate high school?")
firstdate = raw_input("What year you had first date?")
teams = ["Vikings","Timberwolves", "Twins"]
mvp =dict()
mvp={"Golden":"Steve Curey", "Cavaliers":"LeBron", "Lakers":"Kobe"}
print "MVP 2015 is : ", mvp["Golden"]
numb1 = raw_input("Enter 1st number: ")
numb2 = raw_input("Enter 2nd number: ")
print "Sum of 2 numbers: " + str(numb1+numb2)
print "Product of 2 numbers: " + str(numb1 * numb2)
#conditional statements
if numb1>numb2:
    print "First number is greater than 2nd number"
else:
    print "Second number is greater than 1st number."
print sport +" has always been my favorite game since childhood. And I love watching movies starring " + str(actor)
print "Since the death of ZGang, " + str(rapper) +" has been my best rapper in the game. And being someone of the "
print birthyear + ", I have varies of genre."
