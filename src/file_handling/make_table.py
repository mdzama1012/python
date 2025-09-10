"""Python program to write multiplication tables."""


def write_table(n: int) -> None:
    with open(f"/home/mdzama/tables.txt", "w") as wf:
        for x in range(1, n + 1):
            wf.write(f"Multiplication Table of {x}: \n")
            for y in range(1, 11):
                table = f"{x} x {y} = {x*y:03}\n"
                wf.write(table)


n: int = int(input("How many tables: "))
write_table(n)
