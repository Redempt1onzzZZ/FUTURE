import oneflow as flow
import numpy as np

x1 = flow.tensor(np.array([[float('inf'), 0, -1, float('nan'), 5]], dtype=np.float32))
x1 = x1.cuda()
y1 = flow.cast(x1,dtype=flow.int8)
print(y1)

x1 = flow.tensor(np.array([[float('inf'), 0, -1, float('nan'), 5]], dtype=np.float32))
x1 = x1.cpu()
y2 = flow.cast(x1,dtype=flow.int8)
print(y2)

