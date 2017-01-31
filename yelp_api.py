from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# put these into environment variables so protect them.
# location: address
# term: A search term.
# limit: The number of items to return atmost.
def get_businesses (location, term, limit):    
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ.get('TOKEN_SECRET')
    )

    client = Client(auth)

    
    params = {
        'term': term,
        'lang': 'en',
        'limit': limit
    }

    response = client.search(location, **params)

    # create an empty list named businesses
    businesses = []

    # add things to it.
    for business in response.businesses:
        businesses.append({"name": business.name, "address": business.location.display_address, "rating": business.rating, 'phone': business.display_phone})
    return businesses


