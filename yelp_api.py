from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# put these into environment variables so protect them.
#def get_businesses (location, term):
def get_businesses (location):    
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ.get('TOKEN_SECRET')
    )

    client = Client(auth)

    #params['term'] = search_term
    params = {
        'term': 'food',
        'lang': 'en',
        'limit': 3
    }

    response = client.search(location, **params)

    # create an empty list named businesses
    businesses = []

    # add things to it.
    for business in response.businesses:
        #businesses.append(business.name)
        # returning a dictionary of business fields in a list
        businesses.append({"name": business.name, "rating": business.rating, 'phone': business.phone})
    return businesses


# Main 
#loc = input("\nEnter address\n\t")
#search_term = input ("\nEnter a category\n\t")
#businesses = get_businesses(loc, search_term)
#businesses = get_businesses('New York City', 'food')
#print (businesses)
