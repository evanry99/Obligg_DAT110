# Integrator for øving 10, som returnerer resultatene sine ved gjentatte kall til next()
class Oving10Integrator:
    # Lager integratoren
    def __init__(self, delta_time, time_end, function, initial_condition_vector):
        self.delta_time = delta_time
        self.time_end = time_end
        self.function = function
        self.initial_condition_vector = initial_condition_vector
        self.parameter_vector = self.initial_condition_vector
        self.current_time = 0.0

    # Starter den på nytt hvis det er behov for det
    def start(self):
        self.parameter_vector = self.initial_condition_vector
        self.current_time = 0.0

    # Henter neste verdi som en vektor
    def next(self):
        self.current_time += self.delta_time
        if self.current_time > self.time_end:
            raise StopIteration
        change_vector = self.function.evaluate(self.current_time, self.parameter_vector)
        for i in range(len(self.parameter_vector)):
            self.parameter_vector[i] += self.delta_time * change_vector[i]
        return self.parameter_vector[:]
