from dependency_injection import DI, DI1, DI2
from database_adaptor import DatabaseAdaptor1
from repository_adaptor import RepositoryAdaptor1


@DI1.params
def connect_insert_get_disconnect(database_adaptor, repository_adaptor):
    database_adaptor.connect()
    repository_adaptor.insert()
    repository_adaptor.get()
    database_adaptor.disconnect()


@DI2.params
def connect_disconnect(database_adaptor, repository_adaptor):
    database_adaptor.connect()
    database_adaptor.disconnect()


if __name__ == '__main__':
    print('----------- di params for model 1 ------------')
    connect_insert_get_disconnect()
    print('\n')
    print('----------- di params for database 2 ------------')
    connect_disconnect()
    print('\n')
    print('----------- di injection ------------')
    di = DI.injection()
    print('type of DI.injection: ', type(di))
    print('\n')
    print('----------- di bind ------------')
    di.bind(DatabaseAdaptor1, RepositoryAdaptor1)
    print('DI.database_adaptor: ', di.database_adaptor)
    print('DI.repository_adaptor: ', di.repository_adaptor)
    print('\n')
    di.clear()
    print('----------- di clear------------')
    print('DI.database_adaptor: ', di.database_adaptor)
    print('DI.repository_adaptor: ', di.repository_adaptor)


