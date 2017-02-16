'''
Created on May 7, 2015

@author: zdw3
'''

#Different exceptions tests
try:
    'hi' + 4
except TypeError as bad_code:
    print('dealt with TypError: ', bad_code)
    
try:
    10 / 0
except ArithmeticError as bad_code:
    print('dealt with Ariththmetic Error: ', bad_code)
    
try:
    'person'.find_first('e')
except AttributeError as bad_code:
    print('dealt with AttributeError: ', bad_code)
    
try:
    [0,1,2]['summer']
except TypeError as bad_code:
    print('dealt with TypeError: ', bad_code)
    
try:
    ['hi','there','student'][5]
except IndexError as bad_code:
    print('dealt with IndexError: ', bad_code)
    
try:
    print(name)
except NameError as bad_code:
    print('dealt with NameError: ', bad_code)
    
try:
    9 <= (3, 4)
except TypeError as bad_code:
    print('dealt with TypeError: ', bad_code)
    
try:
    f = open('missingFile.txt')
except FileNotFoundError as bad_code:
    print('dealt with FileNotFoundError: ', bad_code)