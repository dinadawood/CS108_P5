"""
Course: CISC108
Assignment: Project 5
Author: Dina Dawood
"""

from cisc108 import assertEqual

'''
- Ada checks if students are submitting before due date
- Each submission includes a submission date (string) ex. (October 3rd, 2020) -> "10/3/2020"
- Returns bool of true or false if submitted before due date
- Cannot use the < > signs, don't work
'''

# Helper Functions:

def parse_date_month(string):
    '''
    Consumes a string of a single date & produces an int representing month (-1 if not 1-12)
    Parameter:
        string: (str) - random int between 1-12 for month
    Returns:
       month: (int) 
    '''
    month_str = string[0:string.index("/")]
    if month_str.isdigit() == False:
        return -1
    month = int(month_str)
    if (month >= 1) and (month <= 12):
        return month
    return -1

def parse_date_day(string):
    '''
    Consumes a string of a single date & produces an int representing day (-1 if not 1-31)
    Parameter:
        string: (str) - random int between 1-31 for day
    Returns:
        day: (int)
    '''
    first_slash = string.index("/")
    second_slash = string.index("/", first_slash + 1)
    day_str = string[first_slash + 1: second_slash]
    if day_str.isdigit() == False:
        return -1
    day = int(day_str)
    if (day >= 1) and (day <= 31):
        return day
    return -1

def parse_date_year(string):
    '''
    Consumes a string of a single date & produces an int representing year
    (-1 if not 2 or 4 digit)
    Parameter:
        string: (str) - random int for year (2 or 4 digits only)
    Returns:
        year: (int)
    '''
    first_slash = string.index("/")
    second_slash = string.index("/", first_slash + 1)
    year_str = string[second_slash + 1: len(string)]
    if year_str.isdigit() == False or (len(year_str) != 2 and len(year_str) != 4) :
        return -1
    year = int(year_str)
    if year == 0:
        return -1
    if year < 100:
        year = 2000 + year
    return year

def is_date(string):
    '''
    Consumes a string of a single date & produces an bool representing valid date
    Parameter:
        string: (str) - date produced from previous functions
    Returns:
        valid_date: (bool)
    '''
    return parse_date_month(string) != -1 and parse_date_day(string) != -1 and parse_date_year(string) != -1


###################################################################################

def earlier(date1, date2):
    '''
    Consumes 2 string of dates & produces a string 
    Parameter:
        date1: (str) - random string of date 1
        date2: (str) - random string of date 2
    Returns:
        earlier_date: (str)
    '''
    if (is_date(date1) == False) or (is_date(date2)) == False:
        return "error"
    first_date_year = parse_date_year(date1)
    second_date_year = parse_date_year(date2)
    if first_date_year < second_date_year:
        return "First date"
    elif first_date_year > second_date_year:
        return "Second date"
    else:
        first_date_month = parse_date_month(date1)
        second_date_month = parse_date_month(date2)
        if first_date_month < second_date_month:
            return "First date"
        elif first_date_month > second_date_month:
            return "Second date"
        else:
            first_date_day = parse_date_day(date1)
            second_date_day = parse_date_day(date2)
            if first_date_day < second_date_day:
                return "First date"
            elif first_date_day > second_date_day:
                return "Second date"
            else:
                return "equal"

###################################################################################

# Unit Testing:

## parse_date_month
    
assertEqual(parse_date_month("1/1/2020"), 1)
assertEqual(parse_date_month("1/12/2045"), 1)
assertEqual(parse_date_month("10/9/1998"), 10)
assertEqual(parse_date_month("10/30/2010"), 10)
assertEqual(parse_date_month("2/30/2001"), 2)
assertEqual(parse_date_month("10/30/15"), 10)
assertEqual(parse_date_month("01/2/05"), 1)
assertEqual(parse_date_month("12/31/9999"), 12)
assertEqual(parse_date_month("13/1/2013"), -1)
assertEqual(parse_date_month("0/0/0000"), -1)
assertEqual(parse_date_month("22/32/2015"), -1)
assertEqual(parse_date_month("/32/1246"), -1)

## parse_date_day

assertEqual(parse_date_day("1/2/2020"), 2)
assertEqual(parse_date_day("1/12/2026"), 12)
assertEqual(parse_date_day("10/9/1998"), 9)
assertEqual(parse_date_day("10/30/2222"), 30)
assertEqual(parse_date_day("2/30/2010"), 30)
assertEqual(parse_date_day("10/30/15"), 30)
assertEqual(parse_date_day("01/2/05"), 2)
assertEqual(parse_date_day("12/31/9999"), 31)
assertEqual(parse_date_day("5//2020"), -1)
assertEqual(parse_date_day("0/0/0000"), -1)
assertEqual(parse_date_day("1/32/2011"), -1)
assertEqual(parse_date_day("13/45/2017"), -1)

