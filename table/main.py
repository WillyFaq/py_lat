from prettytable import PrettyTable

data = []
for i in range(1,100):
	tmp = {"no":i, "nama":f"User {i}"}
	data.append(tmp)

myTable = PrettyTable(["No", "Nama"])
for nama in data:
	myTable.add_row([nama["no"], nama["nama"]])

print(myTable)
