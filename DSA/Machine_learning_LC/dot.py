# def dot_product(a, b):
#     assert len(a) == len(b), 'different length'
#     res = sum([i*j for i,j in zip(a,b)])
#     return res

# def dot_product(a, b):
#     assert len(a) == len(b), 'different length'
#     res = 0
#     for i in range(len(a)):
#         res = res + a[i]*b[i]
#     return res

# a = [1, 2]
# b = [3, 4]
# print("results:", dot_product(a,b))

# -- L2 norm --

# import math
# def l2_norm(x):
#     return math.sqrt(sum([i**2 for i in x]))

# print('l2 norm:', l2_norm([1, 2]))


def min_max_normalize(xs):
    max_xs = max(xs)
    min_xs = min(xs)
    n = len(xs)
    if max_xs > min_xs:
        return (xs - [min_xs]*n)/(max_xs - min_xs)
    else:
        return [0]*n

print(min_max_normalize([1, 2, 3]))