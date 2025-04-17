import torch
import torch.nn as nn

class PhysicsModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(512, 512)

    def forward(self, x):
        return self.fc(x)