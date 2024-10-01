from bottle import Bottle, run
from Routers import train, emu
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
    print("Github：https://github.com/AZ-Studio-2023/GoRailing.API")
    print(f"Listening on http://{HOST}:{PORT}/")

    app = Bottle()
    app.mount('/train', train.app)
    app.mount('/emu', emu.app)

    run(app, host=HOST, port=PORT, quiet=True)