import numpy as np

X1 = np.ones((12,1))
X2 = np.random.randint(20, 32, (12, 1))
X3 = np.random.randint(60, 82, (12, 1))

X = np.concatenate((X1, X2, X3), axis=1)
Y = np.random.uniform(13.5, 18.6, (12, 1))
A = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose().dot(Y))

Y_new = A[0] + A[1] * X[1] + A[2] * X[2]
print(A)
print(Y_new)