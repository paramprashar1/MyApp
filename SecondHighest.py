n = int(input())
a = list(map(int, input().split()))

print(a)
"""
i = 0
while i<n:
    a.append(int(input()))
    i += 1
"""
x = max(a)
print(x)
b = a.count(x)
print(b)
if b>1:
    j=0
    while j<b:
        a.remove(max(a))
        j += 1
    z=max(a)
else:
    z=max(a)
    a.remove(max(a))
    z=max(a)

print(z)
