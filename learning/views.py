from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The home page for Learning."""
    return render(request, 'learning/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning/topic.html', context)

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':  # Si no es un POST, muestra el formulario en blanco
        form = TopicForm()  # Formulario vacío
    else:  # Si es POST, procesa los datos enviados
        form = TopicForm(data=request.POST)
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda los datos en la base de datos
            return redirect('learning:topics')  # Redirige a la página de 'topics'

    # Si el formulario no es válido o si se accede con GET, se muestra la página con el formulario
    context = {'form': form}
    return render(request, 'learning/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id) 

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()  
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) 
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning:topic', topic_id=topic_id) 

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)  # Línea corregida: Se eliminó el "1" al inicio
    topic = entry.topic
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)  # Línea corregida: Se eliminó el "2" al inicio
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)  # Línea corregida: Se eliminó el "3" al inicio
        if form.is_valid():
            form.save()  # Línea corregida: Se eliminó el "4" al inicio
            return redirect('learning:topic', topic_id=topic.id)  # Línea corregida: Se eliminó el "5" al inicio
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning/edit_entry.html', context)
