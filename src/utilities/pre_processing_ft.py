import torch
from sklearn.preprocessing import QuantileTransformer
from torch.utils.data import Dataset

class pre_processing_ft(Dataset):

    '''
    This class is designed to apply pre-processing
    for "features" and "targets".
    '''

    def __init__(self, data, device):
        self.data = data
        self.device = device
        self.X = data.X
        self.y = data.y

        preprocess = QuantileTransformer()
        preprocess.fit(self.X['train'])
        self.X = {k: torch.tensor(preprocess.transform(v), device=device) for k, v in self.X.items()}
        self.y = {k: torch.tensor(v, device=device) for k, v in self.y.items()}
        self.y_mean = self.y['train'].mean().item()
        self.y_std = self.y['train'].std().item()
        self.y = {k: (v - self.y_mean) / self.y_std for k, v in self.y.items()}

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