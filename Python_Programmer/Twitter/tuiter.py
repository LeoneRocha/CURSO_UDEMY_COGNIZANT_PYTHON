import twitter


print('OI')

api = twitter.Api(consumer_key=' ',
                      consumer_secret=' ',
                      access_token_key=' - ',
                      access_token_secret=' ')


print(api.VerifyCredentials())
#{"id": 16133, "location": "Philadelphia", "name": "bear"}