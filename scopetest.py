def test():
    global b
    b=20
    global a
    a=10
    print("Inside test() a=%d"%(a))
    print("Inside test() b=%d"%(b))

a=1
print("Outside test() a=%d"%(a))
test()
print("Outside test() a=%d"%(a))
print("Outside test() b=%d"%(b))

# For the first run b was not visible
# b is visible after the second run
# a outside is not affected by the third run
# a outside has changed due to global for the last run