while True:
    x = int(input("Enter marks: "))
    if x < 50:
        ans = "FAIL"
    else:
        ans = "PASS"

    with open("file handling\marks.txt", "a+") as file:
        file.write(f"Marks: {x}, {ans}\n")
        file.seek(0)
        print("Current contents of the file:")
        print(file.read())

    user = input("Do you want to enter more numbers? (Y/N): ").strip().lower()
    if user != "y":
        break
