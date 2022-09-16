import torch


def get_loss_fn(loss_fn):
    fn = None
    if loss_fn == 'MSE':
        fn = torch.nn.MSELoss()
    elif loss_fn == 'l1':
        fn = torch.nn.L1Loss()
    return fn

def compute_loss_fn(loss_fn):
    res = None
    return None