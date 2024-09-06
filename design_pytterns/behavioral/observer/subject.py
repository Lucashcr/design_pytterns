from contextlib import suppress

from .observer import Observer


class Subject:
    def __init__(self) -> None:
        self.__observer_collection = []

    def register_observer(self, observer: Observer):
        self.__observer_collection.append(observer)

    def unregister_observer(self, observer: Observer):
        with suppress(ValueError):
            self.__observer_collection.remove(observer)

    def notify_observers(self):
        for observer in self.__observer_collection:
            observer.update()
