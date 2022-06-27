try:
    print('Lets try thsi risky codes, if anything goes wrong will throw exception')
except Exception as e:
    print('I will run only if try block fails')
else:
    print('I will run only if there is no exception, Use this to run code when there is no exception')
finally:
    print('I am inevitable')