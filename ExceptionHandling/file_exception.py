try:
    file = open("sample.txt",'r')
    print('try block')
except EOFError as e:
    print('EOF block')
    print(e)
except IOError as e:
    print('IO block')
    print(e)
except Exception as e:
    print('Exception block')
    print(e)
finally:
    print('finally block reached here at any cost')
print("continued")