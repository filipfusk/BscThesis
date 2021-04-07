# imports
import numpy as np
import torch
from torch.utils.data import Dataset, TensorDataset
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from parseData import parseData

"""
Class name: Implements a Dataset object to be able to use DataLoader in PyTorch. 
To do this we need to implement the methods __getitem__ and __len__.
Function: Transform
Input: Test
Output: Test
"""
class CellDataset(Dataset):


    def __init__(self, tensors, transform=None):
        assert all(tensors[0].size(0) == tensor.size(0) for tensor in tensors)
        self.tensors = tensors
        self.transform = transform

    # Takes an index and returns a tuple (x,y)
    def __getitem__(self, index):
        x = self.tensors[0][index]
        if self.transform:
            x = self.transform(x.cpu())
            if torch.cuda.is_available():
                x = x.to(device=torch.device('cuda'))
        y = self.tensors[1][index]
        return x, y

    # Returns the size of the data
    def __len__(self):
        return self.tensors[0].size(0)

#Not used with DataLoader, why is the functionality here?
def imshow(img, title=''):
    """Plot the image batch.
    """
    plt.figure(figsize=(10, 10))
    plt.title(title)
    plt.imshow(np.transpose(img.numpy(), (1, 2, 0)), cmap='gray')
    plt.show()
