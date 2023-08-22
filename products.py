import os #operating system

#讀取檔案
def read_flie(filename):
	products = []
	with open(filename, "r", encoding = "utf-8") as f:
		for line in f:
			if "商品,價格" in line:
				continue #繼續
			name, price = line.strip().split(",")
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
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
	return products

#印出所有購買紀錄
def print_prod(products):
	for product in products:
		print(product[0], "價格是", product[1])

#寫入檔案
def write_flie(filename,products):
	with open(filename, "w", encoding = "utf-8") as f:
		f.write("商品,價格\n")
		for product in products:
			f.write(product[0] + "," + product[1] + "\n")


def main():
	#檢查檔案在不在
	filename = "products.csv"
	if os.path.isfile(filename):
		print("有檔案")	
		products = read_flie(filename)	
	else:
		print("找不到檔案")

	products = user_input(products)
	print_prod(products)
	write_flie(filename, products)

main()

refactor 重構