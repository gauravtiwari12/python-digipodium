import os

# create folder
if os.path.exists('test'):
    print('test folder exists')
else:
    os.mkdir('test')
    print('test folder created')

    folder = 'a/b/c/d/e/f/g'

if os.path.exists('test'):
    print('test folder exists')
else:
    os.mkdir('test')
    print('test folder created')



# display details
if os.path.exists('basics/hello.py'):
    size= os.path.getsize('basics/hello.py')
    ctime = os.path.getctime('basics/hello.py')
    mtime = os.path.getmtime('basics/hello.py') 
    isfile = os.path.isfile( 'basics/hello.py')
    isdir = os.path.isdir('basics/hello.py')
    print('filename: basics/hello.py')
    print('size:', size, 'bytes')
    print('ctime:', datetime.fromtimestamp(ctime))
    print('mtime:', datetime.fromtimestamp (mtime))
    print('isfile:', isfile)
    print('isdir:', isdir)