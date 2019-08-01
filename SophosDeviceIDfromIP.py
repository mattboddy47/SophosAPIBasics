import requests

class SophosIDfromIP:
    def __init__(self, url, xapikey, Authorization, IPAddress):
        self.url = url + '/migration-tool/v1/endpoints'
        self.xapikey = xapikey
        self.Authorization = Authorization
        self.IPAddress = IPAddress

    def RetrieveID(self):
        h = {'x-api-key': self.xapikey,
           'Authorization': self.Authorization}
        r = requests.get(self.url, headers=h)
        devicesDict = dict()
        if r.status_code == 200:
            responseJSON = r.json()
            for item in responseJSON['items']:
                for ip in item['info']['ipAddresses/ipv4']:
                    devicesDict[ip] = item['id']
        else:
            print('The request failed with status code ', r.status_code)

        searchResult = devicesDict.get(self.IPAddress)
        print(searchResult)


if __name__ == "__main__":
    #input your URL , x-api-key, authorization (starting with Basic) and the IP address which you'd like to search for in the below brackets
    idFromIp = SophosIDfromIP('URL', 'x-api-key',
                      'authorization',
                          'search ip')
    idFromIp.RetrieveID()
