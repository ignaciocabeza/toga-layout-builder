import toga
import yaml


class Layout:

    def __init__(self, layout = None):
        self._styles = []
        self._events = []

    def load(self, layout_path):
        layout_file = open(layout_path, 'r')
        with layout_file as f:
            self.layout = yaml.load(f.read())
            self.widgets = self._create_layout(self.layout)
            return self.widgets

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

    def _create_layout(self, layout, parent=None):
        """ recursive and dinamically creates a toga layout

        params:
        - layout: tree dict
        - parent: parent widget
        """

        # structure checks
        if len(layout.keys()) != 1:
            # node of the tree
            raise Exception(f'Bad Format near: {layout}')

        # get id of widget
        name = list(layout.keys())[0]

        # get current yaml node to parse
        current = layout[name]

        # get toga class
        widget_class = getattr(toga, current.pop('type', None))

        # extract special parameters for toga.WIDGET.add() function
        # TODO: improve this
        add_params = []
        if isinstance(parent, toga.OptionContainer):
            add_params.append(current.pop('label', None))

        # get children
        children = current.pop('widgets', None)

        # parse positional parameters
        positional = current.pop('args', None)

        # parse optional parameters
        optional = self._build_optional_parameters(current.items())

        # create toga widget
        # TODO: Improve this if
        if positional:
            widget = widget_class(*positional, id=name, **optional)
        else:
            widget = widget_class(id=name, **optional)

        add_params.append(widget)
    
        # create layout for children
        if children:
            for child in children:
                self._create_layout(child, widget)

        # add widget to parent
        if parent:
            if type(parent) == toga.ScrollContainer:
                #special case of scroll container, only needs one widget as child 
                parent.content = widget
            else:
                parent.add(*add_params)
 
        return widget

    def _build_optional_parameters(self, items):
        
        optional = {key: value for (key, value) in items if key not in ['args', 'type', 'widgets']}
        
        # sanitase optional parameters
        for key, value in optional.items():
            
            # params starting with _on are converted to a function
            if 'on_' in key:
                for event_lib in self._events:
                    if getattr(event_lib, value, None):
                        # found event and exit
                        optional[key] = getattr(event_lib, value)
                        break

            # look for a style in style libs
            if key == 'style':
                for style_lib in self._styles:
                    if getattr(style_lib, value, None):
                        optional['style'] = getattr(style_lib, value)
                        break
        
        return optional