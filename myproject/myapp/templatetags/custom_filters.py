from django import template

register = template.Library()

@register.filter
def format_time(hour, minute):
    """Formats hour and minute as HH:MM."""
    return f"{hour:02}:{minute}"

@register.simple_tag
def is_within_time_range(hour, minute, start_time, end_time):
    """
    Checks if the given hour and minute fall within the time range (inclusive).
    :param hour: Current hour (int).
    :param minute: Current minute (int).
    :param start_time: Start time in "HH:MM" format.
    :param end_time: End time in "HH:MM" format.
    :return: True if the time is within the range, False otherwise.
    """
    # Convert current time to minutes
    current_time = hour * 60 + minute

    # Parse start_time and end_time into hours and minutes
    start_hour, start_minute = map(int, start_time.split(":"))
    end_hour, end_minute = map(int, end_time.split(":"))

    # Convert start and end times to minutes
    start_total_minutes = start_hour * 60 + start_minute
    end_total_minutes = end_hour * 60 + end_minute

    # Check if current_time is within the range
    return start_total_minutes <= current_time <= end_total_minutes