import bottle
from bottle import Bottle
import requests
from Helpers.ipHelper import ip

app = Bottle()


@app.route("/info")
def train_info():
    if ip(bottle.request):
        date = bottle.request.query.date
        train = bottle.request.query.train
        if date == "" or train == "":
            return {"code": 100, "msg": "参数不完整"}
        params = {"date": str(date), "trainNumber": str(train), "pageIndex": 1, "pageSize": 15}
        try:
            data = requests.post("https://rail.moefactory.com/api/trainNumber/query", data=params).json()
        except:
            return {"code": 101, "msg": "服务异常"}
        try:
            if data["code"] != 200:
                return {"code": 101, "msg": "服务异常"}
        except KeyError:
            return {"code": 101, "msg": "服务异常"}
        try:
            data = data["data"]["data"][0]
        except:
            return {"code": 102, "msg": "未查询到信息"}
        if data["crType"] == 0:
            cr = False
        else:
            cr = True
        return {"code": 200, "data": {"train": data["trainNumber"], "beginStation": data["beginStationName"],
                                      "departureTime": data["departureTime"], "endStation": data["endStationName"],
                                      "arrivalTime": data["arrivalTime"], "last": data["durationMinutes"],
                                      "distance": data["distance"], "trainType": data["trainType"], "isCR": cr}}
    else:
        return {"code": 403}


# 动车组交路
@app.route("/emu")
def t_emu():
    if ip(bottle.request):
        keyword = bottle.request.query.keyword
        try:
            d = requests.get("https://api.rail.re/train/{}".format(keyword)).json()
        except:
            return {"code": 101, "msg": "服务异常"}
        return {"code": 200, "data": d}
    else:
        return {"code": 403}
