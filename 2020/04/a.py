# TODO
# end passport on new line
# if all 8 fields are correct
# its okay if "cid" is missing
# count

def p1(x):
    requirements = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
    big = 0
    small = 0
    for line in x:
        if line == "":
            if small == 7:
                big+=1
            small=0
        for x in line.split():
            z,a = x.split(":")
            if z in requirements:
                small+=1
    print(big)


with open("input.txt", "r") as FILE:
    x = (y.strip() for y in FILE.readlines())
    p1(x)