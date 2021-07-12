def swapFileData():
    fileFrom = input("enter files name:- ")
    fileTo = input("enter files name:- ")

    with open(fileFrom, 'r') as a:
    data_a = a.read()

	with open(fileTo, 'r') as b:
    data_b = b.read()

    with open(fileFrom, 'w') as a:
    a.write(data_b)

    with open(fileTo, 'w') as b:
    b.write(data_a)

swapFileData()

