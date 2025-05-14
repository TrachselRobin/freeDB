from commands.create import *
from commands.delete import *
from commands.read import *
from commands.update import *

class freeDB:
    def __init__(self):
        self._database_list = []
        self._active_database = None

    def createDatabase(self, database_name):
        """
        create a new database

        :param database_name:
        :return:
        """
        pass

    def dropDatabase(self, database_name):
        """
        delete the database

        :param database_name:
        :return:
        """
        pass

    def use(self, database_name):
        """
        To switch to the database

        :param database_name:
        :return:
        """
        pass


class Database:
    def __init__(self, name):
        self._name = name

    # functions