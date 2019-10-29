import json

#Place into web core, add run code in JS on node.php

#helper functions

#finds the index for the nth occurence of a substring in a string
def find_occurence(string, substring, n):
    if( n == 1 ):
        return string.find(substring)
    else:
        return string.find(substring,find_occurence(string, substring, n - 1) + 1)

#gets integer after the nth occurence of a substring in a string
def get_value(string, substring, n):
        index = (find_occurence(string, substring, n)) + 1
        secondary_index = index
        while (string[secondary_index]).isdigit():
            secondary_index += 1
        if (string[index:secondary_index]).isdigit():
            return string[index:secondary_index]
            
#get mean of all values in dict
def get_mean(dict):
    temp_list = list(dict.values())
    temp_list = sum(temp_list, [])
    temp_list = map(int, temp_list)
    return int(sum(temp_list)/float(len(temp_list)))

#read file and create list for lines removing whitespaces
def read_file_inline(string):
    lines = []
    with open(string, 'rt') as in_file:
        for line in in_file:
            lines.append(line.replace(' ', ''))
    return lines
        
#creates dictionary for reads(key) and lanes(values)
#expects that density reading will follow third occurence of "," on a line 
def create_dict(lines):

    density_list = []
    density_dict = {}
    read_count = 0
    check = False

    for element in lines:
        #looks for density to assign read number
        if check is False:
            if element.find("Density") != -1:
                read_count += 1
                check = True
                continue
        #verify that line should be scanned for value
        if check:
            if get_value(element, ",", 3):
                #iteravely append values to list for a read
                density_list.append(get_value(element, ",", 3))
            else:
                #no more values in read or invalid entry, update dictionary, reset list for next read
                check = False
                density_dict.update({"read" + str(read_count):density_list})
                density_list = []
    return density_dict

#print "Dictionary:\n", create_dict(read_file_inline("summary.txt"))
#print "mean is:", get_mean(create_dict(read_file_inline("summary.txt")))

def main():
    print get_mean(create_dict(read_file_inline("summary.txt")))
    with open('density.txt', 'w') as outfile:  
    json.dump(get_mean(create_dict(read_file_inline("summary.txt"))), outfile)