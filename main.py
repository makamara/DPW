"""+++++++++++++MADLIB+++++++++++++++++++++++++++++
NAME:    MOHAMED A. KAMARA
PROJECT: WEEK 1 - MADLIB
COURSE:  DWP
++++++++++++++++++++++++++++++++++++++++++++++"""

print "ANSWER EVERY QUESTION HONESTLY...."
sport = raw_input("What's your favorite sport?")   # Input for favorite sport
actor =raw_input("Who's your icon actor?")  # Input for favorite actor
rapper = raw_input("Who's your childhood rapper?")  # Input field for childhood' rapper
birthyear =input("What year were you born?")  # Full year required to calculate age
grad = input("What year did you graduate high school?")  # High school graduation year required.
firstdate = input("What year you had first date?")  # Input field for for year of first date in numeric value
teams = ["Vikings","Timberwolves", "Twins"]  # An array of teams
mvp={"Golden": "Curey", "Cavaliers": "LeBron", "Lakers": "Kobe"}  # a dictionary of teams and players
print "MVP 2015 is : ", mvp["Golden"]  # select the value of golden state and corresponding value
numb1 = input("Enter and number 0 - 10 : ")  # Input field for first number 0-10
numb2 = input("Enter another number 0 -10: ")  # Input field for second number
print "Sum of 2 numbers: " + (numb1+numb2)  # Find the sum of numb1 and numb2
print "Product of 2 numbers: " + (numb1 * numb2)  # Find the product of numb1 and numb2
if numb1>numb2:  # conditional statement that compares numb1 and numb2
    print "First number is greater than 2nd number"  # prints numb1 if greater than numb2
else:
    print "Second number is greater than 1st number." # prints numb2 if greater than numb1
print sport + " has always been my favorite game since childhood. And I love watching movies starring " + str(actor)
print "Since the death of ZGang, " + str(rapper) + " has been my best rapper in the game. And being someone of the " + \
      birthyear + "s, I love such genre of songs. Even before leaving high school in " + grad + ", I had already " \
      "gone on first date during the summer of " + firstdate + " during the " + teams[1] + " pre-season games. I" \
       "couldn't believe too that " + mvp["Golden"] + " became MVP in few years."
print "End of the Madlib game......"

