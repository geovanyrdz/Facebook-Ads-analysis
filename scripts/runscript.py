import asyncio
import subprocess

# Establecer la política del bucle de eventos para evitar advertencias
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Ruta a tu archivo .ipynb
notebook_path = "C:\\Users\\gio_r\\Desktop\\python\\My notebooks\\acala2.ipynb"

# Ruta completa al ejecutable de Jupyter
jupyter_path = "C:\\Users\\gio_r\\anaconda3\\Scripts\\jupyter.exe"

# Ejecutar el notebook
subprocess.run([jupyter_path, "nbconvert", "--to", "notebook", "--execute", notebook_path])





