import traceback

flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'

try :
    decrypt_flag = [(ord(word) >> 8, ord(word) & 0xFF) for word in flag]
    decrypt = ''.join([chr(item) for subtuple in decrypt_flag for item in subtuple])
    print(decrypt)
except Exception as e:
    traceback.print_exc(e)





