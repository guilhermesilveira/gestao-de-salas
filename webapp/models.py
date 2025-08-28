from django.db import models

class Sala(models.Model):
    """
    Represents a room with its name and available hours.
    """
    name = models.CharField(max_length=255)
    available_hours = models.JSONField()

    def __str__(self):
        return self.name

# Example structure for the available_hours JSON field:
# {
#     "monday": [{"from": 9, "to": 17}],
#     "tuesday": [{"from": 9, "to": 12}, {"from": 13, "to": 17}],
#     "wednesday": [],
#     "thursday": [{"from": 10, "to": 18}],
#     "friday": [{"from": 9, "to": 17}],
#     "saturday": [],
#     "sunday": []
# }
