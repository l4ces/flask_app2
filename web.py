import os
from flask import Flask, render_template, request
import yelp_api
app = Flask(__name__)

@app.route("/")
def index():
	# I tried exception handling and still did not figure out how to avoid the 404. To get around
	# absence of a paramter, the index.html page uses default values.
	address = request.values.get('address') # read the address from the HTTP request params
	term = request.values.get('term')
	limit = request.values.get('limit')
	recommendations = None 

	# check to see if address was specified
	if address: 
		recommendations = yelp_api.get_businesses(address, term, limit)
	return render_template('index.html', address=address, recommendations=recommendations, term=term)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)