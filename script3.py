def stringtodic(samplestr):
    lowerstr = samplestr.lower()
    lowerstr = "".join(lowerstr.split())
    counnterdict = {}
    for x in lowerstr:
        if x in counnterdict:
            counnterdict[x] += 1

        else:
            counnterdict[x] = 1

    return counnterdict



samplestring = input("Enter a String: ")
print(stringtodic(samplestring))
