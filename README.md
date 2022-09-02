# 0xMenu  <img width="60px" src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif">

A Handy Package to Create 3 Different types of Menus : ArrowKeyMenu will allow you to create interactive menus using the keyboard arrow key or vim j/k, NumberMenu will create simple menus where the user have to type the index, and finally CheckBox will allow you to create multiple choice menu

# Installation :

From pip :

```bash
pip3 install oxmenu
```

From source :

```bash
git clone https://github.com/0x68616469/oxmenu/
```

### Requirements :

[oxansi](https://github.com/0x68616469/oxansi/)
(downloaded automatically with pip)

# Example :

### ArrowKeyMenu :

```python
from oxmenu import ArrowKeyMenu
menu = ArrowKeyMenu(title="My Menu", subtitle="My Subtitle")

menu.add("One")
menu.add("Two")
menu.add("Three")
menu.add("Four")

selected = menu.select()

print(f"Selected : {selected}")
```

Result :

<img src="https://media.giphy.com/media/QeeUeXoDYwRV2siLdD/giphy.gif">

### NumberMenu :

```python
from oxmenu import NumberMenu
menu = NumberMenu(title="My Menu", subtitle="My Subtitle", input_message="Please choose an option : ")

menu.add("One")
menu.add("Two")
menu.add("Three")
menu.add("Four")

selected = menu.select()

print(f"Selected : {selected}")
```

Result :

<img src="https://media.giphy.com/media/uGe0eFmxJHA3OBgIHP/giphy.gif">

### CheckBox :

```python
from oxmenu import CheckBox
menu = CheckBox(title="My Menu", subtitle="My Subtitle", min_options=1, max_options=2)

menu.add("One")
menu.add("Two")
menu.add("Three")
menu.add("Four")

selected = menu.select()

print(f"Selected : {selected}")
```

Result :

<img src="https://media.giphy.com/media/x6910ZubB4PfZWDhGl/giphy.gif">

<hr>

![Follow me](https://img.shields.io/badge/-Follow%20Me-222222?logo=twitter&logoColor=black&color=272838&labelColor=C09891&style=for-the-badge&logoWidth=30&link=https://twitter.com/0x68616469)