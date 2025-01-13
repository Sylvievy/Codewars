'''
Convert boolean values to strings 'Yes' or 'No'.
8kyu
2 years ago
'''

def bool_to_word(boolean):
    if boolean==True:
        return 'Yes'
    if boolean==False:
        return 'No'
    
bool_to_word(True)
bool_to_word(False)
