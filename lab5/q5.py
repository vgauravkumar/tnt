def Remove_Lowercase (infile, outfile):
    f = open (outfile, "w")
    for line in open (infile):
        if not line [0] in "abcdefghijklmnopqrstuvwxyz":
            f.write(line)
    f.close ()


Remove_Lowercase("text.txt","ans.txt")
    