## parse_date_year

assertEqual(parse_date_year("1/1/2020"), 2020)
assertEqual(parse_date_year("1/12/1945"), 1945)
assertEqual(parse_date_year("10/9/1998"), 1998)
assertEqual(parse_date_year("10/30/2010"), 2010)
assertEqual(parse_date_year("2/30/2002"), 2002)
assertEqual(parse_date_year("10/30/15"), 2015)
assertEqual(parse_date_year("01/2/05"), 2005)
assertEqual(parse_date_year("12/31/9999"), 9999)
assertEqual(parse_date_year("1/1/105"), -1)
assertEqual(parse_date_year("5/23/"), -1)
assertEqual(parse_date_year("06/33/0"), -1)
assertEqual(parse_date_year("0/0/0000"), -1)

## earlier

assertEqual(earlier("0/0/0000", "02/10/105"), "error")
assertEqual(earlier("06/31/3000", "12/26/2499"), "Second date")
assertEqual(earlier("7/04/15", "10/30/1766"), "Second date")
assertEqual(earlier("05/20/74", "9/4/99"), "First date")
assertEqual(earlier("2/15/2000", "2/15/2000"), "equal")
assertEqual(earlier("03/29/2019", "11/07/2004"), "Second date")
assertEqual(earlier("13/12/1", "04/32/999"), "error")
assertEqual(earlier("07/22/22", "4/22/2038"), "First date")
assertEqual(earlier("06/12/2000", "08/31/1999"), "Second date")
assertEqual(earlier("1/18/1945", "1/18/1945"), "equal")
assertEqual(earlier("10/29/8934", "08/18/9990"), "First date")
assertEqual(earlier("11/09/1200", "12/30/1925"), "First date")

# Main Function

if __name__ == "__main__":
    ## Trial
    print(parse_date_month("01/22/2024"))
    print(parse_date_day("01/22/2024"))
    print(parse_date_year("01/22/99"))
    print()
    
    ## parse_date_month
    
    print(parse_date_month("1/1/2020"))
    print(parse_date_month("1/12/2045"))
    print(parse_date_month("10/9/1998"))
    print(parse_date_month("10/30/2010"))
    print(parse_date_month("2/30/2001"))
    print(parse_date_month("10/30/15"))
    print(parse_date_month("01/2/05"))
    print(parse_date_month("12/31/9999"))
    print(parse_date_month("13/1/2013"))
    print(parse_date_month("0/0/0000"))
    print(parse_date_month("22/32/2015"))
    print(parse_date_month("/32/1246"))
    print()

    ## parse_date_day

    print(parse_date_day("1/2/2020"))
    print(parse_date_day("1/12/2026"))
    print(parse_date_day("10/9/1998"))
    print(parse_date_day("10/30/2222"))
    print(parse_date_day("2/30/2010"))
    print(parse_date_day("10/30/15"))
    print(parse_date_day("01/2/05"))
    print(parse_date_day("12/31/9999"))
    print(parse_date_day("5//2020"))
    print(parse_date_day("0/0/0000"))
    print(parse_date_day("1/32/2011"))
    print(parse_date_day("13/45/2017"))
    print()

    ## parse_date_year

    print(parse_date_year("1/1/2020"))
    print(parse_date_year("1/12/1945"))
    print(parse_date_year("10/9/1998"))
    print(parse_date_year("10/30/2010"))
    print(parse_date_year("2/30/2002"))
    print(parse_date_year("10/30/15"))
    print(parse_date_year("01/2/05"))
    print(parse_date_year("12/31/9999"))
    print(parse_date_year("1/1/105"))
    print(parse_date_year("5/23/"))
    print(parse_date_year("06/33/0"))
    print(parse_date_year("0/0/0000"))
    print()
    
    ## earlier
    
    print(earlier("0/0/0000", "02/10/105"))
    print(earlier("06/31/3000", "12/26/2499"))
    print(earlier("7/04/15", "10/30/1766"))
    print(earlier("05/20/74", "9/4/99"))
    print(earlier("2/15/2000", "2/15/2000"))
    print(earlier("03/29/2019", "11/07/2004"))
    print(earlier("13/12/1", "04/32/999"),)
    print(earlier("07/22/22", "4/22/2038"),)
    print(earlier("06/12/2000", "08/31/1999"),)
    print(earlier("1/18/1945", "1/18/1945"))
    print(earlier("10/29/8934", "08/18/9990"))
    print(earlier("11/09/1200", "12/30/1925"))
