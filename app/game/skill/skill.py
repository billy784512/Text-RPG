from abc import ABC, abstractmethod

class Skill(ABC):
    
    @abstractmethod
    def use(self, user, target):
        pass
    
    @abstractmethod
    def desc(self):
        pass

