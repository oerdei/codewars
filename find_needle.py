def find_needle(haystack):
    for str in haystack :
        if str == "needle":
            index = haystack.index("needle")
            return f'found the needle at position {index}'
            
haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(haystack))