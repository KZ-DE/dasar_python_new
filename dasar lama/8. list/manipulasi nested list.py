data = data0 = [1,2]
data1 = [3,4]

data = [1,2,3,4,1,3,1]
print(f"data list biasah = {data}")

data_nested = [data0, data1, "bejo", 1]
print(f"data nested = {data_nested}")
data_nested[0][0] = "tets"
print(f"data nested baru {data_nested}")
data_nested[0][1] = "halo"
print(f"data nested baru {data_nested}") 