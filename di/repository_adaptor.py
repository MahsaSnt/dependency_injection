from abc import ABC, abstractmethod


class AbstractRepositoryAdaptor(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def insert(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get(self, *args, **kwargs):
        raise NotImplementedError


class RepositoryAdaptor1(AbstractRepositoryAdaptor):
    def insert(self, *args, **kwargs):
        print(f'inserted in {self.model} by repository 1')

    def get(self, *args, **kwargs):
        print(f'loaded from {self.model} by repository 1')


class RepositoryAdaptor2(AbstractRepositoryAdaptor):
    def insert(self, *args, **kwargs):
        print(f'inserted in {self.model} by repository 2')

    def get(self, *args, **kwargs):
        print(f'loaded from {self.model} by repository 2')
