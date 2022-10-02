import temper




temp = temper.Temper()
resp1 = temp.main()
resp2 = temp.read()
print(resp1)
print(resp2)


print(resp2[0]['internal temperature'])