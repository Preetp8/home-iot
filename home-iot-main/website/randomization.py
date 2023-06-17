from random import uniform
import random
import psycopg2
from calculations import *
from datetime import date,timedelta
import datetime

connect = psycopg2.connect(
	database = "Team1DB",
	user = "Team1",
	password = "team1",
	host = "138.26.48.83",
	port = '5432'
)

cursor_obj = connect.cursor()


#currentDate = date(2023,1,1)


## Testing purposes
# print(energy)
# print(energyCost)
# print(water)
# print(waterCost)
# cursor_obj.execute("ALTER TABLE usage ALTER COLUMN water TYPE FLOAT")
# cursor_obj.execute("ALTER TABLE usage ALTER COLUMN cost_of_water TYPE FLOAT")
# cursor_obj.execute("ALTER TABLE usage ALTER COLUMN electricity TYPE FLOAT")
# cursor_obj.execute("ALTER TABLE usage ALTER COLUMN cost_of_electricity TYPE FLOAT")
cursor_obj.execute("DELETE FROM usage")

today = datetime.datetime.now()
todayDate = today.date()
dayNum = today.day
print(todayDate, dayNum)
twoMonAgo = todayDate - datetime.timedelta(days=60 + dayNum) 
print(twoMonAgo)

currentDate = twoMonAgo
counter = 1
while currentDate!=todayDate:
	
	water = round(totalGallonsWD(),2)
	waterCost = round(waterCostWD(),2)
	energy = round(totalEnergyWD(),2)
	energyCost = round(energyCostWD(),2)
	
	print(currentDate)
	print(water, waterCost, energy, energyCost)
	print(counter)

	cursor_obj.execute(f"INSERT INTO usage (water, cost_of_water, electricity, cost_of_electricity, date, id) VALUES ({water}, {waterCost}, {energy}, {energyCost}, \'{str(currentDate)}\', {counter})")
	currentDate+=timedelta(days=1)
	counter+= 1
	
connect.commit()

cursor_obj.close()
connect.close()