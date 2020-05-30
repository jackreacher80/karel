def main():
    # TODO write your solution here
    print("Enter a sequence of non decreasing numbers")

    num1 = float(input("Enter num:- "))

    non_decreasing_sequence(num1)


"""This function calculates non decreasing series and its count"""
def non_decreasing_sequence(n1):
    count=3
    n2 = float(input("Enter num:- "))
    while n2 >= n1:
        n1 = n2
        n2 = float(input("Enter num:- "))
        count+=1
    print("Thanks for playing!")
    print("Sequence length: " + str(count-1))



if __name__ == "__main__":
    main()