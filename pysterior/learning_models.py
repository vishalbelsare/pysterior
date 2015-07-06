import data_model
import sampler
import parametric_functions

class RegressionModel(object):
    def __init__(self, target_energy, sampler_class, regression_function):
        """
        :type target_energy abstract_differentiable_function.AbstractDifferentiableFunction
        :type sampler_class sampler.AbstractHamiltonianSampler.__class__
        :type regression_function parametric_functions.SupervisedRegressionFunction
        """
        self.sampler = sampler_class(target_energy=target_energy)
        self.regression_function = regression_function
        self.samples = None

    def sample_parameter_posterior(self, iterations, burn_in=0, thinning=1):
        self.samples = self.sampler.sample(iterations, burn_in, thinning)

    def get_samples(self):
        return self.samples