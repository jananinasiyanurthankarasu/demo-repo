is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are male but not tall")
elif not (is_male) and is_tall:
    print("You are not male and is tall")
else:
    print("You are not a tall male")
