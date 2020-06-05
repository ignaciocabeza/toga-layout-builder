import yaml
import toga
from toga_layout import Builder

import styles
import events

layout_yaml = """
main_box:
  type: Box
  style: main_box_style
  widgets:
  - label_test:
      type: Label
      args: ["I'm a label"]
  - button_test:
      type: Button
      args: ["I'm a button"]
      on_press: button_handler
"""


def button_handler(widget):
    print("hello")


def build(app):
    layout = yaml.load(layout_yaml)
    builder = Builder(styles=styles, events=events)
    return builder.create_layout(layout, None)

    
def main():
    return toga.App('First App', 'org.beeware.helloworld', startup=build)


if __name__ == '__main__':
    main().main_loop()
