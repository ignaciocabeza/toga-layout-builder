import toga


class Builder:

    def __init__(self, styles=None, events=None):
        self.styles = styles
        self.events = events

    def create_layout(self, layout, parent):
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

        # get initialization params
        optional = {key: value for (key, value) in layout[name].items() if key not in ['args', 'type', 'widgets', 'style']}

        # sanitase optional parameters
        for key, value in optional.items():
            if 'on_' in key:
                # params starting with _on are converted to a function
                optional[key] = getattr(self.events, value)

        if layout[name].get('style', None):
            optional['style'] = getattr(self.styles, layout[name].get('style'))

        # get positional params
        # TODO: Improve this if
        if layout[name].get('args', None):
            widget = widget_class(*layout[name].get('args'), id=name, **optional)
        else:
            widget = widget_class(id=name, **optional)

        if parent:
            # add widget to parent
            parent.add(widget)

        if children:
            for child in children:
                # create layout for children
                self.create_layout(child, widget)

        return widget
