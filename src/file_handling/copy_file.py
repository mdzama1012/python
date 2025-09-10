"""Program to copy contents of one file to another."""


def make_copy(org_path: str):
    with open(org_path, "r") as rf:
        with open("/home/mdzama/copy.txt", "w") as wf:
            chunk_size = 10
            chunk: str = rf.read(chunk_size)
            while len(chunk) > 0:
                wf.write(chunk)
                chunk = rf.read(chunk_size)


org_path = input("Enter the path of original file: ")
make_copy(org_path)
