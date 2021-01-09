'''
You can use the open function to create a file object that can read and write files. It
takes two arguments, the path of the file and the mode (mode optionally defaults to
reading). You use the mode to indicate, among other things, if you want to read or
write a file and if it is text or binary data. You can open a text file using the mode r to
read its contents. The file object has a read method that returns the contents of the
file as a string:
'''

file_path = 'sample.txt' # give complete of file here
open_file = open(file_path , 'r')
text = open_file.read()

# to find length of text file
len(text)

# after you open file close it using close()
text = open_file.close() 

# readlines

#anything that uses () is a method
'''
You can also read a file using the readlines method. This method reads the file
and splits its contents on newline characters. It returns a list of strings. Each string is
one line of the original text
'''

open_file = open(file_path, 'r')
text = open_file.readlines() # readlines() is a method.
len(text)
text[100] # display 100 lines

#then close the file 

open_file.close()


# reading a Binary file 

'''
If you are opening a binary file, such as a .jpeg image,
you are likely to corrupt the data by this conversion if you open it as text. You can,
however, read binary files by appending a b to mode:
'''

file_path = 'sample.pdf' # or 'sample.jpeg'
with open(file_path,'rb') as open_file:
    binary_text = open_file.read()

binary_text[0] # to display the result.

# we can use with in place of file_path in the above ; lines # 20-35

# writing to file using 'W' mode

'''
To write to a file, use the write mode, represented as the argument w. The tool
direnv is used to automatically set up some development environments. You can
define environment variables and application runtimes in a file named .envrc;
direnv uses it to set these things up when you enter the directory with the file. You
can set the environment variable STAGE to PROD and TABLE_ID to tokenstorage-
1234 in such a file in Python by using open with the write flag:
'''

text = 'sample.txt'
''' export STAGE=PROD
export TABLE_ID=token-storage-1234'''

with open('.envrc','w') as open_file:
    open_file.write(text)

# then you can view the file using 

!cat .envrc 
export STAGE=PROD
export TABLE_ID=token-storage-1234



# basically this is used for installing your own directories for your project.
'''
Let’s start with the easy case. Say you have a python project, and that project comes with a requirements.txt. If you try and maintain your python dependencies in your global packages, it will not be long before some of the various projects have package conflicts. Why not install them in the project directory (a la node_modules, if you will)? direnv makes that easy.
The simplest method for using python and direnv is using virtualenv. This package is typically included in most python installations or is available in the appropriate package repository.
'''

# this url is good for explanation:
#https://www.pinnsg.com/direnv-take-control-of-your-development-environment/



# OPEN function 

'''
The open function creates a file if it does not already exist and overwrites if it does.
If you want to keep existing contents and only append the file, use the append flag a.
This flag appends new text to the end of the file while keeping the original content. If
you are writing nontext content, such as the contents of a .jpeg file, you are likely to
corrupt it if you use either the w or a flag. This corruption is likely as Python converts
line endings to platform-specific ones when it writes text data. To write binary data,
you can safely use wb or ab.
'''

# use pathlib fr this.
# pathlib handles the file object behind the scene.It allows to read the text from file.

import pathlib
path = pathlib.Path("/some/path/sample.py")
path.read_text() #To read binary data, use the path.read_bytes method.

# overwriting a file 

path = pathlib.Path("/some/path/sample.py")
path.write_text("LOG:DEBUG")
path=pathlib.Path("/some/path/sample.py")


# while reading structuredd data i.e the text files we can use the above method
# but if unstructured data is there then use json methods.
# example as below

with open('sample.json','r') as opened_file:
    policy = opened_file.readlines()

# this will give a string or list of strings.

print(policy)

# this will print the content.


# now to return data structure in python 

import json 
with open('sample.json','r') as opened_file:
    policy = json.load(opened_file)

from pprint import pprint 

pprint(policy)

# for pprint refer this link :https://www.geeksforgeeks.org/pprint-data-pretty-printer-python/
# it uses for formatting text in better way.

# the above is useful when dealing with JSON docs in cloud environments when mostly its in JSON format as outpuyt.

