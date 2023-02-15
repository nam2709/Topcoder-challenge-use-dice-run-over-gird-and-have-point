import random
N = int(input())
V=int(input())
A = 0-V
point = 0
U = 1
D = 2
R = 3
R1 = 3
L = 4
F = 5
B = 6
# U = random.randint(1,V)
# D = random.randint(1,V)
# R = random.randint(1,V)
# R1 = random.randint(1,V)
# L = random.randint(1,V)
# F = random.randint(1,V)
# B = random.randint(1,V)
grid = [U,R,D,L,F,B]
ar = [
    [[random.randint(A,V)] for t in range(1, N+1)]
    for i in range(1, N+1)
]
print(U,R,D,L,F,B)
print(ar)
print(ar[0][0])
print(ar[0][1])
print(ar[0][2])
for row in ar:

	print(row)
if N % 2 == 0:
	N_s = N/2
elif N % 2 != 0:
	N_s = (N+1)/2
# Muốn lặp hết có thể để vòng lặp to hơn
print(int(N_s))
for t in range(0,int(N_s)):

	# RIGHT
	for i in range(1,N+1-t-t):
			R = D
			D = L
			print("ar[N-N+t][i-1+t] = ")
			print(ar[N-N+t][i-1+t])
			if [D] == ar[N-N+t][i-1+t]:
				point = point + D
			L = U
			U = R1
			# Khi giá trị cụ thay đổi mà mình muốn nó bằng giá trị cũ
			R1 = R
			F = F
			B = B
			# in những giá trị ra sau khi thay đổi bởi for mỗi 1 lần for thay đổi sẽ in một lần
			print("U,R,D,L,F,B = ")
			print(U,R,D,L,F,B)
			# để thế này sẽ in lần lượt cả 2 print theo 1 for trước)
			#3 2 4 1 5 6
			#4
			#2 4 1 3 5 6
			#1
			print("D = ")
			print(D)
			print("point = ")
			print(point)
			print("_____________________________________________")


	#DOWN

	print("============================================")
	print(U,R,D,L,F,B)
	F1 = F
	print(F1)
	print("============================================")
	for i in range(1,N-t-t):
		F = D
		D = B
		print("ar[i+t][N-1-t] = ")
		print(ar[i+t][N-1-t])
		if [D] == ar[i+t][N-1-t]:
			point = point + D
		B = U
		U = F1
		# Khi giá trị cụ thay đổi mà mình muốn nó bằng giá trị cũ
		F1 = F
		R = R
		L = L
		# in những giá trị ra sau khi thay đổi bởi for mỗi 1 lần for thay đổi sẽ in một lần
		print("U,R,D,L,F,B = ")
		print(U,R,D,L,F,B)
		# để thế này sẽ in lần lượt cả 2 print theo 1 for trước)
		#3 2 4 1 5 6
		#4
		#2 4 1 3 5 6
		#1
		print("D = ")
		print(D)
		print("point = ")
		print(point)
		print("_____________________________________________")

	# LEFT


	print("============================================")
	print(U,R,D,L,F,B)
	U1 = U
	print(U1)
	print("============================================")
	for i in range(N-t-t,1,-1):
		U = L
		L = D
		print("ar[N-1-t][i-2+t] = ")
		print(ar[N-1-t][i-2+t])
		if [D] == ar[N-1-t][i-2+t]:
			point = point + D
		D = R
		R = U1
		# Khi giá trị cụ thay đổi mà mình muốn nó bằng giá trị cũ
		U1 = U
		F = F
		B = B
		# in những giá trị ra sau khi thay đổi bởi for mỗi 1 lần for thay đổi sẽ in một lần
		print("U,R,D,L,F,B = ")
		print(U,R,D,L,F,B)
		# để thế này sẽ in lần lượt cả 2 print theo 1 for trước)
		#3 2 4 1 5 6
		#4
		#2 4 1 3 5 6
		#1
		print("D = ")
		print(D)
		print("point = ")
		print(point)
		print("_____________________________________________")


	#UP

	print("============================================")
	print(U,R,D,L,F,B)
	F2 = F
	print(F2)
	print("============================================")
	for i in range(N-t-t,2,-1):
		F = U
		U = B
		print("ar[N-N][i-2] = ")
		print(ar[i-2+t][N-N+t])
		if [D] == ar[i-2+t][N-N+t]:
			point = point + D
		B = D
		D = F2
		# Khi giá trị cụ thay đổi mà mình muốn nó bằng giá trị cũ
		F2 = F
		R = R
		L = L
		# in những giá trị ra sau khi thay đổi bởi for mỗi 1 lần for thay đổi sẽ in một lần
		print("U,R,D,L,F,B = ")
		print(U,R,D,L,F,B)
		# để thế này sẽ in lần lượt cả 2 print theo 1 for trước)
		#3 2 4 1 5 6
		#4
		#2 4 1 3 5 6
		#1
		print("D = ")
		print(D)
		print("point = ")
		print(point)
		print("_____________________________________________")