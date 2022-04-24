from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    La clase abstracta define un método de plantilla que contiene un esqueleto de
    algún algoritmo, compuesto de llamadas a (generalmente) primitivas abstractas
    operaciones.

    Las subclases concretas deberían implementar estas operaciones, pero dejar el
    método de plantilla en sí intacto.  
    """

    def template_method(self) -> None:
        """
        El método de plantilla define el esqueleto de un algoritmo.
        """

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # Estas operaciones ya tienen implementaciones.

    def base_operation1(self) -> None:
        print("AbstractClass dice: Estoy haciendo la mayor parte del trabajo")

    def base_operation2(self) -> None:
        print("AbstractClass dice: Pero dejo que las subclases anulen algunas operaciones")

    def base_operation3(self) -> None:
        print("AbstractClass dice: Pero estoy haciendo la mayor parte del trabajo de todos modos")

    # Estas operaciones deben implementarse en subclases.

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    # Estos son "ganchos". Las subclases pueden anularlas, pero no es obligatorio
    # ya que los ganchos ya tienen una implementación predeterminada (pero vacía). Manos
    # proporcionar puntos de extensión adicionales en algunos lugares cruciales del
    #algoritmo.

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    Las clases concretas tienen que implementar todas las operaciones abstractas de la base.
    clase. También pueden anular algunas operaciones con una implementación predeterminada.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    """
    Por lo general, las clases concretas anulan solo una fracción de la clase base.
    operaciones.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


def client_code(abstract_class: AbstractClass) -> None:
    """
El código del cliente llama al método de plantilla para ejecutar el algoritmo. Cliente
    código no tiene que saber la clase concreta de un objeto con el que trabaja, como
    siempre que trabaje con objetos a través de la interfaz de su clase base.
    """

    # ...
    abstract_class.template_method()
    # ...


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
    print("\n")
