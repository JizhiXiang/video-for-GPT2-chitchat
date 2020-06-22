import torch
torch.manual_seed(1)
logits = torch.randn(10)
top_k = 3
x = torch.topk(logits, top_k)[0]
print(x)
print(x.shape)
x = x[..., -1,None]
print(x)
y = logits<x
print(y)