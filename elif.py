is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are not tall male")
elif not(is_male) and is_tall:
    print("you are not a male but and is tall")
else:
    print("you are either a male or a tall")
