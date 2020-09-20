import matplotlib.pyplot as plt 
from datetime import datetime, timedelta

"""

This is the section that the user needs to fill out to get accurate results. 

"""

age = 19 #Current age
emit = 16 #How much CO2 emited per year in metric tons.
newTrees = 60 #How many trees are being planted per year
UsersName = "Thrasher" #The users name
numYears = 50 #How many years you will be donating
numYearsStillAlive = 30 #How many additional years to simulate (after you stop donating)
numYearsAfterDonations = 50 #How many years after your death to simulate the trees
currentTrees = 0 #How many trees you're planting or have already planted (Generally 0)

"""

DISCLAIMER:

The numbers I used here are based on a lot of research. The values in particular that I am reffering
to are: Tree Death Rate, Carbon absorption rate per tree per year, time to mature. I spent hours to 
find these values. Once I had decided on the values I chose (As seen directly below this section of
text), I reached out to the Arbor Day Foundation to confirm and they agreed with my research. I plan
to put the conversation in the github repo for reference.

ABOUT THE ARBOR DAY FOUNDATION:

The Arbor Day Foundation is a nonprofit conservation and educational foundation. They are the 
largest nonprofit membership organization that is dedicated to planting trees [2]. They were also
the organization behind #TeamTrees, who along side the hundreds of large YouTubers that set the 
goal of planting 20,000,000 trees. As of writing, they have raised over $22,000,000. Each dollar
donated was another tree planted. Team Trees is where I recommend donating to plant your trees 
seeing as how it is very affordable. Current rate is $1 = 1 tree. Go to https://www.teamtrees.org 
to donate.


ADDITIONAL SOURCES:

[1] Average American emits 16 metric tons per year SOURCE: https://www.nature.org/en-us/get-involved/how-to-help/carbon-footprint-calculator/#:~:text=The%20average%20carbon%20footprint%20for,under%202%20tons%20by%202050.
[2] Arbor Day Foundation: https://www.arborday.org/generalinfo/about.cfm#:~:text=Founded%20in%201972%20%E2%80%94%20the%20centennial,organization%20dedicated%20to%20planting%20trees.

"""

#Aspects of the average tree
deathRate = .97
absRate = .021 #Absorption rate in Metric Tons
timeToMature = 5

#Get the current year
now = datetime.now()
year = int(now.strftime("%Y"))

#Misc Starting values
carbonFootPrint = 0

#Creates the lists that will manage
yearsCarbon = []
yearsTime = []
yearsNumTrees = []


#Calculates carbon footprint already caused
carbonFootPrint += emit * age
yearsCarbon.append(carbonFootPrint)
yearsTime.append(year)
yearsNumTrees.append(0)

print("Your starting Carbon Footprint is " , carbonFootPrint)

tempTime = 1 #A throwaway variable to track which cycle the following loop is in

#This accounts for the years in which the trees are growing and not mature, thus not being counted
for nonYear in range(year, year + timeToMature):

    #print(carbonFootPrint)
    carbonFootPrint += emit 

    yearsCarbon.append(carbonFootPrint) 
    yearsTime.append(year+tempTime)
    tempTime += 1


print("Carbon footprint by the time the first trees mature: ", carbonFootPrint)

#This Calculates for the amount of time that trees are being donated
for thisYear in range(year + timeToMature,(year + numYears)):
    
    #carbonFootPrint
    carbonFootPrint += emit
    
    #Plant trees 
    currentTrees += newTrees
    
    #kill trees 
    currentTrees = int(currentTrees * deathRate)

    #Absorb
    carbonFootPrint -= (currentTrees * absRate)
    
    thisStat = "In Year: "+ str(thisYear)+ "--------- Carbon Footprint: "+ str(round(carbonFootPrint, 2)) + " Metric tons of CO2 with " + str(currentTrees) + " trees alive"
    print(thisStat)

    yearsCarbon.append(carbonFootPrint)
    yearsTime.append(thisYear)


#This tracks after trees have stopped being donated but the person is still alive
for thisYear in range(year + numYears,(year + numYears +numYearsStillAlive)):
    print("Is called")

    #carbonFootPrint
    carbonFootPrint += emit
    
    #kill trees 
    currentTrees = int(currentTrees * deathRate)

    #Absorb carbon
    carbonFootPrint -= (currentTrees * absRate)
    
    thisStat = "In Year: "+ str(thisYear)+ "--------- Carbon Footprint: "+ str(round(carbonFootPrint, 2)) + " Metric tons of CO2 with " + str(currentTrees) + " trees alive"
    print(thisStat)

    yearsCarbon.append(carbonFootPrint)
    yearsTime.append(thisYear)

#This tracks the tree's effects after the person dies / stops polluting
for thisYear in range(year + numYearsStillAlive + numYears,(year + numYears + numYearsStillAlive + numYearsAfterDonations)):

    
    #kill trees 
    currentTrees = int(currentTrees * deathRate)

    #Absorb Carbon
    carbonFootPrint -= (currentTrees * absRate)
    
    thisStat = "In Year: "+ str(thisYear)+ "--------- Carbon Footprint: "+ str(round(carbonFootPrint, 2)) + " Metric tons of CO2 with " + str(currentTrees) + " trees alive"
    print(thisStat)

    yearsCarbon.append(carbonFootPrint)
    yearsTime.append(thisYear)


#Builds the graph using matplotlib for carbon footprint
plt.ylabel("Carbon footprint (in metric tons)")
plt.xlabel("Year")
plt.axhline(y=0.5, color='black', linestyle='-')
plt.plot(yearsTime, yearsCarbon)
titleStr = str(UsersName) + "'s Carbon Footprint graph if he plants " + str(newTrees) + " trees every year for " + str(numYears) + " years"
fontdict = {"fontsize": 10}
plt.title(titleStr, fontdict)
plt.show()

