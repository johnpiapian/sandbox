class Sut:
  def __init__(self, list):
    self.list = list

  def map(self, f):
    return [f(x) for x in self.list]
  
  def filter(self, f):
    return [x for x in self.list if f(x)]
  
  def data(self):
    return self.list


mylist = Sut([1, 2, 3, 4, 5])

print(mylist.data())
print(mylist.map(lambda x: x * 2))
print(mylist.map(lambda x: x * x))
print(mylist.filter(lambda x: x % 2 == 1))
