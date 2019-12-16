from abc import ABC, abstractmethod


class Method(ABC):
    def __init__(self, sequence, output_dict, spec):
        self.spec = spec
        self.output = None
        self.params = None
        self.sequence = sequence
        self.output_dict = output_dict

    @abstractmethod
    def set_params(self, parameters):
        ...

    @abstractmethod
    def identify(self):
        ...

    @abstractmethod
    def parse_output(self):
        ...
