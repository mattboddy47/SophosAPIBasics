import requests

#within the url input both the Sophos Central url followed by the api call you want to make
#I provide the example of the endpoint information in the Central API
url = 'https://api3.central.sophos.com/gateway/migration-tool/v1/endpoints'
# add your API keys provided within Sophos Central here
headers = {'x-api-key': 'YOURAPIKEYHERE',
           'Authorization': 'YOURAUTHKEYHERE'}
#we pull the data from the API and store it within the variable r
r = requests.get(url, headers=headers)
#a simple if statement to make sure the request was succesful
if r.status_code == 200:
    #we convert the variable r to the format of JSON
    responseJSON = r.json()
    #since the response provides a nested JSON, I provide an example below of
    #itterating through the JSON to search for the unique IDs per item in Sophos Central
    #as well as the IPv4 addresses.
    for item in responseJSON['items']:
        print (item['id'])
        print (item['info']['ipAddresses/ipv4'])
else:
    #we print a failed message along with the status code if this request fails
    print('The request failed with status code ', r.status_code)

