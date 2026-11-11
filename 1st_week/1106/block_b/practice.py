import numpy as np

a = np.array([0.5, 0.2, 0.9, 1.4])
print(a.min(), a.max(), a.mean())
print(a.argmin(), a.argmax())
print(a[1:3])

print(a*2)

mask = a < 1.0
print(a[mask])
print(mask.sum())

b = np.array([0.5, np.inf, 0.9])
print(np.isfinite(b))
print(b[np.isfinite(b)])

c = np.concatenate([a[:2], a[-2:]])
print(c)