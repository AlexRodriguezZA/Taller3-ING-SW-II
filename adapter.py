#*--------------------------------------------------
#* adapter.py
#* excerpt from https://refactoring.guru/design-patterns/adapter/python/example
#*--------------------------------------------------

class Target:
    """
    El destino define la interfaz específica del dominio utilizada por el código del cliente.
    """

    def request(self) -> str:
        return "Objetivo: el comportamiento del objetivo predeterminado."


class Adaptee:
    """
    El Adaptee contiene algunos comportamientos útiles, pero su interfaz es incompatible
    con el código de cliente existente. El Adaptado necesita alguna adaptación antes de que el
    el código del cliente puede usarlo.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    El adaptador hace que la interfaz del Adaptee sea compatible con la del Target
    Interfaz a través de herencia múltiple.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    El código del cliente admite todas las clases que siguen la interfaz de Target.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Cliente: puedo trabajar bien con los objetos de destino:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: La clase Adaptee tiene una interfaz rara."
          "Mira, no lo entiendo:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Cliente: Pero puedo trabajar con él a través del Adaptador:")
    adapter = Adapter()
    client_code(adapter)
