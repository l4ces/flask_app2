import os
from flask import Flask, render_template, request
import yelp_api
app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('address') # read the address from the HTTP request params
	recommendations = None # we need to declare & initialize the variable before referencing.
	# check to see if address was specified
	if address: 
		recommendations = yelp_api.get_businesses(address)
	return render_template('index.html', recommendations=recommendations)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)