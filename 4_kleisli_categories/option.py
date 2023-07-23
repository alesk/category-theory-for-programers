from abc import abstractmethod, ABC
from typing import Callable, Optional, TypeVar, Generic

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")

PartialFunction = Callable[[A], Optional[B]]


class Option(Generic[A], ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def get(self) -> A:
        pass


class Empty(Option[A]):
    def is_empty(self) -> bool:
        return True

    def get(self) -> A:
        raise Exception("Could not get value of Empty")

    def __repr__(self) -> str:
        return "Empty()"


class Some(Option[A]):
    def __init__(self, value: A):
        self.value = value

    def is_empty(self) -> bool:
        return False

    def get(self) -> A:
        return self.value

    def __repr__(self) -> str:
        return f"Some({self.value})"


# identity
def identity(x: A) -> Option[A]:
    return Some(x)


# composition
def compose(f: Callable[[B], C], g: Callable[[A], B]) -> Callable[[A], C]:


    def fn(x: A) -> C:
        y = f(x)
        return Empty() if y.is_empty() else g(y.get())

    return fn

def safe_root(x: float) -> Option[float]:
    return Some(x ** 0.5) if x >= 0 else Empty()

def safe_reciprocal(x: float) -> Option[float]:
    return Some(1 / x) if x != 0 else Empty()
def main():
    composed = compose(safe_root, safe_reciprocal)
    print(f'composed(2) = {composed(2)}')
    print(f'composed(0) = {composed(0)}')
    print(f'composed(-1) = {composed(-1)}')

if __name__ == "__main__":
    main()