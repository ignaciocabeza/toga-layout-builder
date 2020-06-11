[![PyPI version](https://badge.fury.io/py/toga-layout-builder.svg)](https://badge.fury.io/py/toga-layout-builder)

# Toga Layout Builder

The purpose of this project is to create user interfaces easily with a yaml document.
This is an unofficial tool for Toga GUI Toolkit.

## Install

```
pip install toga-layout-builder
```

## Use

* Create Toga App in `app.py`
```python
import toga
from toga_layout import Layout

import myevents
import mystyles

def main():
    layout = Layout()
    layout.events = [myevents]
    layout.styles = [mystyles]
    widgets = layout.load('layout.yaml')
    return toga.App('Example Layout App', 'org.ignaciocabeza.example_layout_app', startup=widgets)

if __name__ == '__main__':
    main().main_loop()
```
* Create app layout in `layout.yaml`
```yaml
main_box:
    type: Box   
    style: ["padding_10","column_dir"]
    widgets:
        - box_row_1:
            type: Box
            style: padding_bottom_5
            widgets:
                - label_info:
                    type: Label
                    style: ['padding_top_5', 'flex1']
                    args: ['Insert your name here:']
                - text_name:
                    type: TextInput
                    style: 'flex1'
        - btn_greetings:
            type: Button
            style: "padding_bottom_5"
            on_press: handle_greetings
            args: ["Greetings"]
        - response_greetings:
            type: Label
            style: flex1
            args: [""]
```
* Create events file in `myevents.py`
```python
from toga_layout import Layout, get_widget_by_id

def handle_greetings(Button):
    response_greetings = get_widget_by_id(Button.window, 'response_greetings')
    txt_name = get_widget_by_id(Button.window, 'text_name')
    response_greetings.text = f'Hello {txt_name.value}!'
```

* Create styles file in `mystyles.py`
```python
from toga.style.pack import Pack, COLUMN, ROW

padding_10 = Pack(padding=10)
padding_bottom_5 = Pack(padding_bottom=5)
padding_top_5 = Pack(padding_top=5)
column_dir = Pack(direction=COLUMN)
flex1 = Pack(flex=1)
```
* Run app
```
python app.py
```

More examples at: https://github.com/ignaciocabeza/toga-layout-builder/tree/master/example.

## YAML Layout reference and examples

`mywidget = toga.Widget(arg1, arg2, optional1=value1, optional2=value2)`

Replace in yaml with: 
```yaml
mywidget:
    type: Widget
    args: [arg1, arg2]
    optional1: value1
    optional2: value2
```

Example:

`mybutton = toga.Button('Click me!', on_press=myhandler)`

Yaml:
```yaml
mybutton:
    type: Button
    args: ["Click me!"]
    on_press: myhandler
```

### Add multiple styles

Your `style.py` file
```python

from toga.style.pack import Pack

padding_left10 = Pack(padding_left=10)
flex1 = Pack(flex=1)
```

Mix styles in your `layout.yaml`:
```yaml
mybutton:
    type: Button
    style: ["padding_left10", "flex1"]
    args: ["Click me!"]
    on_press: myhandler
```

This line `style: ["padding_left10", "flex1"]` is the same than doing: `Pack(padding_left=10, flex=1)`

### Children widgets

```yaml
my_container:
    type: Box
    widgets: 
        - mybutton:
            type: Button
            args: ["Click me!"]
        - mylabel:
            type: Label
            args: ["I'm a label"]
```

### Special cases

#### OptionContainer

For OptionContainer, a special attribute `label` has to be placed in all children.

```yaml
my_option_container:
    type: OptionContainer
    widgets:
        - option1:
            type: Box
            label: Option 1 Title # <---
        - option2:
            type: Box
            label: Option 2 Title # <---
```