# 1 -> 1, 2^0 = 1 
# 2 -> 2, 2^1 = 2
# 3 -> 4, 2^2 = 4
# 4 -> 8, 2^3 = 8

def pow_loop(base: int, exponent: int) -> int:
  product = 1
  for i in range(0, exponent):
    product = product * base
  return product

def pow_recursion(base: int, exponent: int) -> int:
  if exponent == 0:
    return 1
  if exponent == 1:
    return base
  return pow(base, exponent - 1) * 2


for i in range(0, 10):
  print(pow_recursion(2, i))