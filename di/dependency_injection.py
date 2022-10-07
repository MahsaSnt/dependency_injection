from database_adaptor import DatabaseAdaptor1, DatabaseAdaptor2
from repository_adaptor import RepositoryAdaptor1, RepositoryAdaptor2


class DI:
    database_adaptor = None
    repository_adaptor = None

    @classmethod
    def bind(cls, database_adaptor, repository_adaptor):
        cls.database_adaptor = database_adaptor
        cls.repository_adaptor = repository_adaptor

    @classmethod
    def injection(cls):
        return cls.__new__(cls)

    @classmethod
    def clear(cls):
        cls.database_adaptor = None
        cls.repository_adaptor = None

    @classmethod
    def params(cls, func):
        def wrapper(*args, **kwargs):
            func(cls.database_adaptor, cls.repository_adaptor, *args, **kwargs)
        return wrapper


class DI1(DI):
    database_adaptor = DatabaseAdaptor1()
    repository_adaptor = RepositoryAdaptor1('model_1')


class DI2(DI):
    database_adaptor = DatabaseAdaptor2()
    repository_adaptor = RepositoryAdaptor2('model_2')
