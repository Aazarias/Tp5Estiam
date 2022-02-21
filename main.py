from add import add
from add import concat

def test_function():
  a : str
  b : str
  c : int
  d : int
  
  a = "test"
  b = "concat"
  c = 8
  d = 12

  print("test de fonction add avec : ",c,"+",d,"=",add(2,3))
  print("test de fonction concat avec : ",a,"et",b,"=",concat("test","concat"))

test_function()