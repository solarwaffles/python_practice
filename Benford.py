def main():
  counter = 0
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  # fill the rest
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]

    # make entries in the dictionary
    x = pop_num[0]
    pop_freq.update({x:  int(pop_freq.get(x, 0)) + 1})
    counter += 1

  # close the file
  in_file.close()

  # write out the result
  print("Digit  Count  %")
  for key in pop_freq.keys():
    print(key + "  " + str(pop_freq.get(key, 0)) + "  " + str(pop_freq.get(key, 0)/counter*100))
  
main()
