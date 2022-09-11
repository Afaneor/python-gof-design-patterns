import abc
from logging import getLogger

logger = getLogger(__name__)


class AbstractPastry(abc.ABC):

    @abc.abstractmethod
    def some_logic(self):
        pass


class Pastry(AbstractPastry):

    def some_logic(self):
        logger.info('some logic')


class AbstractBake(abc.ABC):

    @abc.abstractmethod
    def create_pastry(self) -> AbstractPastry:
        pass


class Bake(AbstractBake):

    def create_pastry(self) -> Pastry:
        return Pastry()


class CustomBake(AbstractBake):

    def create_pastry(self) -> Pastry:
        pastry = Pastry()
        logger.info('some custom logic')
        return pastry
