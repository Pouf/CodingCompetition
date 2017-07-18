# You are provided with a table which associates MIME types to file extensions.
# You are also given a list of names of files to be transferred and for each
# one of these files, you must find the MIME type to be used.

# The extension of a file is defined as the substring which follows the last
# occurrence, if any, of the dot character within the file name. If the
# extension for a given file can be found in the association table (case
# insensitive, e.g. TXT is treated the same way as txt), then print the
# corresponding MIME type. If it is not possible to find the MIME type
# corresponding to a file, or if the file doesn’t have an extension, print
# UNKNOWN.

 
N = int(input())
Q = int(input())
table = {}

for i in range(N):
    ext, mt = input().split()
    table[ext.lower()] = mt
for i in range(Q):
    fname = input()
    fext = '.' in fname and fname.split('.')[-1].lower() or ''
    print(fext in table and table[fext] or 'UNKNOWN')
