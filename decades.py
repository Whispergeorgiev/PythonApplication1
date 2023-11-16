age = int(input("How old are you?\n"))

dacades = age // 10
years = age % 10

print("You are " + str(dacades) +
      " decades and " + str(years) + " years old.")