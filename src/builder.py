import yaml
import toga

def create_layout(layout, parent):
    """ receives a layout dict and a parent """

    if len(layout.keys()) != 1:
        raise Exception('Bad Format')

    name = list(layout.keys())[0]
    widget_class = getattr(toga, layout[name].get('type'))
    children = layout[name].get('widgets', None)
    
    attributes = { key:value for (key,value) in layout[name].items() if key not in ['type', 'widgets']}
    widget = widget_class(id=name, **attributes)

    if parent:
        parent.add(widget)

    if children:
        for child in children:
            create_layout(child, widget)

    return widget
