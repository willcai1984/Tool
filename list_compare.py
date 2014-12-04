#!/usr/bin/python
# Filename: list_Compare.py
# Function: Compare two list and print the add/remove parameters,return a dict, the value means appear times, if it is negative, means the standard list not has the item 
# coding:utf-8
# Author: Will
# python list_compare.py -sf '1.txt' -cf '2.txt' 

import re, argparse, sys


'''
This func can give the standard parameters occur times in compare list 
For example
>>> a=[1,2,3]
>>> b=[1,3,3,5]
>>> list_compare(a,b)
{1: 1, 2: 0, 3: 2, 5: -1}
>>> 
 1: 1 time in compare list
 2: 0 time in compare list
 3: 2 time in compare list
 5: -1 is in compare list but not in standard
'''

def list_compare(standard_list, compare_list):
    #set all compare parameters' occur times to 0
    #standard_dict = {i:0 for i in standard_list}--not suppot in python2.6
    standard_dict = {}
    for i in standard_list:
        standard_dict[i] = 0
    for j_key in compare_list:
        #if list_standard not has the key,may raise the KeyError
        try:
            j_value = standard_dict[j_key]
        except KeyError:
            j_value = -1
        else:
            #-1+1=0 if the value is -1, do nothing
            if j_value != -1:
                j_value += 1
        standard_dict[j_key] = j_value
    return standard_dict

parse = argparse.ArgumentParser(description='list compare')
parse.add_argument('-sf', '--standardfile', required=True, dest='standard',
                    help='standard file path')

parse.add_argument('-cf', '--comparefile', required=True, dest='compare',
                    help='compare file path')

def main():
    args = parse.parse_args() 
    sf = args.standard
    cf = args.compare
    try:
        with open(sf, mode='r') as sf_o:
            sf_list = sf_o.readlines()
        with open(cf, mode='r') as cf_o:
            cf_list = cf_o.readlines()
    except IOError:
        print '''No such file or directory: '%s' or '%s', please check ''' % (sf, cf)
        sys.exit(1)
    sf_list = [re.sub(r'\n|\r|\r\n', '', i).rstrip() for i in sf_list if i != '\n' or i != '\r\n' or i != '']
    cf_list = [re.sub(r'\n|\r|\r\n', '', i).rstrip() for i in cf_list if i != '\n' or i != '\r\n' or i != '']
    compare_result_dict = list_compare(sf_list, cf_list)
    print 'compare_result_dict is %s' % str(compare_result_dict)
    match_list = [key for key, value in compare_result_dict.items() if int(value) == 1]
    standard_only_list = [key for key, value in compare_result_dict.items() if int(value) == 0]
    compare_only_list = [key for key, value in compare_result_dict.items() if int(value) == -1]
    more_list = [key for key, value in compare_result_dict.items() if int(value) > 1]
    
    return match_list, standard_only_list, compare_only_list, more_list

if __name__ == '__main__':
    try:
        match_list, standard_only_list, compare_only_list, more_list = main()
        if standard_only_list:
            for i in sorted(standard_only_list):
                print '''--- %s ''' % i
        if compare_only_list:
            for i in sorted(compare_only_list):
                print '''+++ %s ''' % i
        if more_list:
            for i in sorted(more_list):
                print '''*** %s''' % i
        if not standard_only_list and not compare_only_list and not more_list:
            print '''The two files are the same'''
        if not standard_only_list and (compare_only_list or more_list):
            print '''Compare file contains standard file'''
        sys.exit(0)
    except Exception, e:
        print str(e)
        sys.exit(1)
