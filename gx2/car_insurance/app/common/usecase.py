from abc import abstractmethod
from fastapi import Depends
from typing import Type, Callable, TypeVar
from pydantic import BaseModel


class BaseUseCase:
    @abstractmethod
    def invoke(self):
        ...


Req = TypeVar('Req', bound=BaseModel)
UC = TypeVar('UC', bound=BaseUseCase)

def usecase_dependency(request_type: Type[Req], usecase_type: Type[UC]) -> Callable[[Req], UC]:
    def dependency(request: request_type = Depends()) -> UC:
        return usecase_type(request)
    return dependency