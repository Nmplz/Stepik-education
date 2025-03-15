class Layer:

    def __init__(self):
        self.next_layer = None

    def __call__(self, layer):
        self.next_layer = layer
        return layer


class Input(Layer):
    name = "Input"

    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs


class Dense(Layer):
    name = "Dense"

    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        current_layer = self.network
        while current_layer is not None:
            yield current_layer
            current_layer = current_layer.next_layer
