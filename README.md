# todo-cli-Lucfontana
TODO CLI With Python

## Requisitos

- Python 3 instalado

## Ejecutar la app

Desde la carpeta del proyecto:

```bash
python todo_cli.py
```

Cuando aparezca el menu, usa opciones `1` a `6`.

## Test rapido manual

1. Ejecuta la app con `python todo_cli.py`.
2. Prueba este flujo:
	- `1` para agregar una tarea.
	- `2` para listar tareas.
	- `4` para exportar a CSV.
	- `5` para cargar desde CSV.
	- `3` para eliminar una tarea por indice.
	- `6` para salir.

## Test rapido por consola (no interactivo)

Este comando simula entradas del usuario:

```bash
printf '1\nComprar pan\n4\n\n3\n0\n5\n\n2\n6\n' | python todo_cli.py
```

## Validar sintaxis

```bash
python -m py_compile todo_cli.py
```
