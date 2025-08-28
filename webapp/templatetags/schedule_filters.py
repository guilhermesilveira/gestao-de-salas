from django import template

register = template.Library()

@register.filter
def count_schedule_slots(available_hours):
    """
    Count the total number of schedule slots in available_hours
    """
    if not available_hours:
        return 0
    
    total = 0
    for day, times in available_hours.items():
        if times:
            total += len(times)
    
    return total
