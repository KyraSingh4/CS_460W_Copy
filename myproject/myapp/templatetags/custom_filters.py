from django import template

register = template.Library()

@register.filter
def format_time(hour, minute):
    """Formats hour and minute as HH:MM."""
    return f"{hour:02}:{minute}"