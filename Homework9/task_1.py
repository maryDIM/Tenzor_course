# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

with open('test_file/task1_data.txt', encoding='utf-8') as f:
    with open('test_file/task1_answer.txt', 'a', encoding='utf-8') as task1_answer:
        string = '0123456789'
        for i in f.readlines():
            for j in i:
                if j not in string:
                    task1_answer.write(j)

with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
