def getInput():
  return input()

def splitInput(string):
  return string.split(' ')

# wire an argument with its action
def performer(argument):
  actions = { "CREATE" : "create a file(function)"} 
  return actions.get(argument, "Invalid ")  

def handler():
  arguments = splitInput(getInput())
  
  if len(arguments) > 0:
    print(performer(arguments[0]))

handler()