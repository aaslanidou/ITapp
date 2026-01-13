from django.shortcuts import render, redirect, get_object_or_404
from .models import Building, Room, Computer
from .forms import BuildingForm, RoomForm, ComputerForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required , permission_required





# Dashboard
@login_required 
def dashboard(request):
    buildings = Building.objects.prefetch_related('rooms__computers')
    return render(request, 'buildings/dashboard.html', {'buildings': buildings})

# Building CRUD
@login_required
@permission_required('buildings.add_building', raise_exception=True)
def add_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BuildingForm()
        return render(request, 'buildings/form_templates.html', {
        'form': form,
        'form_title': 'Add Building',
        'button_text': 'Add Building',
        'button_color': '#28a745'
    })

@login_required
@permission_required('buildings.change_building', raise_exception=True)
def edit_building(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BuildingForm(instance=building)
    return render(request, 'buildings/form_templates.html', {
        'form': form,
        'form_title': 'Edit Building',
        'button_text': 'Update Building',
        'button_color': '#007BFF'
    })

@permission_required('buildings.delete_building', raise_exception=True)
def delete_building(request, pk):
    building = get_object_or_404(Building, pk=pk)
    building.delete()
    return redirect('dashboard')

# Room CRUD
@login_required
@permission_required('buildings.add_room', raise_exception=True)
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RoomForm()
    return render(request, 'buildings/form_templates.html', {
        'form': form,
        'form_title': 'Add Room',
        'button_text': 'Add Room',
        'button_color': '#28a745'
    })
@login_required
@permission_required('buildings.change_room', raise_exception=True)
def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RoomForm(instance=room)
    return render(request, 'buildings/form_templates.html', {
        'form': form,
        'form_title': 'Edit Room',
        'button_text': 'Update Room',
        'button_color': '#007BFF'
    })

@permission_required('buildings.delete_room', raise_exception=True)
def delete_room(request, pk):
     room = get_object_or_404(Room, pk=pk)
     room.delete()
     return redirect('dashboard')

# Computer CRUD
@login_required
@permission_required('buildings.add_computer', raise_exception=True)
def add_computer(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ComputerForm()
    return render(request, 'buildings/form_templates.html', {
        'form': form,
        'form_title': 'Add Computer',
        'button_text': 'Add Computer',
        'button_color': '#28a745'
    })

@login_required
@permission_required('buildings.change_computer', raise_exception=True)
def edit_computer(request, pk):
    computer = Computer.objects.get(id=pk)
    if request.method == "POST":
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()  # τώρα σώζει και pos_x / pos_y
            return redirect('dashboard')
    else:
        form = ComputerForm(instance=computer)
    return render(request, 'buildings/form_templates.html', {
        'form': form,
        'form_title': 'Edit Computer',
        'button_text': 'Update Computer',
        'button_color': '#007BFF'
    })

@permission_required('buildings.delete_computer', raise_exception=True)
def delete_computer(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    computer.delete()
    return redirect('dashboard')

@login_required
@permission_required('buildings.delete_computer', raise_exception=True)
def update_computer_position(request):
    if request.method == "POST":
        computer_id = request.POST.get("id")
        pos_x = request.POST.get("pos_x")
        pos_y = request.POST.get("pos_y")
        
        try:
            computer = Computer.objects.get(id=computer_id)
            computer.pos_x = int(pos_x)
            computer.pos_y = int(pos_y)
            computer.save()
            return JsonResponse({"status": "success"})
        except Computer.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Computer not found"})
    return JsonResponse({"status": "error", "message": "Invalid request"})