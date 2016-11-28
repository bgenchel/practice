"""
Generate every permutation of a string
"""


def _insert_in_each_position(char, string):
    to_ret = []
    for i in xrange(len(string)):
        to_ret.append(string[:i] + char + string[i:])
    to_ret.append(string + char)
    return to_ret


def generate_permutations(string):
    if len(string) < 2:
        return string

    sol = []
    for perm in generate_permutations(string[:-1]):
        sol.extend(_insert_in_each_position(string[-1], perm))
    return sol

if __name__ == '__main__':
    string = raw_input("enter string: ")
    print generate_permutations(string)