'''
You can write a Python dictionary as a JSON file by using the json.dump method.
This is how you would update the policy file you just modified:
'''
with open('sample.json','w') as opened_file:
    policy = json.dump(policy,opened_file)


# Above was JSON format , now YAML format.

# YAML <---> Python 

'''
The most commonly used library for parsing YAML files in Python is PyYAML. It is
not in the Python Standard Library, but you can install it using pip:
$ pip install PyYAML
'''

'''
Once installed, you can use PyYAML to import and export YAML data much as you
did with JSON:
'''

import yaml
with open('sample.yaml','r') as opened_file:
    random_file = yaml.safe_load(opened_file)

# now to print the data again use pprint module 

pprint(random_file) # this will print in good format 

# to save python data to file in YAML format use:

with open('sample.yaml','w') as opened_file:
    yaml.dump(random_file,opened_file)


# Now CSV format 
# CSV <---> Python 

import csv 
file_path = 'sample.csv'

with open(file_path, newline='') as csv_file:
    off_reader = csv.reader(csv_file, delimiter=',')
    for _ in range(5):
        print(next(off_reader))

# this will print the data contained in the csv file.

# now this is good for small files but what if the csv file is very large ?

# use pandas..

'''
The Pandas package is a mainstay in the data science world. It includes a data
structure, the pandas.DataFrame, which acts like a data table, similar to a very
powerful spreadsheet. If you have table-like data on which you want to do statistical
analysis or that you want to manipulate by rows and columns, DataFrames is the tool
for you. It is a third-party library, so you need to install it with pip. You can use a
variety of methods to load data into the DataFrames; one of the most common is from
a .csv file:
'''
import pandas as pd 
df = pd.read_csv('sample.csv')
# this will be stored in df which is a dataframe.

# here we can perform different operations with dataframe.

df.head(5)
df.subscribe()

# we can use to view a single column as 

df['name of column']


# Now using Regular expressions to Search contents of text

'''
The Apache HTTP server is an open source web server widely used to serve web
content. The web server can be configured to save log files in different formats. One
widely used format is the Common Log Format (CLF). A variety of log analysis tools
can understand this format. Below is the layout of this format:

<IP Address> <Client Id> <User Id> <Time> <Request> <Status> <Size>

What follows is an example line from a log in this format:
127.0.0.1 - swills [13/Nov/2019:14:43:30 -0800] "GET /assets/234 HTTP/1.0" 200 2326
'''


# we will use 're' module to pull information from log file.

# do this in sections for making reading easier

#You can create a regular expression using named groups to pull out the IP
#address from a line:


line = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200'
re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
m = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
m.group('IP') # this will print the IP 


# reg ex to get the time 

r = r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
m = re.search(r,line)
m.group('Time') # this will print the time.


'''
Let’s say you want to pull all of the IP addresses for GET requests that
happened on November 8, 2019. Using the preceding expression, you make
modifications based on the specifics of your request:
'''

r = r'(?P<IP>\d+\.\d+\.\d+\.\d+)' # gets the IP
r+= r'- (?P<User>\w+)' # gets the User information 
r += r'\[(?P<Time>08/Nov/\d{4}:\d{2}:\d{2}:\d{2} [-+]\d{4})\]' # here the date is given , it can be any date which you want.
r += r' (?P<Request>"GET .+")' # finally we want information from GET method so we are using this GET method.


# above will give us date,IP, user info,
# to process the log use FINDITER method.

matched = re.finditer(r, access_log)

for m in matched:
    print(m.group('IP')) # this will give the IP's.



# Dealing with very large files 

'''
you can nest the with statements to open two files at once and loop
through the source file object one line at a time. You can define a generator function
to handle this, especially if you need to parse multiple files a single line at a time:
'''

def line_reading(file_path):
    with open(file_path,'r') as source_file:
        for line in source_file:
            yield line 

reader = line_reader('sample.txt')

with open('sample.txt','w') as target_file:
    for line in target_file:
        target_file.write(line)


