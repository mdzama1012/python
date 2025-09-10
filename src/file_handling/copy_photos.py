"""Program to copy photos"""


def make_copy(org_path: str):
    with open(org_path, "rb") as rf:
        with open("/home/mdzama/copy.jpg", "wb") as wf:
            chunk_size = 10
            chunk: str = rf.read(chunk_size)
            while len(chunk) > 0:
                wf.write(chunk)
                chunk = rf.read(chunk_size)


org_path = input("Enter the path of original file: ")
make_copy(org_path)
