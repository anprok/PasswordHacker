for i in range(1, 11):
    file_name = 'file' + str(i) + '.txt'
    with open(file_name, 'w') as f:
        f.write(str(i))
