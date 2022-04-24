#!/usr/python
#*--------------------------------------------------
#* abstractfactory.py
#* excerpt from https://refactoring.guru/design-patterns/abstractfactory/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    La interfaz de Abstract Factory declara un conjunto de métodos que devuelven
    diferentes productos abstractos. Estos productos se denominan familia y son
    relacionados por un tema o concepto de alto nivel. Los productos de una familia suelen ser
    capaces de colaborar entre ellos. Una familia de productos puede tener varios
    variantes, pero los productos de una variante son incompatibles con los productos de
    otro.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Las Fábricas de Concreto producen una familia de productos que pertenecen a un solo
    variante. La fábrica garantiza que los productos resultantes son compatibles. Nota
    que las firmas de los métodos de Concrete Factory devuelven un resumen
    producto, mientras que dentro del método se instancia un producto concreto.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Cada Concrete Factory tiene una variante de producto correspondiente.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Cada producto distinto de una familia de productos debe tener una interfaz base. Todos
    las variantes del producto deben implementar esta interfaz.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Los Productos de Concreto son creados por las Fábricas de Concreto correspondientes.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
    Aquí está la interfaz base de otro producto. Todos los productos pueden interactuar
    entre sí, pero la interacción adecuada sólo es posible entre productos de
    la misma variante concreta.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        El producto B es capaz de hacer lo suyo...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...pero también puede colaborar con el ProductoA.

        The Abstract Factory se asegura de que todos los productos que crea sean de la
        misma variante y por lo tanto, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    La variante, Producto B1, solo puede funcionar correctamente con la variante,
    Producto A1. Sin embargo, acepta cualquier instancia de AbstractProductA como un
    argumento.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
    La variante, Producto B2, solo puede funcionar correctamente con el
        variante, Producto A2. Sin embargo, acepta cualquier instancia de
        AbstractProductA como argumento.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    """
    El código de cliente funciona con fábricas y productos solo a través de resumen.
    tipos: AbstractFactory y AbstractProduct. Esto le permite pasar cualquier fábrica
    o subclase de producto al código del cliente sin romperlo.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    El código del cliente puede funcionar con cualquier clase de fábrica concreta.
    """
    print("Cliente: Prueba de código de cliente con el primer tipo de fábrica:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Cliente: probando el mismo código de cliente con el segundo tipo de fábrica:")
    client_code(ConcreteFactory2())

