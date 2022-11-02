import os

def renamer():
    i = 0
    path = "D:\pictures\work_motiv"
    for filename in os.listdir(path):
        names = f"pics{i}.png"
        src = path + filename
        dest = path + names

        os.rename(src,dest)
        i = i + 1

if __name__ == "__main__":
    renamer()
