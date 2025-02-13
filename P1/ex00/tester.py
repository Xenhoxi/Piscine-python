from give_bmi import give_bmi, apply_limit

try:
    height = [5, 9, 6]
    weight = [165.3, 38.4, 8]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 24))
except AssertionError as msg:
    print(msg)
