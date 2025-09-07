def fun(fname, lname):
  print(lname+" "+  fname)

fun("vikas ", " Yogita")

def my_fun(*kids):
  print("the youngest child "+ kids[2])

my_fun("Emil", "tobay","Linus")

def new_fun(child3, child2, child1):
  print("the yongest child is "+ child1)
new_fun(child1="emil",child2="tobe",child3="linus")  