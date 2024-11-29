from flask import Flask, request
from config import Config
from webhookhandler import WebHookHandler

config = Config()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    whh = WebHookHandler(request, config)
    return whh.run()


if __name__ == '__main__':
    app.run(
        host=config.host,
        port=config.port
    )
