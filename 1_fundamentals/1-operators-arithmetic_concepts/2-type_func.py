print(f"1) '[1, 2]'\t\tis {type([1, 2]).__name__}")
print(f"2) '(1, 2)'\t\tis {type((1, 2)).__name__}")
print("3) '{1, 2}' " + f"\t\tis {type({1, 2}).__name__}")
print("3) '{'name': 'lucas'}' " + f" is {type({'name': 'lucas'}).__name__}")
""" out >>
1) '[1, 2]'             is list
2) '(1, 2)'             is tuple
3) '{1, 2}'             is set
3) '{'name': 'lucas'}'  is dict
"""