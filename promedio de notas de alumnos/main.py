def imprimir_materias_suspendidas(calificaciones):
    calificacion_aprobatoria = 7
    asignaturas_suspendidas = {}
    for alumno in calificaciones:
        for asignatura_con_calificacion in calificaciones[alumno]:
            asignatura = asignatura_con_calificacion["asignatura"]
            calificacion = asignatura_con_calificacion["calificacion"]
            if asignatura not in asignaturas_suspendidas:
                asignaturas_suspendidas[asignatura] = 0
            if calificacion < calificacion_aprobatoria:
                asignaturas_suspendidas[asignatura] += 1

    for asignatura_suspendida in asignaturas_suspendidas:
        conteo = asignaturas_suspendidas[asignatura_suspendida]
        print(f"{asignatura_suspendida} suspendida por {conteo} alumno(s)")


def obtener_alumnos_con_media(calificaciones):
    sumatorias = {}
    for alumno in calificaciones:
        for asignatura_con_calificacion in calificaciones[alumno]:
            calificacion = asignatura_con_calificacion["calificacion"]
            if alumno not in sumatorias:
                sumatorias[alumno] = {"sumatoria": 0, "conteo": 0}
            sumatorias[alumno]["sumatoria"] += calificacion
            sumatorias[alumno]["conteo"] += 1

    return sumatorias


def imprimir_media(calificaciones):
    sumatorias = obtener_alumnos_con_media(calificaciones)
    for alumno in sumatorias:
        sumatoria = sumatorias[alumno]["sumatoria"]
        conteo = sumatorias[alumno]["conteo"]
        media = sumatoria/conteo
        print(f"{alumno} media de {media}")


def imprimir_media_nota_superior_5(calificaciones):
    sumatorias = obtener_alumnos_con_media(calificaciones)
    media_minima = 5
    for alumno in sumatorias:
        sumatoria = sumatorias[alumno]["sumatoria"]
        conteo = sumatorias[alumno]["conteo"]
        media = sumatoria/conteo
        if media > media_minima:
            print(f"{alumno} tuvo una media superior a {media_minima} ({media})")


def main():
    calificaciones = {
        "Alumno 1": [{"asignatura": "Latin", "calificacion": 8}, {"asignatura": "Castellano", "calificacion": 8}, {"asignatura": "Francés", "calificacion": 9}, {"asignatura": "Inglés", "calificacion": 4}],
        "Alumno 2": [{"asignatura": "Latin", "calificacion": 7}, {"asignatura": "Castellano", "calificacion": 6}, {"asignatura": "Francés", "calificacion": 7}, {"asignatura": "Inglés", "calificacion": 2}],
        "Alumno 3": [{"asignatura": "Latin", "calificacion": 10}, {"asignatura": "Castellano", "calificacion": 7}, {"asignatura": "Francés", "calificacion": 8}, {"asignatura": "Inglés", "calificacion": 9}],
        "Alumno 4": [{"asignatura": "Latin", "calificacion": 4}, {"asignatura": "Castellano", "calificacion": 4}, {"asignatura": "Francés", "calificacion": 3}, {"asignatura": "Inglés", "calificacion": 2}],
        "Alumno 5": [{"asignatura": "Latin", "calificacion": 9}, {"asignatura": "Castellano", "calificacion": 8}, {"asignatura": "Francés", "calificacion": 9}, {"asignatura": "Inglés", "calificacion": 6}],
    }
    imprimir_materias_suspendidas(calificaciones)
    imprimir_media(calificaciones)
    imprimir_media_nota_superior_5(calificaciones)


main()