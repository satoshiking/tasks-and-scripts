import os.path

dirs_with_py = []

for cur_dir, dirs, files in os.walk("main"):
    f2 = [s[-3:] for s in files]
#   print(cur_dir, dirs, f2)
    if '.py' in f2:
        if cur_dir not in dirs_with_py:
            dirs_with_py.append(cur_dir)

with open('answer.txt', 'w') as f:
    for dir in dirs_with_py:
        f.write(dir+'\n')

#print('dirs=', dirs_with_py)
    

#f1 = ['a.txt', 'dsht.txt', 'fjcnm.py', 'asdasdasdasd.py']
#f2 = [s[-3:] for s in f1]
#s = 'asdasd.py'
#print(f2)

#files_py = [str[:3]]