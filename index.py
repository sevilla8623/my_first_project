counter = 0
while True:
    my_input = input("Tell me something or a secret word to exit: ")
    secret_word = "red"
    print("You told me: ", my_input)
    # Write some code to stop loop
    counter += 1
    if my_input == secret_word:
        if counter == 1:
            print("ooooh man!!! You succeded with " + str(counter) + " try")
        else:
            print("ooooh man!!! You succeded with " + str(counter) + " tries")
        break
    print("You are in a loop #" + str(counter) + ". Try again!")

