# vertex-ai-examples
Code samples and notebooks for Vertex AI on Google Cloud

## PyTorch on Vertex AI

The goal of the PyTorch repo is to provide examples to help users build familiarity with using the various services on Vertex AI. The neural nets are lightweight and datasets familiar to those in the field, the focus is on the interplay of the ML code and the Vertex AI SDK. 

### Where to start

If you need to set up a GCP project, Workbench instance, or want to experiment with authenticating to a project via Colab, please see:

[gcp_setup.ipynb](https://github.com/rastringer/vertex-ai-examples/blob/main/pytorch_on_vertex/gcp_setup.ipynb).

### Vertex Training 

To learn how to run a simple MNIST model on the Vertex AI Training service using prebuilt containers:

[pytorch_mnist_training_simple.ipynb](https://github.com/rastringer/vertex-ai-examples/blob/main/pytorch_on_vertex/pytorch_mnist_training_simple.ipynb)

Move on to creating a custom Python package and launching a Training job:

[python_mnist_training_package.ipynb]()

### Vertex Experiments

How to experiment with different hyper-parameters and analyse results:

[pytorch_experiments_CIFAR10.ipynb](https://github.com/rastringer/vertex-ai-examples/blob/main/pytorch_on_vertex/pytorch_experiments_cifar10.ipynb)
