n1 = input("N1 ")
n2 = input("N2 ")
n3 = input("N3 ")

if n1 < n2:
	if n2 < n3:
		print("Central ", n2)
	elif n1 < n3:
		print("Central ", n3)
	else:
		print("Central ", n1)

elif n1 < n3:
	print("Central ", n1)
elif n3 > n2:
	print("Central ", n3)
else:
	print("Central ", n2)