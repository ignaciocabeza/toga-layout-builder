from toga_layout import get_widget_by_id

def button_handler(Button):
    print('I was pressed')
    text = get_widget_by_id(Button.window, 'text')
    text.value = "I was completed"

def handler_onselect(*args, **kwargs):
    pass