scores = input("What are the scores? Use CSV.").split(",")

for sc in range(0, len(scores)):
    scores[sc] = int(scores[sc])

max = 0

for score in scores:
    if score > max:
        max = score

print(f"Max score is: {max}")