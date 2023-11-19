import sqlite3

class Database:
    def __init__(self, path):
        self.path = path
        self.connection = None
        self.connected = False
        self.connect()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.path)
            self.connected = True
        except sqlite3.Error as e:
            print(e)
        return self.connection

    def commit(self):
        if self.connection:
            self.connection.commit()
        else:
            print("No active connection to commit.")

    def close(self):
        if self.connected:
            self.connection.close()
            self.connected = False
