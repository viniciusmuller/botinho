from abc import ABC, abstractmethod

class IRepository(ABC):
    """
    """
    @abstractmethod
    async def create(self): pass

    @abstractmethod
    async def find(self): pass

    @abstractmethod
    async def update(self): pass

    @abstractmethod
    async def delete(self): pass
