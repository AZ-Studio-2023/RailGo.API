import bottle
from bottle import Bottle
import requests
from bs4 import BeautifulSoup

app = Bottle()


@app.route("/model")
def emu_info():
    model = bottle.request.query.model
    pageNumber = bottle.request.query.page
    try:
        url = f'https://emu.passearch.info/index.php?type=model&keyword={model}&pagenum={pageNumber}'  # 将此替换为实际 URL
        response = requests.get(url)
    except:
        return {"code": 101, "msg": "服务异常"}
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    rows = soup.find_all('tr')

    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        if len(cols) >= 6:
            data.append(cols[:6])
    return {"code": 200, "data": data}