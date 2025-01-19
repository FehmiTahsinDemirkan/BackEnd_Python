# with open("demo2.txt", "w") as f:
    # size_to_read=100
    #
    # f_contents=f.read(size_to_read)
    #
    # while len(f_contents) > 0:
    #     print(f_contents, end="*")
    #     f_contents = f.read(size_to_read)
    # f.write("Hello World")

with open('ornek_resim.jpg', "rb") as rf:
    with open('kopya.jpg','wb') as wf:
        for line in rf:
            wf.write(line)