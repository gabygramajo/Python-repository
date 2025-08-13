from pathlib import Path
import os
import platform

base_path = Path(__file__).parent / "Recetas"

def limpiar_consola():
    os.system("cls" if platform.system() == "Windows" else "clear")

def agregar_receta(categoria, nombre, contenido):
    receta_path = base_path / categoria / nombre
    if not receta_path.exists():
        receta_path.touch()
        receta_path.write_text(contenido)
        print("Receta creada con éxito.")
    else:
        print("No se pudo crear la receta. La Receta ya existente")

def crear_receta():
    print("Categorías disponibles:")
    categorias = obtener_categorias()

    for categoria in categorias:
        print(f'- {categoria}')

    categoria = input("¿En qué categoría deseas guardar la receta?: ").strip()

    if categoria not in categorias:
        print("No existe la categoria deseada.")
        return

    nombre = input("¿Cuál es el nombre de la receta? ").strip()
    contenido = input("Escribe el contenido de la receta:\n")
    agregar_receta(categoria, nombre, contenido)

def leer_receta(categoria, receta):
    receta_path = base_path / categoria / receta

    if receta_path.exists():
        print(receta_path.read_text(encoding='utf-8'))
    else:
        print("La receta no existe.")

def contar_recetas():
    contador_recetas = 0
    for file in base_path.rglob("*.txt"):
        contador_recetas += 1

    return contador_recetas

def obtener_recetas(categoria):
    categoria_path = base_path / categoria
    if categoria_path.exists():
        return [receta.name for receta in categoria_path.glob("*.txt")]

    return []

def obtener_categorias():
    return [categoria.name for categoria in base_path.iterdir() if categoria.is_dir()]

def seleccionar_categoria():
    print("Categorías disponibles: ")
    categorias = obtener_categorias()

    for categoria in categorias:
        print(f'- {categoria}')

    categoria = input("Selecciona una categoria: ").strip()
    recetas = obtener_recetas(categoria)
    if recetas:
        print("Recetas disponibles:")
        for receta in recetas:
            print(f'- {receta}')
        receta = input("¿Qué receta deseas leer? ").strip()
        leer_receta(categoria, receta)

    else:
        print("La categoría no existe")

def validar_crear_categoria(nombre):
    nueva_categoria = base_path / nombre
    nueva_categoria.mkdir(exist_ok=True)
    return nueva_categoria.exists()

def crear_categoria():
    nombre = input("¿Qué nombre tendrá la nueva categoría? ").strip()
    if validar_crear_categoria(nombre):
        print("✅ Categoría creada.")
    else:
        print("❌ No se pudo crear la categoría.")
    input("\nPresiona ENTER para continuar...")
    limpiar_consola()

def validar_eliminar_receta(categoria, receta):
    receta_path = base_path / categoria / receta
    if receta_path.exists():
        receta_path.unlink()
        return True
    return False

def eliminar_receta():
    print("Categorías disponibles:")
    categorias = obtener_categorias()
    for cat in categorias:
        print(f"- {cat}")
    categoria = input("¿Qué categoría eliges? ").strip()
    recetas = obtener_recetas(categoria)
    if recetas:
        print("\nRecetas disponibles:")
        for r in recetas:
            print(f"- {r}")
        receta = input("¿Qué receta deseas eliminar? ").strip()
        if validar_eliminar_receta(categoria, receta):
            print("✅ Receta eliminada.")
        else:
            print("❌ No se pudo eliminar la receta.")
    else:
        print("❌ Categoría vacía o no existente.")
    input("\nPresiona ENTER para continuar...")

def validar_eliminar_categoria(categoria):
    categoria_path = base_path / categoria
    if categoria_path.exists() and categoria_path.is_dir():
        for file in categoria_path.iterdir():
            if file.is_file():
                file.unlink()
        categoria_path.rmdir()
        return True
    return False

def eliminar_categoria():
    print("Categorías disponibles:")
    categorias = obtener_categorias()
    for cat in categorias:
        print(f"- {cat}")
    categoria = input("¿Qué categoría deseas eliminar? ").strip()
    if validar_eliminar_categoria(categoria):
        print("✅ Categoría eliminada.")
    else:
        print("❌ No se pudo eliminar la categoría. Asegúrate de que esté vacía.")
    input("\nPresiona ENTER para continuar...")

def mostrar_menu():
    print("¿Qué deseas hacer?")
    print("[1] Leer una receta")
    print("[2] Crear una receta")
    print("[3] Crear una categoría")
    print("[4] Eliminar una receta")
    print("[5] Eliminar una categoría")
    print("[6] Salir")

def ejecutar():
    print("¡Bienvenido al gestor de recetas!")
    print(f"Hay un total de {contar_recetas()} recetas.")

    while True:
        mostrar_menu()
        opcion = input("Ingresar una opcion: ")

        if opcion == "1":
            seleccionar_categoria()

        elif opcion == "2":
            crear_receta()

        elif opcion == "3":
            crear_categoria()

        elif opcion == "4":
            eliminar_categoria()

        elif opcion == "5":
            eliminar_categoria()

        elif opcion == "6":
            print("\nFinalizando gestor de recetas...")
            break
        else:
            print("Opción no válida, intente nuevamente...")

        limpiar_consola()

# INICIAR PROGRAMA
ejecutar()