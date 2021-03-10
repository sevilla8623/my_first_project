# "3. Write a Python program which iterates the integers from given by user ranges.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output:
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz"
begin = int(input())
end = int(input())
for number in range(begin, end):
    for fizzbuzz in range(15):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)


