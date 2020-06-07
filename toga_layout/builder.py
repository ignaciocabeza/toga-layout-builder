import toga
import yaml


class Builder:

    def __init__(self, layout = None):
        self._styles = []
        self._events = []

    def load(self, layout_path):
        layout_file = open(layout_path, 'r')
        with layout_file as f:
            self.layout = yaml.load(f.read())
            return self.create_layout(self.layout)

    @property
    def styles(self):
        return self._styles

    @styles.setter
    def styles(self, styles):
        self._styles = styles

    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, events):
        self._events = events

    def create_layout(self, layout, parent=None):
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
        optional = {key: value for (key, value) in layout[name].items() if key not in ['args', 'type', 'widgets']}

        # sanitase optional parameters
        for key, value in optional.items():
            if 'on_' in key:
                # params starting with _on are converted to a function
                for event_lib in self._events:
                    if getattr(event_lib, value, None):
                        # found event and exit
                        optional[key] = getattr(event_lib, value)
                        break
            print (key)
            if key == 'style':
                # look for a style in style libs
                for style_lib in self._styles:
                    if getattr(style_lib, value, None):
                        optional['style'] = getattr(style_lib, value)
                        break

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
