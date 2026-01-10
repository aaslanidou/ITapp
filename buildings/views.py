from django.shortcuts import render, redirect, get_object_or_404
from .models import Building, Room, Computer
from .forms import BuildingForm, RoomForm, ComputerForm
from django.http import JsonResponse


# Dashboard
def dashboard(request):
    buildings = Building.objects.prefetch_related('rooms__computers')
    return render(request, 'buildings/dashboard.html', {'buildings': buildings})

# Building CRUD
def add_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BuildingForm()
    return render(request, 'buildings/building_form.html', {'form': form})

def edit_building(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BuildingForm(instance=building)
    return render(request, 'buildings/building_form.html', {'form': form})

def delete_building(request, pk):
    building = get_object_or_404(Building, pk=pk)
    building.delete()
    return redirect('dashboard')

# Room CRUD
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RoomForm()
    return render(request, 'buildings/add_room.html', {'form': form})

def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RoomForm(instance=room)
    return render(request, 'buildings/room_form.html', {'form': form})

def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.delete()
    return redirect('dashboard')

# Computer CRUD
def add_computer(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ComputerForm()
    return render(request, 'buildings/computer_form.html', {'form': form})

def edit_computer(request, pk):
    computer = Computer.objects.get(id=pk)
    if request.method == "POST":
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()  # τώρα σώζει και pos_x / pos_y
            return redirect('dashboard')
    else:
        form = ComputerForm(instance=computer)
    return render(request, 'buildings/edit_computer.html', {'form': form})


def delete_computer(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    computer.delete()
    return redirect('dashboard')


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