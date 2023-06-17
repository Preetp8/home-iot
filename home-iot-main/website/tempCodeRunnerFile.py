 currentDate!=date(2023,5,1):
# 	print(currentDate)
# 	# cursor_obj.execute(f"INSERT INTO usage (water, cost_of_water, electricity, cost_of_electricity, date) VALUES ({round(water*uniform(0.9,1.1))}, {round(waterCost*uniform(0.9,1.1))}, {round(energy*uniform(0.9,1.1))}, {round(energyCost*uniform(0.8,1.2))}, \'{str(currentDate)}\')")
# 	# cursor_obj.execute(f"INSERT INTO usage (water, cost_of_water, electricity, cost_of_electricity, date) VALUES ({(water) * 0}, {(waterCost) * 0}, {(energy) * 0}, {(energyCost)*0}, \'{str(currentDate)}\')")
# 	# cursor_obj.execute(f"INSERT INTO usage (water, cost_of_water, electricity, cost_of_electricity, date) VALUES ({water}, {waterCost}, {energy}, {energyCost}, \'{str(currentDate)}\')")
# 	currentDate+=timedelta(days=1)