# FactoryPlanning for Satisfactory
from Satisfactory import factorycalc
from Satisfactory import gui
from PyQt5.QtWidgets import QApplication
import sys

factory_dict = {}


def new_building(location, building, recipe, clockspeed):
    factory_dict[location] = {'typ': building, 'recipe': recipe, 'quantity': clockspeed}


app = QApplication(sys.argv)
window = gui.Window()
window.show()

new_building('main', 'smelter', 'iron_ingot', 2)
new_building('main', 'smelter', 'iron_ingot', 3)

print(factory_dict)

wantediron = 30

factorycalc.buildings('iron_ingot', wantediron)

sys.exit(app.exec_())
