def question_1(name: str) -> str:
    """
    Takes in string and returns concatenated string.

    Parameters:
    * name - string

    Returns:
    "Hello my name is" plus the * name string.
    """
    return "Hello my name is " + name

def question_2(name: str) -> str:
    """
    Takes in string and returns concatenated string capitalized.

    Parameters:
    * name - string

    Returns:
    "My first name is" plus the *name string capitalized.
    """
    return "Hello my name is " + name.capitalize()

def question_3(name: str) -> str:
    """
    Takes in string and returns concatenated string.

    Parameters:
    * name - string

    Returns:
    "My first name is" plus the *name string.
    """
    return "My first name is " + name

def question_4(name: str) -> str:
    """
    Takes in string and returns concatenated and capitalized string.

    Parameters:
    * name - string

    Returns:
    "My first name is" plus the *name string capitalized.
    """
    return "My first name is " + name.capitalize()

def question_5(first_name: str, last_name: str) -> str:
    """
    Takes in two strings and returns concatenated strings.

    Parameters:
    * first_name - string
    * last_name - string

    Returns:
    "My full name is" + first_name + last_name.
    """
    return "My full name is " + first_name + last_name

def question_6(first_name: str, last_name: str) -> str:
    """
    Takes in two strings and returns concatenated string.

    Parameters:
    * first_name - string
    * last_name - string

    Returns:
    "My full name is" plus capitalization of first_name and last_name
    """
    return "My full name is " + first_name.capitalize() + last_name.capitalize()

def question_7(lower_string: str) -> str:
    """
    Takes in string and returns indices of string that are lower case.

    Parameters:
    * lower_string - string

    Returns:
    Indices of the string that are lowercase.
    """
    newString = []
    for i,n in enumerate(lower_string):
        if n.islower():
            newString.append(str(i))
    return newString

def question_8(upper_string: str) -> str:
    """
    Takes a string and returns the indices of the string that are upper case.

    Parameters:
    * upper_string - str

    Returns:
    Indices of the string that are upper case.
    """
    newString = []
    for i,n in enumerate(upper_string):
        if n.isupper():
            newString.append(str(i))
    return newString

def question_9(white_string: str) -> str:
    """
    Takes in a string and returns indices of string that are white spaces.

    Parameters:
    * white_string - string

    Returns:
    Indices of string that are white spaces.
    """
    newString = []
    for i,n in enumerate(white_string):
        if n.isspace():
            newString.append(str(i))
    return newString

def question_10(distinct_string: str) -> int:
    """
    Takes in a string and returns number of distinct words in string.

    Parameters:
    * distinct_string - string

    Returns:
    Number of distinct words in the string.
    """
    return len(distinct_string.split(" "))

def question_11(int_string: str) -> int:
    """
    Takes in a string and returns the number of integers in the string.

    Parameters:
    * int_string - string

    Returns:
    Number of integers in the string.
    """
    counter = 0
    for i in int_string:
        if i.isdigit():
            counter += 1
        else:
            continue
    return counter

def question_12(one_string: str, two_string: str) -> str:
    """
    Takes in two strings and concatenates them.

    Parameters:
    * one_string - string
    * two_string - string

    Returns:
    Concatenation of the two strings.
    """
    return one_string + two_string

def question_13(one_string: str, two_string: str) -> str:
    """
    Takes in two strings and capitalizes and concatenates them.

    Parameters:
    * one_string - string
    * two_string - string

    Returns:
    Capitalizes and concatenates the two strings.
    """
    return one_string.capitalize() + two_string.capitalize()

def question_14(replace_string: str) -> str:
    """
    Takes in a string and replaces spaces with "_"

    Parameters:
    * replace_string - string

    Returns:
    String but replacing spaces with "_"
    """
    return replace_string.replace(" ", "_")

def question_15(list_str: str) -> str:
    """
    Takes in a list of strings and returns the longest word.

    Parameters:
    * list_str - list of strings

    Returns:
    Longest string/word.
    """
    return max(list_str, key=len)

