import yaml
import toga
from toga_layout import Builder
from toga.style.pack import Pack, COLUMN, ROW

import styles
import events


def button_handler(widget):
    print("hello")


def build(app):
    builder = Builder()
    builder.styles = [styles]
    builder.events = [events]
    return builder.load('./example/layout.yaml')

def main():
    return toga.App('Calculator', 'org.beeware.helloworld', startup=build)


if __name__ == '__main__':
    main().main_loop()
