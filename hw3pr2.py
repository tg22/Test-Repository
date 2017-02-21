Writeup: This function first analyzes features in a string of random s,p and r's. the features we included in our functions measured the number of same letters occurring
      consecutively. We believe that if a machine randomly generates these letters the likelihood
      that said machine randomly chooses, say, the letter 'p' 5 times in a row is extremely unlikely.
      Hence, we believe that rps-strings with many consecutive letters accurately measures humanness. Our function counts the most repetitions within the string for r p and s.
      We then add those max repeated strings together and multiply this value by 10 to acquire the score. We then picked 100 as the cutoff between human and robot with >100 being human generated

import random
import csv

def gen_rps_string( num_characters ):
    """ return a uniformly random rps string with num_characters characters """
    result = ''
    for i in range( num_characters ):
        result += random.choice( 'rps' )
    return result

# Here are two example machine-generated strings:
rps_machine1 = gen_rps_string(200)
rps_machine2 = gen_rps_string(200)
# print those, if you like, to see what they are...




from collections import defaultdict

#
# extract_features( rps ):   extracts features from rps into a defaultdict
#
def extract_features( rps ):
    """ extracts the number of consecutive characters from rps into a default dict
    """
    d = defaultdict( float )  # other features are reasonable# counts all of the 's's in rps
    
    count_s = 0
    alllist_s = []
    
    count_r = 0
    alllist_r = []
    
    count_p = 0
    alllist_p = []

    
    for i in range(len(rps)):
        if rps[i] == 's':
            count_s += 1
            
        elif rps[i] == 'r':
            alllist_s += [count_s]
            count_s = 0

        elif rps[i] == 'p':
            alllist_s += [count_s]
            count_s = 0
    
    for i in range(len(rps)):
        if rps[i] == 'r':
            count_r += 1
            
        elif rps[i] == 's':
            alllist_r += [count_r]
            count_r = 0

        elif rps[i] == 'p':
            alllist_r += [count_r]
            count_r = 0

    for i in range(len(rps)):
        if rps[i] == 'p':
            count_p += 1
            
        elif rps[i] == 'r':
            alllist_p += [count_p]
            count_p = 0

        elif rps[i] == 's':
            alllist_p += [count_p]
            count_p = 0

    alllist_s += [count_s]
    alllist_r += [count_r]
    alllist_p += [count_p]

    print(alllist_p)
    print(alllist_r)
    print(alllist_s)

    final_list_s = max(alllist_s)
    final_list_r = max(alllist_r)
    final_list_p = max(alllist_p)

    """
    for x in alllist_s:
        if x == max(alllist_s):
            final_list_s += x
            for i in range(len(alllist_s)):
                if alllist_s[i] == x:
                    posx = i
            alllist_s = alllist_s[0:posx] + alllist_s[posx+1:]
            for x in alllist_s:
                if x == max(alllist_s):
                    final_list_s += x
                    for i in range(len(alllist_s)):
                        if alllist_s[i] == x:
                            posx = i
                    alllist_s = alllist_s[0:posx] + alllist_s[posx+1:]
                    for x in alllist_s:
                        if x == max(alllist_s):
                            final_list_s += x
    
    print(final_list_s)

    for x in alllist_r:
        if x == max(alllist_r):
            final_list_r += x
            for i in range(len(alllist_r)):
                if alllist_r[i] == x:
                    posx = i
            alllist_r = alllist_r[0:posx] + alllist_r[posx+1:]
            for x in alllist_r:
                if x == max(alllist_r):
                    final_list_r += x
                    for i in range(len(alllist_r)):
                        if alllist_r[i] == x:
                            posx = i
                    alllist_r = alllist_r[0:posx] + alllist_r[posx+1:]
                    for x in alllist_r:
                        if x == max(alllist_r):
                            final_list_r += x

    for x in alllist_p:
        if x == max(alllist_p):
            final_list_p += x
            for i in range(len(alllist_p)):
                if alllist_p[i] == x:
                    posx = i
            alllist_p = alllist_p[0:posx] + alllist_p[posx+1:]
            for x in alllist_p:
                if x == max(alllist_p):
                    final_list_s += x
                    for i in range(len(alllist_p)):
                        if alllist_p[i] == x:
                            posx = i
                    alllist_p = alllist_p[0:posx] + alllist_p[posx+1:]
                    for x in alllist_p:
                        if x == max(alllist_p):
                            final_list_p += x
                                    
    """
    

    d['s'] = final_list_s
    d['r'] = final_list_r
    d['p'] = final_list_p                    # doesn't use them, however
    return d   # return our features... this is unlikely to be very useful, as-is






#
# score_features( dict_of_features ): returns a score based on those features
#
def score_features( dict_of_features ):
    """ returns a score based on the highest number of consecutive characters
        for each letter
    """
    d = dict_of_features
    score = (d['s'] + d['p'] + d['r']) * 10
    return score   # return a humanness or machineness score







#
# read_data( filename="rps.csv" ):   gets all of the data from "rps.csv"
#
def read_data( filename="rps.csv" ):
    """ reads a file named rps.csv and outputs a list of lists that 
        conveys each row of the .csv file
    """
    try:
        csvfile = open( filename, newline='')
        csvrows = csv.reader (csvfile)

        all_rows = []
        for row in csvrows:
            all_rows.append( row )
        
        del csvrows
        csvfile.close()
        return all_rows
    
    except FileNotFoundError as e:
        print("File not found: ", e)
        return []


def main():
    lists = read_data()
    scores = []
    for x in lists:
        dictionary = extract_features(x[3])
        scoring = score_features(dictionary)
        scores += [scoring]

    print( scores )
