"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(str):
    result = str
    #...
    letter_remove = {"a":"", "o":"", "i":"", "u":""}

    for old_letter, new_letter in letter_remove.items():
        result = result.replace(old_letter, new_letter)
           
    return result
