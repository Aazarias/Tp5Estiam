from add import add
from add import concat
from add import soustraction

def test_function():
  a : str
  b : str
  c : int
  d : int
  
  a = "test"
  b = "concat"
  c = 8
  d = 12

  print("test de fonction user 2 add avec : ",c,"+",d,"=",add(c,d))
  print("test de fonction user 2 concat avec : ",a,"et",b,"=",concat("test","concat"))
  print("test de fonction user 2 soustraction avec : ",d,"-",c,"=",soustraction(d,c))

test_function()
