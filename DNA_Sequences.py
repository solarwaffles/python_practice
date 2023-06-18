def main():
    in_file = open ("./dna.txt", "r")
    numPairs = in_file.readline()

    while True:
        s1 = in_file.readline().upper()
        s2 = in_file.readline().upper()
       
        if not s1:
            break


        if (len(s1) > len(s2)):
            print (longest_sebsequence(s2, s1))
        else:
            print (longest_sebsequence(s1, s2))
    print ("")

def longest_sebsequence(shorter, longer):
    length = len(shorter) - 1
    sequence = ""
    while length > 1:
        shift = 0
        while length + shift < len(shorter):
            string = shorter[shift: length + shift]
            if (longer.__contains__(string)):
                if (sequence != string):
                    print (sequence)
                    sequence = string
            shift += 1
        if (sequence != ""):
            return sequence
        length -= 1
    return "\nNo Common Sequence Found"

main()