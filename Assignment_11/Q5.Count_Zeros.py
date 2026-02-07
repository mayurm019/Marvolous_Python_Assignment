# 5. Count Zeros in a Number (Recursively)
# Write a recursive function to count how many zeros are in the given number.
# count_zeros(1020300) → 4


num = int(input("Entre Number"))
n = str(num)
res = n.count("0")
print(res)