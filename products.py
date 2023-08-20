products = []
while True:
	name = input("請輸入商品名稱")
	if name == "q":
		break
	price = input("請輸入商品價格")
	"""p = []
	p.append(name)
	p.append(price)
	products.append(p)
	"""
	products.append([name, price])
print(products)

for product in products:
	print(product[0], "價格是", product[1])


with open("products.csv", "w", encoding = "utf-8") as f:
	f.write("商品,價格\n")
	for product in products:
		f.write(product[0] + "," + product[1] + "\n")




