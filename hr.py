# def swap_case(s):
#     b=s.swapcase()
#     return b
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)
#

# a=input()
# a=a.replace(" ","-")
# print(a)
#

# def print_full_name(a, b):
#     print("Hello {} {}! You just delved into python.".format(a,b))
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)
#
# def mutate_string(string, position, character):
#     l=list(string)
#     l[position]=character
#     string = ''.join(l)
#     return string
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)
#

def count_substring(string, sub_string):
    string.rfind(sub_string)

    return


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)