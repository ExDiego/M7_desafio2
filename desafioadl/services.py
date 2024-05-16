from .models import Tarea, SubTarea

# def recupera_tareas_y_sub_tareas():
#     return Tarea.objects.all(), SubTarea.objects.all()

def crear_tarea(descripcion):
    tarea = Tarea(descripcion=descripcion)
    tarea.save()
    imprimir_en_pantalla()

def crear_subtarea(descripcion,tarea):
    tarea = Tarea.objects.get(pk=tarea)
    subtarea = SubTarea(tarea_id=tarea,descripcion=descripcion)
    subtarea.save()
    imprimir_en_pantalla()
    
def elimina_tarea(tarea_id):
    tarea = Tarea.objects.filter(id=tarea_id).update(eliminada=True)
    SubTarea.objects.filter(tarea_id=tarea_id).update(eliminada=True)
    imprimir_en_pantalla()

def elimina_subtarea(subtarea_id):
    subtarea = SubTarea.objects.filter(id=subtarea_id).update(eliminada=True)
    imprimir_en_pantalla()

def imprimir_en_pantalla():
    tareas = Tarea.objects.filter(eliminada=False).all()
    subtareas = SubTarea.objects.filter(eliminada=False).all()
    
    for tarea in tareas:
        print(f"Tareas [{tarea.id}]: {tarea.descripcion}")
        for subtarea in subtareas.filter(tarea_id=tarea.id):
                print(f" .... Subtarea:[{subtarea.id}]:{subtarea.descripcion}")