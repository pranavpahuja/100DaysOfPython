student_heights = input("Enter heights: ").split(",")

sum_h = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_h += student_heights[n]

print(student_heights)

avg_h = sum_h/len(student_heights)

print(f"Average Height = {avg_h}")