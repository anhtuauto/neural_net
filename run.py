import MNIST_Loader
import network

def main():

    training_data, validation_data, test_data = \
        MNIST_Loader.load_data_wrapper()

    net = network.Network([784, 30, 10])
    net.SGD(training_data, 30, 10, 1.0, test_data = test_data)

if __name__ == "__main__":
    main()
