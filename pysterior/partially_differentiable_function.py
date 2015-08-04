import theano.tensor as T
import theano

def gradient_factory(variables, output_expression, differentiable_variable):
    f = theano.function(variables, output_expression)
    f_grad = theano.function(variables, theano.grad(output_expression, differentiable_variable))
    return f, f_grad

class PartiallyDifferentiableFunctionFactory(object):
    def __init__(self, variables, output_expression):
        self.f = theano.function(variables, output_expression)
        self.variables = variables
        self.var_lookup = {v.name:v for v in variables}
        self.output_expression = output_expression

    def get_partial_diff(self, differentiable_var_name):
        diff_var = self.var_lookup[differentiable_var_name]
        grad = theano.function(self.variables,
                               theano.grad(self.output_expression,
                                           diff_var))
        return self.f, grad

a,b = T.scalar('a'), T.scalar('b')
product = a*b

factory = PartiallyDifferentiableFunctionFactory([a,b], product)
f, a_grad = factory.get_partial_diff('a')

print(f(a=2, b=2))

#Note kwargs implicit, see f.input_storage
#TODO: Write a closure generator for kwarg functions produced by the factory