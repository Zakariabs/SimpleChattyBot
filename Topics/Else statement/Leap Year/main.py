# put your python code here
given_year = int(input())


def leap_year_calc(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        answer = 'Leap'
    else:
        answer = 'Ordinary'
    return answer


output = leap_year_calc(given_year)  # function call with argument a.k given_year
print(output)
