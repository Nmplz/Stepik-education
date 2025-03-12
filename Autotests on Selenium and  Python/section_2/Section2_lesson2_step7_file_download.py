import os


# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")  # добавляем к этому пути имя файла
print(f" file-->>> {file_path}")
# element.send_keys(file_path)


print("full file path >>", os.path.abspath(__file__))
print()
print("catalog of file path>>", os.path.abspath(os.path.dirname(__file__)))
