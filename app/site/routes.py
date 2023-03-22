from flask import Blueprint, render_template, request
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
    max_days_supply = 56 # maximum days supply with 1 box
    days_supply = total_amount / (initial_dose * frequency) #to get the weeks

    if days_supply > max_days_supply:
        boxes_needed = days_supply / max_days_supply #how many boxes to cover the days supply
        result = f"Days supply exceeds maximum. You would need {boxes_needed} box(es) to cover the days supply."
        print(result)        
    else:
        result = days_supply * 7
        print(result)



    return render_template('index.html' ,  result=result)