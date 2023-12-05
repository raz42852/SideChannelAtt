import time

password = "lalallaa"

def check_password(candidate):
    for i in range(len(candidate)):
        if candidate[i] != password[i]:
            return False
        time.sleep(0.1)
    if len(candidate) != len([password]):
        return False
    return True

def guess_password(time_arr, current_password):
    j = 0
    while j < 26:
        t0 = time.time()
        check_password(current_password + chr(97 + j))
        t1 = time.time()
        print(" Char :{} , took:{} seconds".format(chr(97 + j), t1 - t0))
        time_arr.insert(j, t1 - t0)
        j += 1

def find_password():
    time_arr = []
    whole_password = ''
    i = 0

    while i < len(password):
        guess_password(time_arr, whole_password)
        letter = chr(97 + time_arr.index(max(time_arr)))
        whole_password += letter
        time_arr.clear()
        print(whole_password)
        i += 1

find_password()
