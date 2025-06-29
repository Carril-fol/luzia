from database.db import Database

def start_server(app):
    database = Database()
    database.initialize()

    app.run()