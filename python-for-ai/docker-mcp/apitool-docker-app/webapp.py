from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the main SPA page"""
    return render_template("index.html")


@app.route("/static/<path:path>")
def send_static(path):
    """Serve static files"""
    return send_from_directory("static", path)


if __name__ == "__main__":
    import configsettings

    app.run(
        host=configsettings.IP_ADDRESS,
        port=8080,  # Flask on different port than FastAPI
        ssl_context=(configsettings.SSL_CERTFILE, configsettings.SSL_KEYFILE),
    )
