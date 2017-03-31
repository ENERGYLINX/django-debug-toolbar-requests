from django.template import Template, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from debug_toolbar.panels import Panel

from requests_toolbar import operation_tracker


class RequestsDebugPanel(Panel):
    name = 'Requests'
    has_content = True
    template = 'requests_toolbar/panels/requests.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        operation_tracker.install_trackers()

    def process_request(self, request):
        operation_tracker.reset()

    def nav_title(self):
        return 'Requests'

    def nav_subtitle(self):
        results = operation_tracker.results
        number_of_calls = len(results)
        time_spent = sum([result['time'] for result in results])
        return '{} calls in {:.2f} ms'.format(number_of_calls, time_spent)

    def title(self):
        return 'Requests operations'

    def url(self):
        return ''

    def process_response(self, request, response):
        self.record_stats({
            'requests': operation_tracker.results
        })



