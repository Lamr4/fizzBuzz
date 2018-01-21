def fizzbuzz(i):
    fizz = 'Fizz'
    buzz = 'Buzz'
    fizzbuzz = 'FizzBuzz'
    normal = 'Normal Number'
    if i%3 == 0 and i%5 != 0:
        return fizz
    if i%3 != 0 and i&5 == 0:
        return buzz
    if i%3 == 0 and i%5 == 0:
        return fizzbuzz
    else:
        return normal
def main():
    for i in range(0,101):
        print("{} is a {}".format(i, fizzbuzz(i)))

if __name__ == '__main__':
    main()

