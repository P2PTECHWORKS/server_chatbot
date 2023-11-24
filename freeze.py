from frozen_flask import Freezer
from server import app

app = Freezer(app)

if __name__ == '__main__':
    app.freeze()
