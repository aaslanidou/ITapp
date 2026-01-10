from django import forms
from .models import Building, Room, Computer

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'address']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'building', 'width', 'height']

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['ip_address', 'pc_name', 'bria_number', 'status', 'notes','is_team_leader', 'room', 'pos_x', 'pos_y']
        widgets = {
            'pos_x': forms.HiddenInput(),
            'pos_y': forms.HiddenInput(),
        }