def question_16(list_str: str) -> str:
    """
    Takes in a list of strings and returns the shortest word.

    Parameters:
    * list_str - list of strings

    Returns:
    Shortest word/string
    """
    return min(list_str, key=len)

def question_17(list_str: str) -> float:
    """
    Takes in list of strings and returns average word length

    Parameters:
    * list_str - string

    Returns:
    Average word length.
    """
    return sum(len(i) for i in list_str) / len(list_str)

def question_18(list_str: str) -> int:
    """
    Takes in list of string and return median word length

    Parameters:
    * list_str - strings

    Returns:
    Median word length
    """
    return int(sum(len(i) for i in list_str) / len(list_str))

def question_19(list_num: int) -> int:
    """
    Takes in list of integers and returns even integers.

    Parameters:
    * list_num - integers

    Returns:
    Even integers
    """
    return [i for i in list_num if i % 2 == 0]

def question_20(list_num: int) -> int:
    """
    Takes in list of ints and returns odd ints.

    Parameters:
    * list_num - integers

    Returns:
    Odd Integers
    """
    return [i for i in list_num if i % 2 == 1]

def question_21(list_num: float) -> float:
    """
    Takes list of numbers and returns 3 largest numbers

    Parameters:
    * list_num - floats

    Returns:
    3 largest numbers
    """
    list_num.sort(reverse=True)
    return list_num[0:3]

def question_22(list_num: float) -> float:
    """
    Takes list of numbers and returns 3 smallest numbers

    Parameters:
    * list_num - floats

    Returns:
    3 smallest numbers.
    """
    list_num.sort()
    return list_num[0:3]

def question_23(list_num: float) -> float:
    """
    Takes list of numbers and returns the mean.

    Parameters:
    * list_num - floats

    Returns:
    Mean
    """
    return sum(list_num) / len(list_num)

def question_24(list_num: int) -> int:
    """
    Takes list of numbers and returns the mode

    Parameters:
    * list_num - Integers

    Returns:
    Mode
    """
    return max(list_num, key=list_num.count)

def question_25(list_num: int) -> int:
    """
    Takes list of numbers and returns the list in reverse.

    Parameters:
    * list_num - list of integers

    Returns:
    List in reverse order.
    """
    list_num.reverse()
    return list_num

def question_26(list_num: int) -> int:
    """
    Takes in list of numbers and returns cumulative sum.

    Parameters:
    * list_num - list of integers

    Returns:
    Cumulative sum.
    """
    return sum(list_num)

def question_27(list_num: int) -> int:
    """
    Takes in list of integers and returns the difference between each adjacent
    number.

    Paramters:
    * list_num - list of integers.

    Returns:
    Difference between each adjacent number.
    """
    return [abs(list_num[i+1] - list_num[i]) for i,v in enumerate(list_num) if
         i <= len(list_num) - 2]

def question_28(x: int) -> int:
    """
    This is a recursive function that takes in an integer and returns
    F[n-1] + F[n-3].

    Parameters:
    * x - integer

    Returns:
    List of numbers that follow the recursive function.
    """
    # Base cases below:
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 1
    # Recursive function below:
    else:
        return question_28(x-1) + question_28(x-3)

def question_29(x: int) -> int:
    """
    A recursive function that returns
    F[n-1] * F[n-2] * F[n-3] * ... * 2 * 1

    Parameters:
    * x - integer

    Returns:
    List of integers that follows the recursive function.
    """
    # Base case below:
    if x == 0:
        return 1
    # Recursive function below:
    else:
        result = 1
        while x > 0:
            for i in range(x):
                result *= question_29(i)
                x -= 1
        return result * 2 * 1

def question_30(x: int) -> int:
    """
    A recursive function that returns as its nth case
    2^F[n-1] * 2^F[n-2] * 2^F[n-3] * ... * 2^2 * 2*1 * 2^0

    Parameters:
    * x - integer

    Returns:
    Integers that follow the recursive function.
    """
    # Base case below:
    if x == 0:
        return 1
    # Recursive function below:
    else:
        result = 1
        while x > 0:
            for i in range(x):
                result *= 2 ** question_30(i)
                x -= 1
        return result
