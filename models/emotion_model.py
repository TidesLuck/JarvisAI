import torch
import torch.nn as nn

class EmotionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(512, 7)

    def forward(self, x):
        return self.fc(x)