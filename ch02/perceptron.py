import numpy as np

def AND(x1, x2):
	x = np.array([x1, x2])
	w = np.array([0.5, 0.5])
	b = -0.7
	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else:
		return 1

def NAND(x1, x2):
	x = np.array([x1, x2])
	w = np.array([-0.5, -0.5])
	b = 0.7
	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else:
		return 1

def OR(x1, x2):
	x = np.array([x1, x2])
	w = np.array([0.5, 0.5])
	b = -0.2
	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else:
		return 1

def NOR(x1, x2):
	x = np.array([x1, x2])
	w = np.array([-0.5, -0.5])
	b = 0.2
	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else:
		return 1

for i in range(0, 2):
	for j in range(0, 2):
            print(i, j, ": ", AND(i, j), NAND(i, j), OR(i, j), NOR(i, j))

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)

print("XOR")
for i in range(0, 2):
	for j in range(0, 2):
            print(i, j, ": ", XOR(i, j))

def XNOR(x1, x2):
    s1 = AND(x1, x2)
    s2 = NOR(x1, x2)
    return OR(s1, s2)

print("XNOR")
for i in range(0, 2):
	for j in range(0, 2):
            print(i, j, ": ", XNOR(i, j))
