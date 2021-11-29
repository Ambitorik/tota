import os

my_dictionary = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in my_dictionary.items():
    if os.path.exists(root):
        print('объект уже существует')

    else:
        for folder in folders:
            library = os.path.join(root, folder)
            os.makedirs(library)
