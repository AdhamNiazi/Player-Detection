import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from models.simple_object_detector import PlayerDataset, SimpleObjectDetector
import torch.nn.functional as F