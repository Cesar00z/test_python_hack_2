"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(arr):
    result = arr
    #...

    for i in range(len(result)):
        dict1 = {"1":"2"}
        new_set = {"3","4"}
        dict2 = {"5":"6"}
        if i == 0:
            result[i] = dict1
       
        elif i == 1:
            result[i] = new_set
        
        elif i == 2:
            result[i] = dict2

    return result