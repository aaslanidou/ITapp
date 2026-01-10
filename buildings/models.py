from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=50)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="rooms")
    width = models.PositiveIntegerField(default=1200)   # πλάτος σε pixels
    height = models.PositiveIntegerField(default=700)   # ύψος σε pixels 
    
    def __str__(self):
        return f"{self.name} ({self.building.name})"

class Computer(models.Model):
    ip_address = models.GenericIPAddressField()
    pc_name = models.CharField(max_length=50)
    bria_number = models.CharField(max_length=50, blank=True)
    STATUS_CHOICES = [
        ('OK', 'OK'),
        ('WARNING', 'WARNING'),
        ('REPLACE', 'REPLACE')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OK')
    notes = models.TextField(blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="computers")
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)

    is_team_leader = models.BooleanField(default=False)  # νέο πεδίο

    def __str__(self):
        return f"{self.pc_name} ({self.ip_address})"
