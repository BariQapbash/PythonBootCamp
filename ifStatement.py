is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

print("__________________________________________________")
is_rich = False
is_kind = True

if is_rich and is_kind:
    print("You are rich and kind")
elif is_kind and not(is_rich):
    print("You are kind but not rich")
elif is_rich and not(is_kind):
    print("You are rich but not kind")
else:
    print("You neither rich and kind")

