col = ["Burgundy", "Grey", "Purple", "Blue"]

print("The Colors Are: ") 
print(*col, sep=", ")

new_col = input ("Enter a New Color: ")
col.append(new_col)
print("New Color List: ")
print(*col, sep=", ")
