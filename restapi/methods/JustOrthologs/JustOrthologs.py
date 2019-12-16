from restapi.methods.Methods import Method


class JustOrthologs(Method):
    def __init__(self, sequence, output_dict, spec):
        super().__init__(sequence, output_dict, spec)
        self.spec = spec
        self.output = None
        self.params = None
        self.sequence = sequence
        self.output_dict = output_dict

    def set_params(self, parameters):
        pass

    def identify(self):
        pass

    def parse_output(self):
        pass

# if "__main__" == __name__:
#     out = {}
#     just = JustOrthologs(out)
#     just.set_params("str")
#     just.identify("seq")
#     just.parse_output()
#     print(just.output_dict)
#     print(out)
#     assert out == just.output_dict
