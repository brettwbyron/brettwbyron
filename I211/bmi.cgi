#! /usr/bin/env python
print 'Content-type: text/html\n'

import cgi

html = """
<html>
    <head><title>BMI - Calculator</title></head>
    <body>

"""

form = cgi.FieldStorage()

try:
	fields = ""
	weight = float(form.getfirst('weight', 'error'))
	feet = int(form.getfirst('height_ft', 'error'))
	inches = float(form.getfirst('height_in', 'error'))
	height = (feet*12)+inches
	bmi = (weight*703)/(height*height)

	if bmi < 15:
		category = "Very severely underweight"
	if bmi >= 15 and bmi < 16:
		category = "Severely underweight"
	if bmi >= 16 and bmi < 18.5:
		category = "Underweight"
	if bmi >= 18.5 and bmi < 25:
		category = "Normal (healthy weight)"
	if bmi >= 25 and bmi < 30:
		category = "Overweight"
	if bmi >= 30 and bmi < 35:
		category = "Obese Class I (Moderately obese)"
	if bmi >= 35 and bmi < 40:
		category = "Obese Class II (Severely obese)"
	if bmi > 40:
		category = "Obese Class III (Very severely obese)"
	
	html += "<p>Your weight is " + str(weight) + "lbs</p>"
	html += "<p>Your height is " + str(feet) + " feet " + str(inches) + " inches</p>"
	html += "<p>Your BMI is " + str(bmi) + "</p>"
	html += "<p>BMI Category: " + str(category) + "</p>"
	html += "</body></html>"

	print html
except:
	html += "<p>Can't convert to number.</p>"
	html += "</body></html>"
	print html