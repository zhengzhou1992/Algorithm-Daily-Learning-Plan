from os import listdir
from os.path import abspath, dirname, join

URL_BASE = 'https://github.com/zhengzhou1992/Algorithm-Daily-Learning-Plan/blob/master/'
SECTION_SEPARATOR = '## One day one file:'
BASE_DIR = dirname(abspath(__file__))

with open(join(BASE_DIR, 'README.md'), 'r+') as readme:
    append_pos = readme.read().find(SECTION_SEPARATOR)
    readme.truncate(append_pos + len(SECTION_SEPARATOR) + 3)
    readme.seek(0, 2)
    readme.write('\n')
    for filename in listdir(BASE_DIR):
        if '_' not in filename or not filename.endswith('.py'):
            continue
        show_name = filename[:-3].replace('_', ' ')
        new_line = '* [{show_name}]({url_base}{filename})\n'.format(
            show_name=show_name,
            url_base=URL_BASE,
            filename=filename)
        readme.write(new_line)
