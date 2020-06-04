import yaml
import toga

from builder import create_layout

layout_yaml = """
main_box:
  type: Box
  widgets: 
  - label_test:
      type: Label
      text: hola dasdadas nacho
  - button_test:
      type: Button
      label: Soy boton
"""

def button_handler(widget):
    print("hello")

def build(app):
    layout = yaml.load(layout_yaml)
    return create_layout(layout, None)

def main():
    return toga.App('First App', 'org.beeware.helloworld', startup=build)

if __name__ == '__main__':
    main().main_loop()