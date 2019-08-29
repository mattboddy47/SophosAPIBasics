import requests
import csv
import datetime
import time

class CreateEndpointReport:
    def __init__(self, url, xapikey, Authorization):
        self.url = url + '/migration-tool/v1/endpoints'
        self.xapikey = xapikey
        self.Authorization = Authorization

    def generateCSV(self):
        h = {'x-api-key': self.xapikey,
           'Authorization': self.Authorization}
        r = requests.get(self.url, headers=h)
        with open('EndpointReport'+time.strftime("%Y%m%d-%H%M%S")+'.csv', 'w', newline='') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow(["COMPUTER NAME", "IP ADDRESSES",
                                    "OPERATING SYSTEM", "LAST SUCCESSFUL UPDATE",
                                    "LAST MESSAGE FROM ENDPOINT","NOT UP TO DATE",
                                    "LAST LOGGED ON USER", "ENCRYPTION STATUS"])
            if r.status_code == 200:
                responseJSON = r.json()
                for item in responseJSON['items']:
                    computerName = item['info']['computer_name']
                    lastUser = item['info']['last_logged_on_user']
                    encryptionStatus = item['status']['denc/encryption_status']
                    
                    try:
                        LastSuccessfulUpdate = item['status']['alc/last_successful_update']
                        LastSuccessfulUpdate = str(LastSuccessfulUpdate)
                        LastSuccessfulUpdate = int(str(LastSuccessfulUpdate)[:-3])
                        LastSuccessfulUpdate = str(datetime.date.fromtimestamp(LastSuccessfulUpdate))
                    except:
                        LastSuccessfulUpdate = "Not available"
                    try:
                        LastMessageTime = item['last_activity']
                        LastMessageTime = str(LastMessageTime)[:-14]
                    except:
                        LastMessageTime = "Not available"
                    try:
                        isOutOfDate = item['status']['alc/alerted_out_of_date']
                    except:
                        isOutOfDate = "Not available"
                    OS = item['info']['osName']
                    IPs = ""
                    for ip in item['info']['ipAddresses/ipv4']:
                        IPs += ip + " "
                    newFileWriter.writerow([computerName, IPs, OS, LastSuccessfulUpdate,
                                            LastMessageTime, isOutOfDate, lastUser, encryptionStatus])
            else:
                print('The request failed with status code ', r.status_code)

        
        


if __name__ == "__main__":
    #input your URL , x-api-key, authorization (starting with Basic) in the below brackets
    CreateReport = CreateEndpointReport('URL', 'x-api-key',
                      'basic auth')
    
    CreateReport.generateCSV()
