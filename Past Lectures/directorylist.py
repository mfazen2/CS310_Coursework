import sys
import os
def directorytree(directory,ind="|"):
    print(ind + os.path.basename(directory)+"/")
    ind = ind + ' -- '
    for item in os.listdir(directory):
        item_path = os.path.join(directory,item)
        if os.path.isdir(item_path):
            directorytree(item_path,ind)
        else:
            print(ind+item)
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("OOPS WRONG ARGUEMENT! Please try the following format: python directorylist.py <directory path>")
        sys.exit(1)
    target_dir = sys.argv[1]
    if not os.path.exists(target_dir):
        print("ERROR: Invalid directory, ",target_dir," does not exist.")
        sys.exit(1)
    if not os.path.isdir(target_dir):
        print("Error: ",target_dir," is not a valid directory.")
        sys.exit(1)

    directorytree(target_dir)        


