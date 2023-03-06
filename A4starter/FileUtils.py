def readIntoList(filename):
    fin = open(filename)
    lines = []
    for line in fin:
        lines.append(line.strip())
    fin.close()
    return lines


def writeListToFile(lines, fileName):
    fout = open(fileName, 'w')
    for line in lines:
        # print(line)
        fout.write(line + "\n")
    fout.close()
