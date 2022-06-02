from collections import deque

ROOT = "/"
EMPTY = ""
CURRENT = "."
PARENT = ".."
PATHS_TO_SKIP = (EMPTY, CURRENT, PARENT)


def reduce_file_path(path: str):
    # Use the Python list as a stack data structure, alternatively use a deque
    try:
        reduced_path = []
        elements = path.split('/')
        for el in elements:
            if el == '..' and len(reduced_path) > 0:
                reduced_path.pop()
            if el not in PATHS_TO_SKIP:
                reduced_path.append(el)
        print(reduced_path)
        return '/' + '/'.join(reduced_path)
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


def reduce_file_path_2(path: str):
    """Defensive programming solution"""
    dirs = path.split('/')
    new_path = deque()
    for directory in dirs:
        if directory == CURRENT or not directory:
            continue
        if directory == PARENT:
            if new_path:
                new_path.pop()
            continue
        new_path.append(directory)
    return ROOT + "/".join(new_path)


if __name__ == '__main__':
    result = [
        reduce_file_path('/home//user/courses/./Programming101-Python/week01/../') ==
        '/home/user/courses/Programming101-Python',
        reduce_file_path('/') == '/',
        reduce_file_path('/srv/../') == '/',
        reduce_file_path('/srv/www/htdocs/wtf/') == '/srv/www/htdocs/wtf',
        reduce_file_path('/srv/www/htdocs/wtf') == '/srv/www/htdocs/wtf',
        reduce_file_path('/srv/./././././') == '/srv',
        reduce_file_path('/etc//wtf/') == '/etc/wtf',
        reduce_file_path('/etc/../etc/../etc/../') == '/',
        reduce_file_path('//////////////') == '/',
        reduce_file_path('/../../../../../../../') == '/',
        reduce_file_path('///////') == '/'
    ]
    
    print(result)

