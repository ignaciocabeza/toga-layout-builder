def get_widget_by_id(window, search_id):
        
        if not window.content:
            return None

        elements = []
        elements.append(window.content)

        while elements:
            current = elements.pop(0)
            
            # found control
            if current.id == search_id:
                return current

            # check if children are in content or children attr
            content = getattr(current, 'content', None)
            to_add = None
            if content:
                to_add = content
            else:
                children = getattr(current, 'children', None)
                if children:
                    to_add = children

            # add children to next elements to check
            if to_add:
                if type(to_add) == list:
                    for el in to_add:
                        elements.append(el)
                else:
                    elements.append(to_add)

        return None