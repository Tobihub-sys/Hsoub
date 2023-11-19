from Database import Database

class Model:
    db = None

    def __init__(self):
        self._create_table()
        self._saved = False

    @classmethod
    def _get_table_name(cls):
        return cls.__name__.lower()

    @classmethod
    def get_columns(cls):
        columns = {}
        for key, value in cls.__dict__.items():
            if str(key).startswith('_'):
                continue
            columns[str(key)] = str(value)
        return columns

    def _create_table(self):
        if not Model.db:
            raise ValueError("You need to set Model.db with a valid Database instance.")
        
        columns = ', '.join(f'{key} {value}' for key, value in self.get_columns().items())
        sql = f'CREATE TABLE IF NOT EXISTS {self._get_table_name()} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})'
        cursor = Model.db.connection.cursor()
        result = cursor.execute(sql)
        return result
