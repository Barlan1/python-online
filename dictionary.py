dic= {
  "brand":"tata",
  "model":"safari",
  "year": 1999,
  "flag": False,
  "flag": True,
  "year": 1933,
  "color":["red","blue","white"]
}
#print(dic)
#print(dic["flag"])
#print(len(dic))
#print(dic['model'])

#x= dic.items()
#print(x)
#if "colr" in dic:
 #  print("ok")
#else: print("Not")   
#
#dic["brand"]="MG"
#print(dic)

#dic.update({"year":2025})
#print(dic["year"])

#dic.clear()
#print(dic)

#for x in dic:
 # print(x) 

#for x in dic:
 # print(dic[x])

#print(dic)

#for x in dic.values():
 # print(x)

#for x in dic.keys():
 # print(x)  

#mydic= dic.copy()
#print(mydic)
print(dic)
nydic= dict(dic)
nydic.pop("model")
print(nydic)

nydic.popitem()
print(nydic)

