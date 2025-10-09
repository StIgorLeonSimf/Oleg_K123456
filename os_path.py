from datetime import datetime
import os
from pathlib import Path
import shutil
from tkinter import *
from tkinter import filedialog as fd


# # os.mkdir('size_tr')
# # os.mkdir(r'D:\UNITS\Python\Units\Oleg_Karabanov\size_tr\size_tr3')
# # os.makedirs(r'D:\UNITS\Python\Units\Oleg_Karabanov\size_tr\sz\size_tr2', exist_ok=True)
# # print(os.path.abspath('size_tr'))
# # pf = os.path.join('..', 'size_tr')
# pf = os.path.join('size_tr')
# # print(pf)
# print(os.path.abspath(pf))
# t = os.path.getmtime(r'D:\UNITS\Python\Units\Oleg_Karabanov\size_tr\size_tr3')
# print(t)
# dt = datetime.fromtimestamp(t)
# dt = dt.strftime('%H:%M:%S %d.%m.%Y')
# print(dt)
# print(os.path.exists(r'D:\UNITS\Python\Units\Oleg_Karabanov\size_tr\size_tr3'))

def seek(target, target1='') -> tuple:
    """Писк количества папок, файлов и размера основной дирректории."""
    size = 0
    cnt_dir = 0
    cnt_file = 0
    ps = os.path.join(target, target1)
    print('ps =', ps)
    path_ = os.path.abspath(ps)
    print('path_ =', path_)
    for i in os.listdir(path_):
        ps = os.path.join(path_, i)
        if os.path.isfile(ps):
            cnt_file += 1
            size += os.path.getsize(ps)
        else:
            cnt_dir += 1
            # cnt_dir += seek(ps)[1]
            # size += seek(ps)[0]
            # cnt_file += seek(ps)[2]
            size1, cnt_dir1, cnt_file1 = seek(ps)
            size += size1
            cnt_dir += cnt_dir1
            cnt_file += cnt_file1


    return size, cnt_dir, cnt_file


# print(seek('size_tr'))
# print(Path('').resolve())
# print(os.path.abspath(''))
pf = os.path.join('size_tr')
print(pf)
p = os.path.abspath(pf)
# for root, dirs, files in os.walk(os.path.abspath(p)):
#     print(root, dirs, files)
print(p)
# shutil.copytree(p, r'D:\UNITS\Python\Units\Oleg_Karabanov\size_tr')
ist = r'D:\UNITS\Python\Units\Oleg_Karabanov\size_tr\tr1.py'
# shutil.move(ist, r'D:\UNITS\Python\Units\Oleg_Karabanov\size_new')

root = Tk()
root.withdraw()
dirt = fd.askdirectory()
if dirt:
    for file in os.listdir(dirt):
        if file.endswith('.mp4'):
            fill_path = os.path.join(dirt, file)
            tt = os.path.getmtime(fill_path)
            print()  # fromtimestamp