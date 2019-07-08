# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.

import os
try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Директория уже существует")

# И второй скрипт, удаляющий эти папки.

try:
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except:
    print("Директория уже удалена")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

list = os.listdir()
for i in list:
    if os.path.isdir(i):
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
shutil.copy2(r'567.py', r'file.py')

