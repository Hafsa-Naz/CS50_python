
ans=input("Expression:").split()

x=float(ans[0])
operator=ans[1]
z=float(ans[2])

if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    if z!=0:
        result = x / z
print(result)

