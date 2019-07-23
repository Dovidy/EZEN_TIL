from random import randrange, choice
from math import ceil
from pathlib import Path
import shutil

#1
dirpath = Path('dataset')
if not dirpath.exists():
    dirpath.mkdir()
    for _ in range(100):
        filename = '{:04}'.format(randrange(10000))+'.txt'
        Path(dirpath/filename).write_text(choice('123'))

#2
for subdir in ['high', 'mid', 'low']:
    (dirpath/subdir).mkdir(exist_ok=True)

# dataset/*.txt => dataset/high/, dataset/mid/, dataset/low
for filepath in dirpath.glob('*.txt'):
    fn = int(str(filepath.relative_to(dirpath).with_suffix('')))
    subdir = 'low' if fn <= 3333 else ('mid' if fn <= 6666 else 'high')
    shutil.move(str(filepath), str(dirpath/subdir)) # don't care overwriting

#3
for subdir in ['high', 'mid', 'low']:
    subdirpath = dirpath/subdir
    for subsubdir in '123':
        (subdirpath/subsubdir).mkdir(exist_ok=True)

    # dataset/high/*.txt => dataset/high/1, dataset/high/2, dataset/high/3, same for mid and low
    for filepath in subdirpath.glob('*.txt'):
        subsubdir = filepath.read_text().strip(' \n\r')
        if subsubdir in list('123'):
            shutil.move(str(filepath), str(subdirpath/subsubdir))
        else:
            print(filepath, ': invalid file content')