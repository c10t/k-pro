n = int(input())

# maximize (x_1 mod 1) + ... (x_n mod n)
# max (x_i mod i) = i - 1 for each i = 1, ... n
# N mod 1 + (2 - 1) mod 2 + ... (n - 1) mod n achieve this
# answer = 0 + 1 + 2 + ... + n - 1
print((n * (n - 1)) // 2)
