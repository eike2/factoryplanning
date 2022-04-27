"""recipe for iron ingots"""


def iron_ingot(num):
    building_num = num / 30
    return "smelter", building_num, num


def pure_iron_ingot(num):
    building_num = num / 65
    ironore = (35 / 65) * num
    water = (20 / 65) * num
    return "refinery", building_num, ironore, "water", water


def iron_alloy_ingot(num):
    building_num = num / 50
    ironore = (35 / 50) * num
    copperore = (20 / 50) * num
    return "refinery", building_num, ironore, "water", copperore
