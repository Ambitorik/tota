import os
import shutil

if not os.path.exists('lesson_3'):
    os.mkdir('lesson_3')

folders = r'my_project'
files = []

for r, d, f in os.walk(folders):
    for i in f:
        if '.html' in i:
            files.append(os.path.join(r, i))

for path in files:
    folders = os.path.join('lesson_3', os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folders):
        os.mkdir(folders)
    shutil.copy(path, os.path.join(folders, os.path.basename(path)))
