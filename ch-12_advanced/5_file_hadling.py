with (
    open("ch-12_advanced/file1.txt","w") as f1,
    open("ch-12_advanced/file2.txt","w") as f2
):
    f1.write("hello")
    f2.write("bhavin")


with (
    open("ch-12_advanced/file1.txt") as f1,
    open("ch-12_advanced/file2.txt") as f2
):
    print(f1.read())
    print(f2.read())