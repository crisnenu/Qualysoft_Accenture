arr = range(101)
for i in range(len(arr) - 1, 0, -1):
    if arr[i] % 5 == 0 and arr[i] % 3 == 0:
        print(arr[i], "- Testing")
    elif arr[i] % 5 == 0:
            print(arr[i], "- Agile")
    elif arr[i] % 3 == 0:
            print(arr[i], "- Software")
    else:
        print(arr[i])
