from abc import ABC, abstractmethod

from src.testserver.routing.route_response import RouteResponse


class Route(ABC):

    @abstractmethod
    def execute(self, params: dict) -> RouteResponse:
        pass
