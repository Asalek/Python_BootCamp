# Put this at the top of your kata03.py file
kata = "The right format"

dashes= '-' * (42 - len(kata) - 2)

print(dashes, kata, '%', sep='')