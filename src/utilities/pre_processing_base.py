import pandas as pd
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset

class pre_processing_base(Dataset):

    '''
    This class is designed to preprocess a CSV file
    and split the data into training, validation,
    and testing sets.
    '''

    def __init__(self, csv: str, target_var: str, split: float, device):
        self.csv = csv
        self.target_var = target_var
        self.split = split
        self.device = device
        # self.df = np.loadtxt(csv, delimiter=",", dtype=float)
        self.df = pd.read_csv(csv)
        self.X = {}
        self.y = {}

        y_all = self.df[target_var].astype("float32").to_numpy()
        X_all = self.df.drop(target_var, axis=1).astype("float32").to_numpy()

        self.X['train'], self.X['test'], self.y['train'], self.y['test'] = train_test_split(
            X_all, y_all, train_size=split, random_state=1024)

        self.X['train'], self.X['val'], self.y['train'], self.y['val'] = train_test_split(
            self.X['train'], self.y['train'], train_size=split, random_state=1024)

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