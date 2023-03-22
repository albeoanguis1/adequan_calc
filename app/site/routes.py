from flask import Blueprint, render_template, request
from math import ceil
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/calculate', methods=['GET', 'POST'])
def calculate_days_supply():
    initial_dose = request.form.get('input-initial-dose')
    frequency = request.form.get('input-frequency')
    
    if not initial_dose or not frequency:
        # one or both inputs are blank, so just return the template
        return render_template('index.html')
    
    initial_dose = float(initial_dose)
    print(f'Inital Dose: {initial_dose} mL(s)')
    frequency = float(frequency)
    print(f'Frequency: {frequency}/week')
    
    total_amount = 2 * 5 # total amount in 1 box
    amount_per_week = initial_dose * frequency
    weeks_supply_per_box = total_amount / amount_per_week 
    boxes_needed = ceil(4/weeks_supply_per_box)

    result = f'You need {boxes_needed} boxes to cover the month.'

    return render_template('index.html' ,  result=result)

@site.route('/day_supply', methods=['GET', 'POST'])
def calculate_supply():
    quantity = request.form.get('input-quantity')
    dose = request.form.get('input-dose')
    frequency = request.form.get('input-frequency2')

    if not quantity or not dose or not frequency:
            # one or both inputs are blank, so just return the template
            return render_template('day_supply.html')

    quantity = float(quantity)
    dose = float(dose)
    frequency = float(frequency)

    daily_tabs = dose * frequency
    days_supply = quantity / daily_tabs
    result =  f'You medication will last {days_supply} days'


    return render_template('day_supply.html', result=result)