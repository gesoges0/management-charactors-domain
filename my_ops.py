

class batch_norm(object):
    def __init__(self, epsilon=1e-5, momentum=0.9, name="batch_norm"):
        self.epsilon = epsilon
        self.momentum = momentum
        self.name = name
        