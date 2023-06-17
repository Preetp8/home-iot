import psycopg2
import calculations


cnxn = psycopg2.connect(
        database = "Team1DB",
        user = "Team1",
        password = "team1",
        host = "138.26.48.83",
        port = '5432'
    )
cursor = cnxn.cursor()

# to clear data 
# cursor.execute("DELETE FROM usage")

# too see whats in table
# cursor.execute("SELECT water, cost_of_water, electricity, cost_of_electricity FROM usage")

# add values to the database
# usage = calculations.showerEvent()
# water_usage = usage[0]
# elec_usage = usage[1]
# water_cost = usage[2]
# elec_cost = usage[3]



# query = "UPDATE usage SET water = %s, cost_of_water = %s, electricity = %s, cost_of_electricity = %s WHERE date = (SELECT MAX(date) FROM usage)"
# cursor.execute(query, (water_usage, elec_usage, water_cost, elec_cost))


cursor.execute("SELECT water, cost_of_water, electricity, cost_of_electricity FROM usage")



rows = cursor.fetchall()
water = [row[0] for row in rows]
cost_of_water = [row[1] for row in rows]
electricity = [row[2] for row in rows]
cost_of_electricity = [row[3] for row in rows]
total_cost = []

for i in range(0, len(cost_of_electricity)):
    total_cost.append (round(cost_of_electricity[i] + cost_of_water[i],2))

print(water)
print(cost_of_water)
print(electricity)
print(cost_of_electricity)


# print(total_cost)