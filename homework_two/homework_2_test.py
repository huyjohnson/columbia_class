import question_one
import question_two
import question_three
import question_four
import question_five
import question_six
import question_seven
import question_eight
import question_nine
import question_ten
import question_11
import question_12
import question_13
import question_14
import question_15
import question_16
import question_17
import question_18
import question_19
import question_20
import question_21
import question_22
import question_23
import question_24
import question_25
import question_26
import question_27
import question_28
import question_29

def answer_one():
    counter = 0
    value = 5
    while value <= 10:
        value += 1
        counter += 1
    return value, counter

def test_question_one():
    value, counter = answer_one()
    assert question_one.value == value
    assert question_one.counter == counter

def answer_two():
    counter = 0
    value = 2
    while value <= 120:
        value += 2
        counter += 1
    return value, counter

def test_question_two():
    value, counter = answer_two()
    assert question_two.value == value
    assert question_two.counter == counter

def answer_three():
    counter = 0
    value = -50
    while value >= -100:
        value -= 1
        counter += 1
    return value, counter

def test_question_three():
    value, counter = answer_three()
    assert question_three.value == value
    assert question_three.counter == counter

def answer_four():
    counter = 0
    value = 7
    while value <= 1e7:
        value *= (value/2)
        counter += 1
    return value, counter

def test_question_four():
    value, counter = answer_four()
    assert question_four.value == value
    assert question_four.counter == counter

def answer_five():
    counter = 0
    value = 10000
    while value > 1:
        value -= (value/2)
        counter += 1
    return value, counter

def test_question_five():
    value, counter = answer_five()
    assert question_five.value == value
    assert question_five.counter == counter

def answer_six():
    listing = [0,1,2]
    result = listing[2]
    return listing, result

def test_question_six():
    listing, result = answer_six()
    assert question_six.listing == listing
    assert question_six.result == result

def answer_seven():
    listing = [0,1,2]
    result = listing[-1]
    return listing, result

def test_question_seven():
    listing, result = answer_seven()
    assert question_seven.listing == listing
    assert question_seven.result == result

def answer_eight():
    listing = ["A", 1, 7]
    result = listing[0]
    result = result.lower()
    return listing, result

def test_question_eight():
    listing, result = answer_eight()
    assert question_eight.listing == listing
    assert question_eight.result == result

def answer_nine():
    listing = ["aloha", 1, 7]
    result = listing[0]
    result = result.capitalize()
    return listing, result

def test_question_nine():
    listing, result = answer_nine()
    assert question_nine.listing == listing
    assert question_nine.result == result

def answer_ten():
    import random
    listing = [random.randint(0, 10)
               for _ range(10000)]
    listing.sort()
    result = listing[0]
    return listing, result

def test_question_ten():
    listing, result = answer_ten()
    assert len(question_ten.listing) == len(listing)
    assert set(question_ten.listing) == set(listing)
    assert question_ten.result == result

def answer_11():
    listing = [value for value in range(2, 100)]
    return listing

def test_question_11():
    listing = answer_11()
    assert question_11.listing == listing

def answer_12():
    listing = [value
               for value in range(2, 100)
               if value % 2 == 0]
    return listing

def test_question_12():
    listing = answer_12()
    assert question_12.listing == listing

def answer_13():
    listing = [value
               for value in range(2, 100)
               if value % 2 == 1]
    return listing

def test_question_13():
    listing = answer_13()
    assert question_13.listing == listing

def answer_14():
    listing = [value
               for value in range(2, 100)
               if (value % 15 != 0) and
               ((value % 3 == 0) or (value % 5 == 0))]
    return listing

def test_question_14():
    listing = answer_14()
    assert question_14.listing == listing

def answer_15():
    listing = [value for value in range(100, 5, -1)]
    return listing

def test_question_15():
    listing = answer_15()
    assert question_15.listing == listing

def answer_16():
    dicter = {key: True
              for key in range(2, 100)}
    return dicter

def test_question_16():
    dicter = answer_16()
    assert question_16.dicter == dicter

