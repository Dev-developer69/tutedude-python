try:
    file=open('sample.txt','r')
    file1=file.read()
    print(file1)
    file.close()
except FileNotFoundError:
    print("the file 'sample.txt 'was not found")
