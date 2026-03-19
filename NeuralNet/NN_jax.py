import jax 
import jax.numpy as jnp

# print("Using jax", jax.__version__)

# a = jnp.zeros((2, 5), dtype=jnp.float32)
# print("zero vector\n", a)

# b = jnp.arange(6)
# print("an arange vector \n", b)

# print("device: ", jax.devices())


def simple_graph(x):
    x = x + 2
    x = x ** 2
    x = x + 3
    y = x.mean()
    return y

inp = jnp.arange(3, dtype=jnp.float32)
print("input: ", inp)
print("output: ", simple_graph(inp))
