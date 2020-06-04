import yaml
import toga

def create_layout(layout, parent):
    """ recursive and dinamically creates a toga layout

    params:
    - layout: tree dict 
    - parent: parent widget
    """

    if len(layout.keys()) != 1:
        # node of the tree
        raise Exception('Bad Format')
    
    # get id of widget
    name = list(layout.keys())[0]

    # get toga class
    widget_class = getattr(toga, layout[name].get('type'))
    children = layout[name].get('widgets', None)
    
    # get initialization attributes
    attributes = { key:value for (key,value) in layout[name].items() if key not in ['type', 'widgets']}

    # widget instance
    widget = widget_class(id=name, **attributes)

    if parent:
        # add widget to parent
        parent.add(widget)

    if children:
        for child in children:
            # create layout for children
            create_layout(child, widget)

    return widget
