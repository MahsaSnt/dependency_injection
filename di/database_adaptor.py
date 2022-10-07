from abc import ABC, abstractmethod


class AbstractDatabaseAdaptor(ABC):
    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError


class DatabaseAdaptor1(AbstractDatabaseAdaptor):
    def connect(self):
        print("connected to database_1")

    def disconnect(self):
        print("disconnected from database_1")

    def __str__(self):
        return "database adaptor 1"


class DatabaseAdaptor2(AbstractDatabaseAdaptor):
    def connect(self):
        print("connected to database_2")

    def disconnect(self):
        print("disconnected from database_2")

    def __str__(self):
        return "database adaptor 2"
