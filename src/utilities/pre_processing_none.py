import torch
from torch.utils.data import Dataset

class pre_processing_none(Dataset):

    '''
    This class is designed to apply pre-processing
    for "none".
    '''

    def __init__(self, data, device):
        self.data = data
        self.device = device
        self.X = data.X
        self.y = data.y

        self.X = {k: torch.tensor(v, device=device) for k, v in self.X.items()}
        self.y = {k: torch.tensor(v, device=device) for k, v in self.y.items()}

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        train_x, train_y = self.X['train'][index], self.y['train'][index]
        valid_x, valid_y = self.X['val'][index], self.y['val'][index]
        test_x, test_y = self.X['test'][index], self.y['test'][index]

        # return {
        #     "set": ("features", "targets"),
        #     "training": (train_x, train_y),
        #     "valid": (valid_x, valid_y),
        #     "test": (test_x, test_y)
        # }
    
        return train_x, train_y