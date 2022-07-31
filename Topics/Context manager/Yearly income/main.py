with open('salary.txt', 'r', encoding='utf-8') as in_file:
    with open('salary_year.txt', 'w', encoding='utf-8') as out_file:
    for line in in_file:
        m = 12
        out_file.write(str(int(line) * m) + "\n")
