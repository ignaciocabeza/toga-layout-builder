import toga
from toga_layout import Layout

import events
import styles

def build(app):
    layout = Layout()
    layout.styles = [styles]
    layout.events = [events]
    return layout.load('./example/simple_app/simple_app.yaml')

def main():
    return toga.App('Simple Layout App', 'org.ignaciocabeza.simple_layout_app', startup=build)


if __name__ == '__main__':
    main().main_loop()
