def age_assignment(*names, **age):
    result = []
    for letter, age in age.items():
        for name in names:

            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break
    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
