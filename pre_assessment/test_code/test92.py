class F:
  """An abstract class"""
  list_of_secrets = []
  def __init__(self):
    pass

  def getSecret(self):
    return self.list_of_secrets

class F_None(F):
  def __init__(self):
    self.list_of_secrets = []

class F_Some(F):
  def __init__(self):
    self.list_of_secrets.append("secret value!")

x = F_Some()
print("x:",x.getSecret())

y = F_None()
print("y:",y.getSecret())