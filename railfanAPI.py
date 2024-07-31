from bottle import Bottle, run
from Routers import train
from Helpers.config import HOST, PORT

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
    print(f"Listening on http://{HOST}:{PORT}/")

    app = Bottle()
    app.mount('/train', train.app)

    run(app, host=HOST, port=PORT, quiet=True)