numbers = {1, 2, 3, 4, 5, 6}
names = {"hydrogen", "helium", "lithium", "beryllium", "boron", "carbon" }

{(number,name) for number in numbers for name in names}

numbers = [1, 2, 3, 4, 5, 6]
names = ["hydrogen", "helium", "lithium", "beryllium", "boron", "carbon" ]

set(zip(numbers,names))
