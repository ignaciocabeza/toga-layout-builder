import yaml
import toga
from toga_layout import Layout
from toga.style.pack import Pack, COLUMN, ROW

import styles
import events

def build(app):
    layout = Layout()
    layout.styles = [styles]
    layout.events = [events]
    return layout.load('./example/layout.yaml')

def main():
    return toga.App('Example Layout App', 'org.ignaciocabeza.example_layout_app', startup=build)


if __name__ == '__main__':
    main().main_loop()
