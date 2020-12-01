# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PrzemyslawSarnacki/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

# %%
import math
import numpy as np
import matplotlib.pyplot as plt


# %%
t_sampl = 1
delta_t = 1.0

t_konc = 12
m = 68.1
cd = 0.25
g = 9.81

err_tresh = 0.5
err_sum = 1
while err_sum > err_tresh:
    t = [i for i in np.arange(0, t_konc + 1, delta_t)]
    v_teor = [
        100
        * (
            math.sqrt((g * m) / cd)
            * math.tanh(math.radians((math.sqrt((g * cd / m) * t_))))
        )
        for t_ in t
    ]
    v_iter = [0 for t_ in t]

    for i in range(len(t)):
        if i < len(t) - 1:
            v_iter[i + 1] = delta_t * (g - (cd * v_iter[i] ** 2) / m) + v_iter[i]
    err_sum = sum([abs(i - j) / len(t) for i, j in zip(v_teor, v_iter)])
    delta_t = 0.9 * delta_t

# %%
plt.plot(t, v_teor, t, v_iter)
plt.title("V skoczka w t")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.grid(True)
plt.legend("v_{teoret}")


