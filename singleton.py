#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
class SingletonMeta(type):
    """
    La clase Singleton se puede implementar de diferentes maneras en Python. Algunos
    los métodos posibles incluyen: clase base, decorador, metaclase. Usaremos el
    metaclase porque es la más adecuada para este propósito.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finalmente, cualquier singleton debe definir alguna lógica comercial, que puede ser
        ejecutado en su instancia.
        """

        # ...
    def getid(self):
        return "miIDunico"

if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton funciona, ambas variables contienen la misma instancia.")
        print(s1.getid())
    else:
        print("Singleton falló, las variables contienen diferentes instancias.")


