colors = ["Pink", "Blue","Black"]
with open("colors.txt", "w") as f:
    for line in colors:
        f.write(line)
        f.write('\n')