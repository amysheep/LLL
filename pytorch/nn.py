import torch
from torch.autograd import Variable

N, D_in, H, D_out = 64, 1000, 100, 10

x = Variable(torch.randn(N, D_in))
y = Variable(torch.randn(N, D_out))

model = torch.nn.Sequential(
        torch.nn.Linear(D_in, H),
        torch.nn.ReLU(),
        torch.nn.Linear(H, D_out)
        )

loss_f = torch.nn.MSELoss(size_average=False)

learning_rate = 1e-4
for t in range(500):
    pred_y = model(x)
    loss = loss_f(pred_y, y)
    print("the loss {} is {}".format(t, loss.data[0]))

    model.zero_grad()
    loss.backward()
    for param in model.parameters():
        param.data -= learning_rate * param.grad.data
