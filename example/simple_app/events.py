from toga_layout import Layout, get_widget_by_id

def handle_greetings(Button):
    response_greetings = get_widget_by_id(Button.window, 'response_greetings')
    txt_name = get_widget_by_id(Button.window, 'text_name')
    response_greetings.text = f'Hello {txt_name.value}!'