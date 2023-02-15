"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(str):
    result = str
    #...
    count = len(result)
    dash = "-"

    if len(result) % 2 != 0: #>= 3 or "e" in result:
        result.reverse()
        for letter in result:
            n = result.index(letter)
            new_str = f"{letter}{dash}{count}"
            result[n] = new_str
            count -= 1
    else:
       result.reverse()
       for letter in result:
           n = result.index(letter)
           number = f"{count}"
           result[n] = number
           count -= 1
    return result

