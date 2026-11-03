

# lec 1 exercise


import os

def recursive(path: str):
    cnt = 0

    if os.path.isfile(path):
        return 1

    if not os.path.isdir(path):
        return 0
    
    filepaths = os.listdir(path)
    
    for filepath in filepaths:
        cnt += recursive(os.path.join(path, filepath))

    return cnt
    

if __name__ == "__main__":
    
    path = "/home/frede/intromachinelearning"
    cnt = recursive(path)
    
    print(f"Files counted: {cnt}")
    

