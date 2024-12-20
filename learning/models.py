from django.db import models

class Topic(models.Model):
   """A topic the user is learning about."""
   text = models.CharField(max_length=200)
   date_added = models.DateTimeField(auto_now_add=True)

   def __str__(self):
     """Return a string representation of the model."""
     return self.text
   
class Entry(models.Model):
  """Something specific learned about a topic."""
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # Relación con el modelo Topic
  text = models.TextField()  # Campo de texto largo para la entrada
  date_added = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    
  class Meta:
      verbose_name_plural = 'entries'  # Nombre plural correcto de la clase Entry
    
  def __str__(self):
     """Return a simple string representing the entry."""
     if len(self.text) > 50:
      return f"{self.text[:50]}..."  # Muestra solo los primeros 50 caracteres del texto
     return f"{self.text[:]}"