# Text Encryption
'''
In addition to
Python’s built-in package hashlib, there is a widely used third-party package
called cryptography
'''

'''
To be secure, user passwords must be stored encrypted. A common way to handle this
is to use a one-way function to encrypt the password into a bit string, which is very
hard to reverse engineer. Functions that do this are called hash functions. In addition
to obscuring passwords, hash functions ensure that documents sent over the web are
unchanged during transmission. You run the hash function on the document and send
the result along with the document. The recipient can then confirm that the value is
the same when they hash the document. The hashlib includes secure algorithms for
doing this, including SHA1, SHA224, SHA384, SHA512, and RSA’s MD5. This is
how you would hash a password using the MD5 algorithm:
'''

import hashlib

secret = "This is protectedd file"
bsecret = secret.encode() # bsecret is binary form of text
m = hashlib.md5()

m.update(xsecret)

m.digest()

print("The byte equivalent of hash is : ", end ="") 
print(m.digest()) 

# the output will be: The byte equivalent of hash is : b'\xf1\xe0ix~\xcetS\x1d\x11%Y\x94\\hq'



# OS MODULE ****

# THIS IS IMPORTANT *****

# Commonly used OS METHODS 

os.listdir('.')
os.rename('file','new_file')
os.chmod('sample.py',0o777) # changes permission to 777
os.mkdir('/tmp/nameOfDir')
os.remove('name.py')
os.makedirs('/tmp/names')
os.rmdir('/tmp/name')


# to get statistics of a file 

os.stat('sample.txt')


# Managing Files and Directories Using os.path

'''
The
os.path module offers a plethora of path-related methods for creating and
manipulating paths as strings
'''

'''
using forward slashes to
separate directories in Unix-like systems and backward slashes in Windows. Your
program can construct paths on the fly that work on the current system, whichever it
is. The ability to easily split and join paths is probably the most used functionality of
os.path. The three methods used to split paths are split, basename, and
dirname:
'''

import os

current_directory = os.getcwd()

print(current_directory)

os.path.split(current_directory) 

os.path.dirname(current_directory) # returns the parent name

os.path.basename(current_directory) # returns the leaf name


# these below lines will print the current directory 

while os.path.basename(current_directory):
    current_directory = os.path.dirname(current_directory)
    print(current_directory)


# File locations for .rc and .sh files
# How to access these files -> .rc and .sh files 
# BASH and VIMRC files 

'''
We use the
file variable that Python automatically sets when Python code runs from a file.
This variable is populated with a path relative to the current working directory, not an
absolute or full path. Python does not automatically expand paths, as is common in
Unix-like systems, so we must expand this path before we use it to construct the path
to check our rc file. Similarly, Python does not automatically expand environment
variables in paths, so we must expand these explicitly.
'''


def find_rc(rc_name = ".samplerc"):
    #check for environment variable 
    variable = "sample_DIR"
    if variable in os.environ:
         # Check whether the environment variable exists in the current environment.
         variable_path = os.path.join(f"${variable}", rc_name)
         config_path = os.path.expandvars(variable_path)
         print(f"Checking {config_path}")
         if os.path.exists(config_path):
             return config_path 

    # check current working directory 

    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # check user home directory 
    home_dir = os.path.expanduser("~/")
    config_path = os.path.join(home_dir, rc_name)
    '''
    os.path.expanduser() method in Python is used to expand an initial path component ~( tilde symbol) or ~user in the given path to user’s home directory.
    On Unix platforms, an initial ~ is replaced by the value of HOME environment variable, if it is set. Otherwise, os.path.expanduser() method search for user’s home directory in password directory using an in-built module pwd. Path containing an initial ~user component is looked up directly in the password directory.
    On Windows platform, an initial ~ is replaced by the value of HOME and USERPROFILE environment variable, if it is set. Otherwise, HOMEPATH and HOMEDRIVE environment variable will be used. While Path containing an initial ~user component is handled by replacing the last directory component with ~user from the path derived above.
    '''

    # check directory of the file in use 

    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path,rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path 
        





