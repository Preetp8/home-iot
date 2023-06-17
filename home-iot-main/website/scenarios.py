import psycopg2
from . import calculations
#from calculations import *

# scenarios
def showerScenario():
    cnxn = psycopg2.connect(
        database = "Team1DB",
        user = "Team1",
        password = "team1",
        host = "138.26.48.83",
        port = '5432'
    )
    cursor = cnxn.cursor()

    lastRow = "SELECT * FROM usage ORDER BY id DESC LIMIT 1"
    cursor.execute(lastRow)
    imgonnakms = cursor.fetchall()
    #print("Last Row: ", imgonnakms)

    usage = calculations.showerEvent()
    #usage = showerEvent()
    #print("nums to add: ", usage)
    water_usage = usage[0]
    water_cost = usage[1]
    elec_usage = usage[2]
    elec_cost = usage[3]

    query = "UPDATE usage SET water = water + %s, cost_of_water = cost_of_water + %s, electricity = electricity + %s, cost_of_electricity = cost_of_electricity + %s WHERE date = (SELECT MAX(date) FROM usage)"

    cursor.execute(query, (water_usage, water_cost, elec_usage, elec_cost))

    #lastRow = "SELECT * FROM usage ORDER BY id DESC LIMIT 1"
    cursor.execute(lastRow)
    imgonnakms = cursor.fetchall()

    cnxn.commit()

    #print ("SHOWER!!!!!", imgonnakms)

    return None




def dishwasherScenario():
    cnxn = psycopg2.connect(
        database = "Team1DB",
        user = "Team1",
        password = "team1",
        host = "138.26.48.83",
        port = '5432'
    )
    cursor = cnxn.cursor()



    lastRow = "SELECT * FROM usage ORDER BY id DESC LIMIT 1"
    cursor.execute(lastRow)
    imgonnakms = cursor.fetchall()
    #print("last row: ",imgonnakms)



    usage = calculations.dishwasherEvent()
    #usage = dishwasherEvent()
    #print("nums to add: ",usage)
    water_usage = usage[0]
    water_cost = usage[1]
    elec_usage = usage[2]
    elec_cost = usage[3]

    query = "UPDATE usage SET water = water + %s, cost_of_water = cost_of_water + %s, electricity = electricity + %s, cost_of_electricity = cost_of_electricity + %s WHERE date = (SELECT MAX(date) FROM usage)"

    cursor.execute(query, (water_usage, water_cost, elec_usage, elec_cost))

    cnxn.commit()
    cursor.execute(lastRow)

    imgonnakms = cursor.fetchall()
    #print ("DISHWASHER!!!!", imgonnakms)
    return None

#print(showerScenario(), dishwasherScenario())