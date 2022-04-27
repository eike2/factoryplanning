from Satisfactory import recipe


def buildings(chrecipe, num):
    x = getattr(recipe, chrecipe)(num)
    print(x)
