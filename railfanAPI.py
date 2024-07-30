from bottle import Bottle, run
from Routers import train

if __name__ == '__main__':
    print('''                                                                 
               ,--.,--.                             ,---.  ,------. ,--. 
,--.--. ,--,--.`--'|  |,--.   ,--. ,--,--.,--. ,--./  O  \ |  .--. '|  | 
|  .--'' ,-.  |,--.|  ||  |.'.|  |' ,-.  | \  '  /|  .-.  ||  '--' ||  | 
|  |   \ '-'  ||  ||  ||   .'.   |\ '-'  |  \   ' |  | |  ||  | --' |  | 
`--'    `--`--'`--'`--''--'   '--' `--`--'.-'  /  `--' `--'`--'     `--' 
                                          `---'                          
''')
    print("railfanAPI V0.1.0 Beta")
    print("Github：https://github.com/AZ-Studio-2023/railfanAPI")

    app = Bottle()
    app.mount('/train', train.app)

    run(app, host='localhost', port=8080)