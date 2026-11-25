name = input("Enter Student Name: ")
total = 0
marks = []

for i in range(1, 6):
    m = float(input(f"Enter marks for Subject {i}: "))
    marks.append(m)
    total += m

percentage = total / 5

if percentage >= 80:
    res = "First"
elif percentage >= 60:
    res = "Second"
elif percentage >= 40:
    res = "Third"
else:
    res = "FAIL"

print("\n" + "=" * 30)
print("         MARKSHEET")
print("=" * 30)
print("Name:", name)
print("-" * 30)
for i in range(5):
    print(f"Subject {i+1}: {marks[i]}")
print("-" * 30)
print("Total Marks :", total)
print(f"Percentage  : {percentage:.2f}%")
print("Result      :", res)
print("=" * 30)
