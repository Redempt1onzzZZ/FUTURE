import oneflow as flow
import numpy as np


x1 = flow.tensor(np.array([float('inf'), 0, -1, float('nan'), 5], dtype=np.float32))
x1 = x1.cuda()
x2 = flow.tensor(np.array([float('nan'), 0, -1, 1, 5], dtype=np.float32))
x2 = x2.cuda()
y1 = flow.matmul(x1,x2)
print(y1)

x1 = flow.tensor(np.array([float('inf'), 0, -1, float('nan'), 5], dtype=np.float32))
x1=x1.cpu()
x2 = flow.tensor(np.array([float('nan'), 0, -1, 1, 5], dtype=np.float32))
x2 = x2.cpu()
y2 = flow.matmul(x1,x2)
print(y2)

