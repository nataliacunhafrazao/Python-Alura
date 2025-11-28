import  as np

b = np.array([[1,2,3,5]])

c = b.transpose()

print(b.dot(c),sum(b),sum(c))