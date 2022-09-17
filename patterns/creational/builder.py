from abc import ABC, abstractmethod
from typing import List


class AbstractBuilder(object):

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def create_part_a(self):
        pass

    @abstractmethod
    def create_part_b(self):
        pass


class Product(object):
    parts: List[str] = []

    def add(self, part: str) -> None:
        self.parts.append(part)


class Builder(AbstractBuilder):
    _product: Product

    def __init__(self):
        self._product = Product()

    @property
    def product(self) -> Product:

        product = self._product
        self._product = Product()
        return product

    def _create_part_a(self) -> None:
        self._product.add('part a')

    def _create_part_b(self) -> None:
        self._product.add('part b')

    def create_test_product(self) -> None:
        self._create_part_a()
        self._create_part_b()


