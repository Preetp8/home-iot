# standard roots go here


import random, datetime, psycopg2
# from calculations import showerEvent, dishwasherEvent
from . import scenarios
from flask import Blueprint, render_template, request, jsonify




views = Blueprint('views', __name__)

@views.route('/')
def home(): #function ran when gone to home route 
    return render_template("home.html")


@views.route('/data')
def data():
    thisMonth = [[],[],[]]
    prevMonth = [[],[],[]]
    twoMonths = [[],[],[]]
    predicted = [[],[],[]]
    null = [[],[],[]]
    base = [[],[],[]]


    cnxn = psycopg2.connect(
        database = "Team1DB",
        user = "Team1",
        password = "team1",
        host = "138.26.48.83",
        port = '5432'
    )
    cursor = cnxn.cursor()
    cursor.execute("SELECT water, cost_of_water, electricity, cost_of_electricity FROM usage")
    rows = cursor.fetchall()
    water = [row[0] for row in rows]
    cost_of_water = [row[1] for row in rows]
    electricity = [row[2] for row in rows]
    cost_of_electricity = [row[3] for row in rows]
    total_cost = []
    for i in range(0, len(cost_of_electricity)):
        total_cost.append (cost_of_electricity[i] + cost_of_water[i])

    #creates data for each month
    start = 0
    end = 30
    step = 30
    for i in range(start, end, step):
        x = i
        twoMonths[0] = water[x:x+step]
        twoMonths[1] = electricity[x:x+step]
        twoMonths[2] = total_cost[x:x+step]

        base[0] = water[x:x+step]
        base[1] = electricity[x:x+step]
        base[2] = total_cost[x:x+step]

    # prev month
    start += 30
    end += 30
    for i in range(start, end, step):
        x = i
        prevMonth[0] = water[x:x+step]
        prevMonth[1] = electricity[x:x+step]
        prevMonth[2] = total_cost[x:x+step]


    # this month
    # Get today's date
    today = datetime.datetime.now()
    daysinMonth = today.day

    # # Calculate the start and end dates for the current month
    start += 30
    end += daysinMonth
    step = daysinMonth

    # # Calculate the number of days in the current month
    # num_days = (end - start).days + 1

    # Create data for each day in the current month
    for i in range(start, end, step):
        x = i
        thisMonth[0] = water[x:x+step]
        thisMonth[1] = electricity[x:x+step]
        thisMonth[2] = total_cost[x:x+step]

        predicted[0] = water[x:x+step]
        predicted[1] = electricity[x:x+step]
        predicted[2] = total_cost[x:x+step]

    
    daysPredicted = 30 - daysinMonth
    predicted[0] += base[0][0:daysPredicted]
    predicted[1] += base[1][0:daysPredicted]
    predicted[2] += base[2][0:daysPredicted]

    datalist = [thisMonth, prevMonth, twoMonths, predicted, null]

    # return render_template("data.html", water=water, cost_of_water=cost_of_water, electricity=electricity, cost_of_electricity=cost_of_electricity )
    return render_template("data.html", datalist = datalist )

    

# Tests
    # energy_usage = [10, 20, 30, 40, 50, 60, 70]
    # water_usage = [20, 30, 40, 50, 60, 70, 80]
    # total_cost = [50, 60, 70, 80, 90, 100, 110]
    # return render_template("data.html", energy_usage=energy_usage, water_usage=water_usage, total_cost=total_cost)




@views.route('/controls')
def controls():


    return render_template("controls.html", showerScenario = scenarios.showerScenario, dishwasherScenario = scenarios.dishwasherScenario)

@views.route('/showerscenario')
def callShowerScenario():
    result = scenarios.showerScenario()
    return jsonify(result = result)

@views.route('/dwscenario')
def callDWScenario():
    result = scenarios.dishwasherScenario()
    return jsonify(result = result)

@views.route('/about')
def about(): 
    return render_template("about.html")

@views.route('/irritants')
def irritants(): 
    return render_template("irritants.html")