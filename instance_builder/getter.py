from typing import Callable, TypeVar
from .lib import find_attributes


T = TypeVar("T")


def getter(Class: type) -> type:
    def generate_getter(name: str) -> Callable[Class, T]:
        def get_value(self) -> T:
            return getattr(self, name)
        return get_value

    for attribute in find_attributes(Class):
        getter_name = "get_" + attribute.replace(f"_{Class.__name__}__", "")
        setattr(Class, getter_name, generate_getter(attribute))

    return Class
