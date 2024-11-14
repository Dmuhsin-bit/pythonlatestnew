#try to open and write to a file that is not writable:

try:
    f = open("demo file.txt")
    try:
        f.write("lorum ipsum")
    except:
        print("something went wrong when writing to rhe file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file ")
    