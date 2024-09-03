import logging

from src import create_app

logging.basicConfig(filename='activity.log', level=logging.DEBUG)
app = create_app()

if __name__ == "__main__":
    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=8000, debug=True)
    #app.run(port=8000)
