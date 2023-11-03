import neuron

import numpy

class layer:
    def __init__(self,size) -> None:
        self.neurons = []
        
        self.output = numpy.empty(1)
        
        for x in range(size):
            self.neurons.append(neuron.neuron())
        
    def calc_out(self,inputs:numpy.ndarray):
        
        input = inputs.flatten()
        
        self.output = numpy.empty(1,dtype=numpy.float16)
        
        for x in range(0,len(self.neurons)):
            self.neurons[x].calc_output(input)
            self.output = numpy.append(self.output,self.neurons[x].output,axis=None)
            
    def back_prop(self,toChange):
        pass
        ##Todo