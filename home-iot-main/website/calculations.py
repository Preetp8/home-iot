import random


def HVAC(internal, external, ideal, windowTime, doorTime):
    time = 0 #likely need to keep this in the db too
    while (internal >= ideal + 2 or internal <= ideal - 2): #not within ideal range
        if internal < external:
            internal += 1
            time += 1
        elif external < internal:
            internal -= 1
            time += 1
        if abs(internal-external) > 10:
            if internal < external:
                if windowTime > 0:
                    for i in range(windowTime):
                        internal += 1/5
                elif doorTime > 0:
                    for i in range(doorTime):
                        internal += 1/5
                internal += 1/30
            elif external < internal:
                if windowTime > 0:
                    for i in range(windowTime):
                        internal -= 1/5
                elif doorTime > 0:
                    for i in range(doorTime):
                        internal -= 1/5
                internal -= 1/30  
        else:
            break;
    return time




def totalEnergyWD(): #in kWh
    num = 0
    light = .060 * 24 #assuming its always on
    fan = .030 * 24 
    hvac = 3.500 * HVAC(75, 90, 70, 0, 0)
    fridge = .150 * 24
    microwave = 1.100 * (20/60)

    #hot water using appliances
    waterHeater = 4.500 
    shower = (25 * 0.65) * (4/60) * waterHeater #2 of these a day
    bath = (30 * 0.65) * (4/60) * waterHeater #2 of these a day
    clothesWasher = ((20 * 0.85) * (4/60) * waterHeater)+ (.500 * 30/60) #only on some days, 4x a week
    dishWasher = 1.800 * (45/60) * waterHeater #only on some days, 4x a week

    clothesDryer = 3.000 * (30/60) #only on some days, 4x a week
    stove = 3.500 * (15/60)
    oven = 4.000 * (45/60)
    tvLR = .636 * (4/60)
    tvBR = .100 * (2/60)

    num = light + fan + hvac + fridge + microwave + random.randint(0,4)*shower + random.randint(0,4)*bath + stove + oven + tvBR + tvLR + clothesDryer + clothesWasher + dishWasher

    return (num/10)
def energyCostWD(): #$ from kwh
    #num = totalEnergyinWD() * 0.12 
    
    light = .060 * 24 * 0.12 #assuming its always on
    fan = .030 * 24 * 0.12 
    hvac = 3.500 * HVAC(75, 90, 70, 0, 0) * 0.12 
    fridge = .150 * 24 * 0.12 
    microwave = 1.100 * (20/60) * 0.12 

    #hot water using appliances
    waterHeater = 4.500 * 0.12 
    shower = (25 * 0.65) * (4/60) * waterHeater * 0.12 #2 of these a day
    bath = (30 * 0.65) * (4/60) * waterHeater * 0.12 #2 of these a day
    clothesWasher = (((20 * 0.85) * (4/60) * waterHeater)+ (.500 * 30/60)) * 0.12 #only on some days, 4x a week
    dishWasher = 1.800 * (45/60) * waterHeater * 0.12 #only on some days, 4x a week

    clothesDryer = 3.000 * (30/60) * 0.12 #only on some days, 4x a week
    stove = 3.500 * (15/60) * 0.12 
    oven = 4.000 * (45/60) * 0.12 
    tvLR = .636 * (4/60) * 0.12 
    tvBR = .100 * (2/60) * 0.12 

    num = light + fan + hvac + fridge + microwave + random.randint(0,4)*shower + random.randint(0,4)*bath + stove + oven + tvBR + tvLR + clothesDryer + clothesWasher + dishWasher
    return (num) 

def totalGallonsWD(): #gallons
    shower = 25
    bath = 30
    dishWasher = 6 #only on some days, 4x a week
    clothesWasher = 20 #only on some days, 4x a week

    num = random.randint(0,4)*shower + random.randint(0,4)*bath + clothesWasher + dishWasher
    return (num/100)
def waterCostWD(): #gallons
    shower = 25
    bath = 30
    dishWasher = 6 #only on some days, 4x a week
    clothesWasher = 20 #only on some days, 4x a week

    num = (random.randint(0,4)*shower + random.randint(0,4)*bath + clothesWasher + dishWasher) / 748 * 2.52
    return (num)

def totalCost():
   return  waterCostWD() + energyCostWD()


#test scenarios
def showerEvent():
    #increase gallons, electricity, and cost: 25 gal, 65% hot water, 35% cold water
    addThese = []
    gallons = 25/100
    addThese.append(gallons)
    gallons *= 100  

    showerWaterCost = round((gallons / 748 * 2.52),2)
    addThese.append(showerWaterCost)

    waterHeaterE = 4.500 #energy
    waterHeaterC = 4.500 * 0.12 #cost
    showerEnergy = round(((25 * 0.65) * (4/60) * waterHeaterE)/10,2)
    addThese.append(showerEnergy)

    showerElecCost = round((showerEnergy*10 * 0.12), 2)
    addThese.append(showerElecCost)
    

    # totalCost = showerElecCost + showerWaterCost
    # addThese.append(totalCost)
    return addThese #this is a list that we can hopefully add to our data or something


def dishwasherEvent():
    #increase gallons, electricity, and cost: 1800 watts, 6 gal hot water, 45 min
    addThese = []
    gallons = 6/100
    addThese.append(gallons)
    gallons*=100

    dwWaterCost = round((gallons / 748 * 2.52),2)
    addThese.append(dwWaterCost)

    waterHeaterE = 4.500 #energy
    waterHeaterC = 4.500 * 0.12 #cost
    dwEnergy = round(((1.800 * (4/60) * waterHeaterE)/10),2)
    addThese.append(dwEnergy)

    dwElecCost = round((dwEnergy*10 * 0.12),2)
    addThese.append(dwElecCost)
    
    # totalCost = dwElecCost + dwWaterCost
    # addThese.append(totalCost)
    return addThese


if(__name__=="__main__"):
        print(showerEvent())
        print("----------")
        print(dishwasherEvent())
        print("----------------")

        print("Total energy in kW for one weekday is: " + str(round(totalEnergyWD(), 2)))
        print("Total cost of energy for one weekday is: $" + str(round(energyCostWD(), 2)))
        print("Total energy in kW for one month is: " + str(round(totalEnergyWD()*30, 2)))
        print("Total cost of energy for one month is: $" + str(round(energyCostWD()*30, 2)))
        
        print("------------------")
        print("Total gallons of water for one weekday is: " + str(round(totalGallonsWD(), 2)))
        print("Total cost of water for one weekday is: $" + str(round(waterCostWD(), 2)))
        print("Total gallons of water for one month is: " + str(round(totalGallonsWD()*30, 2)))
        print("Total cost of water for one month is: $" + str(round(waterCostWD()*30, 2)))