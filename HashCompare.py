from tkinter import Tk, Entry, Button, Label, Radiobutton, IntVar, OptionMenu, StringVar
import hashlib

root = Tk()
root.title("Hash Compare")
entry1 = Entry(root, width=50)
entry1.pack(pady=5)
entry2 = Entry(root, width=50)
entry2.pack(pady=5)
entry1.insert(0, "Enter 1st file path or Hash value ")
entry2.insert(0, "Enter 2nd file path or Hash value")

options = [
    "Compare between two files",
    "Compare between Hash and file",
    "Compare between two hash values"
]
option = StringVar()
option.set("Compare between two files")
algorithm = IntVar(0)
drop_menu = OptionMenu(root, option, *options)
drop_menu.pack()

Radiobutton(root, text="MD5", variable=algorithm, value=0).pack()
Radiobutton(root, text="SHA256", variable=algorithm, value=1).pack()
Radiobutton(root, text="SHA512", variable=algorithm, value=2).pack()


def click():
    algorithm_name = "MD5"
    if option.get() == "Compare between two files":
        hash1 = hashlib.md5()
        FileName1 = entry1.get()
        hash2 = hashlib.md5()
        FileName2 = entry2.get()
        if algorithm.get() == 0:
            hash1 = hashlib.md5()
            hash2 = hashlib.md5()
        elif algorithm.get() == 1:
            hash1 = hashlib.sha256()
            hash2 = hashlib.sha256()
            algorithm_name = "SHA256"
        elif algorithm.get() == 2:
            hash1 = hashlib.sha512()
            hash2 = hashlib.sha512()
            algorithm_name = "SHA512"

        # file1
        try:
            with open(FileName1, "rb") as f1:
                buf1 = f1.read()
                hash1.update(buf1)
                hash_file1 = (str(hash1.hexdigest()))

            # file2
            with open(FileName2, "rb") as f2:
                buf2 = f2.read()
                hash2.update(buf2)
                hash_file2 = (str(hash2.hexdigest()))

        except Exception as e:
            lbl = Label(root, text="Error {0}".format(e))
            lbl.pack()
        # Compare
        if hash_file1 == hash_file2:
            myLabel = Label(root, text="Equal hash value\n {0}: {1}".format(algorithm_name, hash_file2))
            myLabel.pack()
        else:
            myLabel = Label(root, text="Value not equal")
            myLabel.pack()

    elif option.get() == "Compare between Hash and file":

        hashToCompare = entry1.get()
        FileName2 = entry2.get()
        if algorithm.get() == 0:
            hash2 = hashlib.md5()
        elif algorithm.get() == 1:
            hash2 = hashlib.sha256()
            algorithm_name = "SHA256"
        elif algorithm.get() == 2:
            hash2 = hashlib.sha512()
            algorithm_name = "SHA512"

        try:
            # file2
            with open(FileName2, "rb") as f2:
                buf2 = f2.read()
                hash2.update(buf2)
                hash_file2 = (str(hash2.hexdigest()))

        except Exception as e:
            lbl = Label(root, text="Error {0}".format(e))
            lbl.pack()
        # Compare
        if hashToCompare == hash_file2:
            myLabel = Label(root, text="Equal hash value\n {0}: {1}".format(algorithm_name, hash_file2))
            myLabel.pack()
        else:
            myLabel = Label(root, text="Value not equal")
            myLabel.pack()

    elif option.get() == "Compare between two hash values":

        hashToCompare = entry1.get()
        hashToCompare2 = entry2.get()
        if algorithm.get() == 0:
            algorithm_name = "MD5"
        elif algorithm.get() == 1:
            algorithm_name = "SHA256"
        elif algorithm.get() == 2:
            algorithm_name = "SHA512"

        # Compare
        if hashToCompare == hashToCompare2:
            myLabel = Label(root, text="Equal hash value\n {0}: {1}".format(algorithm_name, hashToCompare2))
            myLabel.pack()
        else:
            myLabel = Label(root, text="Value not equal")
            myLabel.pack()


myButton = Button(root, text="Compare", command=click)
myButton.pack()

root.mainloop()
