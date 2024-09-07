# import abc

from abc import abstractmethod
from .models import Measurement

# class AbstractRepository(abc.ABC):
#     # @abc.abstractmethod  #(1)
#     # def add(self, batch: model.Batch):
#     #     raise NotImplementedError  #(2)

#     @abc.abstractmethod
#     def get(self, reference):
#         raise NotImplementedError

#     @abc.abstractmethod
#     def get(self, reference):
#         raise NotImplementedError


class MeasurementRepository:
    @abstractmethod
    async def list():
        return await Measurement.find().to_list()
