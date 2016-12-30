start = 1
end = 15

output = ''

print("FizzBuzz counting up to:" + str( end))

for i in range(start,end+1):
    if i%3 == 0:
        print("fizz")
    if i%5 == 0:
        print("buzz")
    if i%3 != 0 and i%5 != 0:
        print(str(i))
