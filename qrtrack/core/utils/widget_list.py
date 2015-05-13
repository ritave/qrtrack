from django.template.response import TemplateResponse

class WidgetList:
    def add_widget(self, widget_view, order=50):
        self._widgets.append((
            order,
            widget_view
        ))
        # First by order, then whatever
        self._widgets.sort()

    def clear_widgets(self):
        self._widgets = []

    def __init__(self):
        self._widgets = []

    def __call__(self, *args, **kwargs):
        result = []
        for widget in self._widgets:
            response = widget[1](*args, **kwargs)
            if isinstance(response, TemplateResponse):
                response.render()
                response = response.rendered_content
            elif not isinstance(response, str):
                raise ValueError("Unknown object received from view")
            result.append(response)
        return result


# A decorator for views that will be a widget shown somewhere
def widget(widget_list, order=50):
    def decorator_func(func):
        widget_list.add_widget(func, order)
        return func
    return decorator_func