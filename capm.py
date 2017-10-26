import matplotlib.pyplot as plt

def CAPM(rf,market,beta):
    return rf+(beta*(market-rf))

betas = []
returns = []
beta = 0
rf = .02
market = .08
for x in range(31):
    betas+=[beta]
    r = CAPM(rf,market,beta)
    returns +=[r]
    beta+=.1
plt.plot(betas,returns,"blue")

betas = []
returns = []
beta = 0
rf = .04
market = .08
for x in range(31):
    betas+=[beta]
    r = CAPM(rf,market,beta)
    returns +=[r]
    beta+=.1
plt.plot(betas,returns,"red")


betas = []
returns = []
beta = 0
rf = .02
market = .12
for x in range(31):
    betas+=[beta]
    r = CAPM(rf,market,beta)
    returns +=[r]
    beta+=.1
plt.plot(betas,returns,"black")

plt.show()