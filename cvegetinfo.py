import requests
import json
owntoken='e5bd0c7fabf44a38a58b09174449c12f'
url = "https://app.nokelock.com/nokelock_v3/order/myOrder"
strheader ={"token":owntoken,
            "User-Agent":"nokelock/5.3.2(Android 8.1.0 ; LGE/Nexus 5X)",
            "clientType":"Android",
            "uid":"273473",}
for userid in range(271077,271078):
    print(userid)
    strdata = {"uid":userid,"limit":10,"page":0,"status":0}
    jsondata = json.dumps(strdata)
    request = requests.post(url,data=jsondata,headers=strheader)
    respdata = request.text
    jsonresp = json.loads(respdata)
    jsonresult = jsonresp['result']
    for result in jsonresult:
        print("address and phone:"+result['address']+"price is:"+str(result['totalFee']/100))