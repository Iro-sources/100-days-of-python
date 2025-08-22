
def subtractProductAndSum(n):
    product = 1
    total_sum = 0

    while n > 0:
        digit = n % 10
        product *= digit
        total_sum += digit
        n //= 10

    return product - total_sum

print(subtractProductAndSum(234))



#Write a Python function called love_calc that takes two names as parameters.
def love_calc(name1, name2):

    #Initialize two counters:
    count_t = 0
    count_l = 0

    #You need to count the letters from both names combined, case-insensitive.
    combined_names = name1 + name2
    for letters in combined_names:
        if letters in "true".lower():
            count_t +=1

    for letters in combined_names:
       if letters in "love".lower():
           count_l += 1

#Print the counts as a two-digit number, where the first digit is count_t and the second digit is count_l.
    print(str(count_t) + str(count_l))

love_calc("mohamed", "qureysha")




