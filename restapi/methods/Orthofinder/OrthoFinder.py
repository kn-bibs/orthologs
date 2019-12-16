import os
from subprocess import Popen

from restapi.methods.Methods import Method
from restapi.methods.sequence import Sequence


class OrthoFinder(Method):
    def __init__(self, sequence, output_dict, spec="swiss_homo"):
        super().__init__(sequence, output_dict, spec)
        self.spec = spec
        self.output = None
        self.params = None
        self.sequence = sequence
        self.output_dict = output_dict

    def set_params(self, parameters):
        self.params = parameters
        self.params = self.params.replace("o", "-o")
        self.params = self.params.replace("f", "-f")

    def create_fasta(self):
        input = ''
        input += "{0}\n".format(self.sequence.header)
        input += "{0}\n".format(self.sequence.sequence)
        return input

    def identify(self):
        input = self.create_fasta()
        FNULL = open(os.devnull, 'w')
        folder = self.params.split("-f")[1].split()[0]
        print(folder + "params.fa")
        file = open(folder + "params.fa", "a")
        file.write(input)
        file.close()
        p = Popen(["python3.6", "./OrthoFinder/orthofinder.py"] + self.params.split())
        p.communicate(input=input.encode("ascii"))
        parsed_output = self.parse_output()
        self.output_dict["Orthofinder"] = parsed_output

    def parse_output(self):
        path = self.params.split("-o")[1].split()[0]
        dir = os.listdir(path)
        path += "/" + dir[-1] + "/Orthologues/"
        dir2 = os.listdir(path)
        path += dir2[-1] + "/"
        dir2 = os.listdir(path)
        path += [i for i in dir2 if i.startswith(self.spec)][0]
        result = {}
        with open(path) as res:
            res.readline()
            for line in res.readlines():
                line = line.strip().split()
                result[line[0]] = [line[1].split(","), line[2].split()]
        return result


if "__main__" == __name__:
    out = {}
    seq = Sequence()
    seq.header = ">tr|D3ZDY4|D3ZDY4_RAT C-C motif chemokine OS=Rattus norvegicus OX=10116 GN=Ccl1 PE=3 SV=1"
    seq.sequence = "MKLLNMVLVCLLVAAMWLQNVDSKSMHVVSSRCCLNTLENKIALKFIKCYKEIGPSCPYYPAVIFRLIKGRESCALTNTTWVQDYLKKVKPC"
    finder = OrthoFinder(seq, out)
    finder.set_params("o ./test/test_res f ./test/")
    finder.identify()
    assert out == finder.output_dict
