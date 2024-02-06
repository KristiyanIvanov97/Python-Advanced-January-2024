def concatenate(*args, **kwargs):
    text = "".join(args)
    for wrong_word, new_word in kwargs.items():
        text = text.replace(wrong_word, new_word)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
