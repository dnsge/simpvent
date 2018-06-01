import exceptions
from types import FunctionType


class EventHandler:

    def __init__(self):
        self._events = {}

    def register(self, event_name: str, func: FunctionType):
        """ Registers an event to the event handler """

        if event_name in self._events:
            raise exceptions.EventException("An event is already registered with that name")

        self._events[event_name] = func

    def remove(self, event_name: str):
        """ Removes an event from the event handler"""

        if event_name in self._events:
            return self._events.pop(event_name)

        raise exceptions.EventException("An event with that name doesn't exist")

    def fire(self, event_name: str, *args, **kwargs):
        """ Triggers an event registered in the event handler """

        if event_name in self._events:
            return self._events[event_name](*args, **kwargs)

        raise exceptions.EventException("An event with that name doesn't exist")

    def emit(self, *args, **kwargs):
        """ Triggers all events registered in the event handler """

        for event_name, event in self._events.items():
            event(*args, **kwargs)
