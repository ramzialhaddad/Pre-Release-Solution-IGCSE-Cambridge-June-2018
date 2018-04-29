#Re-Commented and Polished by Ramzi Al Haddad
#Original coder - Mr. Thornton

# Pre-Release 0478-22 June 2018: Program to record the milk yield of a herd of cows

# Task 1
# Declare variables

cowCode = 0 # 1 CowID
cowCodes = [] # All the CowIDs
herd = int(input("Please enter the size of the herd: ")) # This line asks the user for the size of the herd and wraps it in the int() so it ensures that its a integer
milkYield = []
total = 0
anotherCow = True # This needs to stay True to loop at line 35. Its called anotherCow because in the loop, every loop is another cow being milked
dailyLog = [] # This is an array/list used as a ledger to ensure only 2 milkings per day
weeklyLog = [] # The order of cowCode will correspond to the order in the milk_yeild list 
cowTotals = [] #This is used to store the total milking volume for each cow at the end of the week
cowDay=[] #This stores values to show if a cow has been milked that day or not, this is used for Task 3
maxYield = 0
maxCode = 0

# This is the for loop to record the CowIDs
for count in range(herd): # This for loop only loops in accordance to the herd size
    cowDay.append(0)# This adds a place holder 0 in the list
    cowTotals.append(0)# This adds a place holder 0 in the list
    cowCode = input("Enter the three digit code of cow: ") # This asks the user for the cow code
    while((len(cowCode)!=3) or (cowCode in cowCodes) or (cowCode.isalpha())): # This loop only loops if | the length of the cow code is not 3 OR it has already been entered OR has letters| if even one of those conditions is true the it will execute the loop
        cowCode = input("Code must be unique and 3 digits! ") # This asks the user for the cow code because the one entered previously was invalid
    cowCodes.append(cowCode) # The cow code has been validated and is now being added to the the cowCodes list
print("All herd cowCodes now entered!") # Alerts the user that all the herd cowCodes are entered
                          
# Begin the Milking
for day in range(7): # This only loops for 7 days, 1 week as said in the pre-release
    dailyLog.clear() # This is ensures that there is only 2 milkings per day
    print("Day "+str(day+1)+" of Milking!") # Alerts the user which day of milking it is, it adds one because arrays and computers count from 0
    while(anotherCow): # This is the variable used from line 14 and allows the loop to actually loop
        cowCode = input("Enter code of cow to be milked: ") # This line asks the user for the cow code
        while((len(cowCode)!=3) or (cowCode not in cowCodes) or (cowCode.isalpha())): # Same validation as in line 27
            print("Code entered wrong or not our cow!") # Alerts the user that the code was invalid
            cowCode = input("Enter cow code: ") # Re-Prompts the user to enter the code
        if(dailyLog.count(cowCode) == 2): # Checks the daily log list, if the cow has been milked twice already
            print("Cow already milked twice today!") # Prompts the user that the cow has been milked twice
        elif(dailyLog.count(cowCode) == 1): # Otherwise if it has only been milked once
            milk = float(input("How many litres? ")) # Prompts the user to enter the volume collected
            milkYield.append(milk) # Adds the volume of Milk to the milkYield list
            weeklLog.append(cowCode) # Adds the Cow Code to the weeklyLog list
            dailyLog.append(cowCode) # Adds the Cow Code to the dailyLog list  
        else: # Otherwise if its not 1 or 2 then its 0 milks, so lets fill the first one in
            milk = float(input("How many litres? ")) # Prompts the user for the milk volume
            milkYield.append(milk) # Adds the volume of Milk to the milkYield list
            weeklyLog.append(cowCode) # Adds the cowCode to the weeklyLog list
            dailyLog.append(cowCode) # Adds the cowCode to the dailyLog list
            for i in range(herd): # Repeats the loop as many times as the size of the herd
                if(cowCodes[i] == cowCode): # Searches for the cowCode in cowCodes
                    cowDay[i] = cowDay[i]+1 # This list counts up the number of days a cow has been milked
        answer = input("Any more cows to be milked today(y/n)?")# Prompts the user if anymore cows have to be milked
        if(answer.lower() == "n"): # if the answer.lower() which lowercases it is equal to n then it will break out of the while loop
            break # This breaks out of the while loop and goes to line 60

# Find the weekly total for each cow, and the max
for i in range(len(cowCodes)): # Repeats the loop in correspondance to the length of the cowCodes list
    for x in range(len(milkYield)): # Repeats the loop in correspondance to the length of the milkYield list
        if(cowCodes[i] == weeklyLog[x]): # If the cowCode found in the member of cowCodes is the same as the cowCode in weeklyLog
            cowTotals[i] = cowTotals[i] + milkYield[x] # Adds the current cowTotal and milkYield volumes together and overwrites the previous value 
    if(cowTotals[i] > maxYield): # If the cowTotal member in i is greater than the current maxYield then..
        maxYield = cowTotals[i] # Change maxYield to the cowTotal
        maxCode = cowCodes[i] # And save the index vlaue of it
    if((cowTotals[i]<12) and (cowDay[i]>3)): # Flag up cows with less than 12 litres for 4 days or more
        print("Cow code "+ str(cowCodes[i]) +" only yielded "+ str(cowTotals[i]) +" litres over "+ str(cowDay[i]) +" days.") # This prompts the user about any cows that have produced less than 12 liters of milk for 4 days or more
    total = total + cowTotals[i] # Adds the total milked volume of the herd to the current total for cow i

print ("The total yield is "+str(total)+" litres of milk") # Alerts the user of the total volume of milk produced for the week for the herd
print ("The average yield per cow is "+str(total/herd)+" litres of milk") # Shows the user of the average milk produced with each cow of the herd
print ("Your best cow is "+str(maxCode)+" with a yield of "+str(maxYield)+" litres") # Shows the highest yeilding cowCode and the actual yield of it.






"""

The code works fine, I did remove some parts because they were reduntant even now alot is still redunant but this is 1 way of doing it. You don't have to be so picky with values
and error check because the actual document doesn't ask for any of that. You can either make something janky and get A* or do something nice and also get A* your choice.
This was just to help with people finding it a bit hard to understand the code. This solution was provided in Miss Watson's Google Classroom with the original code written
by Mr. Thornton. This also may be updated, so if you want you can go to my GitHub to find the latest version if you want. If you want any more bits better explained then 
you can find me I guess or email me or put an issue on GitHub if you want idk you decide.

GitHub: https://github.com/ramzialhaddadtm/Pre-Release-Solution-IGCSE-Cambridge-June-2018

"""