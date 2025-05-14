class freeDB:
    def __init__(self):
        self._database_list = []
        self._active_database = None

    def createDatabase(self, database_name):
        pass

    def dropDatabase(self, database_name):
        pass

    def use(self, database_name):
        pass


class Database:
    def __init__(self, name):
        self._name = name

    def createTable(self, table_name):
        pass

    def dropTable(self, table_name):
        pass