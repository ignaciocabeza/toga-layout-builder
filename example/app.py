import yaml
import toga
from toga_layout import Layout
from toga.style.pack import Pack, COLUMN, ROW

import styles
import events


def button_handler(widget):
    print("hello")


def build(app):
    layout = Layout()
    layout.styles = [styles]
    layout.events = [events]
    return layout.load('./example/layout.yaml')

def main():
    return toga.App('Calculator', 'org.beeware.helloworld', startup=build)


if __name__ == '__main__':
    main().main_loop()