def answer_17():
    dicter = {key: key < 10
              for key in range(2, 100)}
    return dicter

def test_question_17():
    dicter = answer_17()
    assert question_17.dicter == dicter

def answer_18():
    dicter = {key: key % 2 == 0
              for key in range(2, 100)}
    return dicter

def test_question_18():
    dicter = answer_18()
    assert question_18.dicter == dicter

def answer_19():
    dicter = {key: key % 2 == 1
              for key in range(2, 100)}
    return dicter

def test_question_19():
    dicter = answer_19()
    assert question_19.dicter == dicter

def answer_20():
    dicter = {key: (key % 7 == 0) or (key % 17 == 0)
              for key in range(2, 100)}
    return dicter

def test_question_20():
    assert question_20.result == "charles in charge".index(" ")

def answer_21():
    dicter = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }
    return dicter

def test_question_21():
    dicter = answer_21()
    assert question_21.dicter == dicter

def answer_22():
    dicter = {key: key+1
              for key in range(0, 100)}
    return dicter

def test_question_22():
    dicter = answer_22()
    assert question_22.dicter == dicter

def answer_23():
    dicter = {key: key*2
              for key in range(0, 100)}
    return dicter

def test_question_23():
    dicter = answer_23()
    assert question_23.dicter == dicter

def answer_24():
    primes = [
        2, 3, 5, 7, 11, 13,
        17, 19, 23, 29, 31,
        37, 41, 43, 47, 53,
        59, 61, 67, 71, 73,
        79, 83, 89, 97
    ]
    keys = list(range(0, 100))
    dicter = {}.fromkeys(keys)
    for key in dicter:
        prime_factors = []
        for prime in primes:
            if key % prime == 0:
                prime_factors.append(prime)
            if prime_factors == []:
                dicter[key] = 1
            else:
                dicter[key] = max(prime_factors)
    return dicter

def test_question_24():
    dicter = answer_24()
    assert question_24.dicter == dicter

def answer_25():
    primes = [
        2, 3, 5, 7, 11, 13,
        17, 19, 23, 29, 31,
        37, 41, 43, 47, 53,
        59, 61, 67, 71, 73,
        79, 83, 89, 97
    ]
    keys = list(range(0, 100))
    dicter = {}.fromkeys(keys)
    for key in dicter:
        prime_factors = []
        for prime in primes:
            if key % prime == 0:
                prime_factors.append(prime)
            if prime_factors == []:
                dicter[key] = 1
            else:
                dicter[key] = min(prime_factors)
    return dicter

def test_question_25():
    dicter = answer_25()
    assert question_25.dicter == dicter

def answer_26():
    import random
    listing = [random.randint(0, 10)
               for _ in range(10000)]
    return list(set(listing))

def test_question_26():
    listing = answer_26()
    assert question_26.listing == listing

def answer_27():
    import random
    listing = [random.randint(0, 10)
               for _ in range(10000)]
    result = []
    for value in listing:
        if value not in result:
            result.append(value)
    return result

def test_question_27():
    result = answer_27()
    assert question_27.result == result

def answer_28():
    import random
    listing = [random.randint(0, 10)
               for _ in range(10000)]
    uniques = list(set(listing))
    value_counts = {}.fromkeys(uniques, 0)
    for value in listing:
        value_counts[value] += 1
    return value_counts

def test_question_28():
    value_counts = answer_28()
    assert question_28.value_counts == value_counts

def answer_29():
    import random
    listing = [random.randint(0, 10)
               for _ in range(10000)]
    uniques = list(set(listing))
    value_counts = {}.fromkeys(uniques, 0)
    for value in listing:
        value_counts[value] += 1
    value_ratios = {}
    for key in value_counts:
        value_ratios[key] = value_counts[key]/len(listing)
    return value_ratios

def test_question_29():
    value_ratios = answer_29()
    your_keys = list(question_29.value_ratios.keys())
    correct_keys = list(value_ratios.keys())
    your_keys.sort()
    correct_keys.sort()
    assert your_keys == correct_keys
