from .models import Estudiante, Direccion, Curso, Profesor

def crear_curso(codigo, nombre, version):
    curso = Curso(
        codigo=codigo,
        nombre=nombre,
        version=version,
    )
    curso.full_clean() #aplica las condiciones del modelo, para no tener problemas con la inconsistencia de datos
    curso.save()
    return curso

def crear_profesor(rut, nombre, apellido, activo, creacion_registro, creado_por):
    profesor = Profesor(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=activo,
        creacion_registro=creacion_registro,
        creado_por=creado_por,
    )
    profesor.full_clean() #aplica las condiciones del modelo, para no tener problemas con la inconsistencia de datos
    profesor.save()
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo, creacion_registro, creado_por):
   estudiante = Estudiante(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nac=fecha_nac,
        activo=activo,
        creacion_registro=creacion_registro,
        creado_por=creado_por,
    )
   estudiante.full_clean() #aplica las condiciones del modelo, para no tener problemas con la inconsistencia de datos
   estudiante.save()
   return estudiante


def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante):
    direccion=Direccion (
        calle=calle,
        numero=numero,
        dpto=dpto,
        comuna=comuna,
        ciudad=ciudad,
        region=region,
        estudiante=estudiante
    )
    direccion.save()
    return direccion

def obtiene_estudiante(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    return estudiante

def obtiene_profesor(rut):
    profesor = Profesor.objects.get(rut=rut)
    return profesor

def obtiene_curso(codigo):
    curso = Curso.objects.get(codigo=codigo)
    return curso

def agrega_profesor_a_curso(rut, codigo):
    profesor = Profesor.objects.get(rut=rut)
    curso = Curso.objects.get(codigo=codigo)
    profesor.cursos.add(curso)
    curso.save()
    print(f"Se agregó el curso {curso.nombre} al profesor {profesor.nombre} {profesor.apellido}")


def agrega_cursos_a_estudiante(rut, codigo):
    estudiante = Estudiante.objects.get(rut=rut)
    curso_id = Curso.objects.get(codigo=codigo)
    estudiante.cursos.add(curso_id)
    
    print(f"Se agregó el curso {curso_id.nombre} al estudiante {estudiante.nombre} {estudiante.apellido}")

#se espera toda la informacion
def imprime_estudiante_cursos():
    estudiantes_curso = Estudiante.objects.all()

    for e in estudiantes_curso:
        print(f""" Estudiante: {e.nombre}/{e.apellido}/{e.rut} / Activo: {e.activo}""")

        cursos = e.cursos.all() # recordar que se usa para todos los cursos del estudiante
        
        if cursos:
            for curso in cursos:
                print(f""" Curso[{curso.codigo}]: {curso.nombre} {curso.version} """)
        else:
            print("No tiene cursos asignados")