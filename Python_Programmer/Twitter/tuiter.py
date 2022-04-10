import twitter


print('OI')

api = twitter.Api(consumer_key='i0f7boTc8E6A4ljkWAKWl3kNL',
                      consumer_secret='7zbCyggNaMLUrnsD579zSh9qZWp2uAFJNQREPGUuispCRdkdzF',
                      access_token_key='1451993523390226439-dYVJ8ENrfnHm50Gt5hYr8drGqv8qGn',
                      access_token_secret='NOyCptinQ0bhbwg3YD8HkrHEbUMzelZnAj7j4qQ1NFKiC')


print(api.VerifyCredentials())
#{"id": 16133, "location": "Philadelphia", "name": "bear"}