def get_multiple():
    """
    Returns a multiple of 6 that was entered by the user
    :return: int a number
    """
    while True:
        try:
            n = input("Please give me a multiple of 6: ")
            n = int(n) # convert the input into an int
            # how to check if there is a multiple of 6
            if n % 6 == 0:
                return n
            else:
                print("that is not a multiple of 6")
        except ValueError:
            print("That is not a number")

get_multiple()