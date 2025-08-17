Requerimientos de la Clase Persona
Debe tener una clase llamada **Persona**.

Debe tener dos atributos:

- nombre

- apellido

Requerimientos de la Clase **Cliente**
Debe tener una clase llamada Cliente.

- Debe heredar de la clase **Persona**.

- Debe tener dos atributos propios, además de los heredados:

- numero_de_cuenta

- balance

**Debe tener tres métodos:**

- Un método especial (__str__ o similar) que permita imprimir todos los datos del cliente, incluyendo el balance de su cuenta.

- Un método llamado Depositar que permita agregar dinero al balance de la cuenta.

- Un método llamado Retirar que permita sacar dinero del balance de la cuenta. Este método debe validar que no se pueda retirar más dinero del que se posee en la cuenta.

Requerimientos del Flujo del Programa
- El programa debe solicitar al usuario que elija una operación: depósito, retiro o salir.

- El usuario debe poder realizar tantas operaciones como desee hasta que decida salir.

- El programa debe mantener un registro del balance del cliente.

Se recomienda organizar el código en dos funciones principales:

- Una función que cree un objeto Cliente solicitando al usuario toda la información necesaria y lo devuelva.

- Una función principal (ej. inicio) que organice la ejecución del programa:

- Llame a la función para crear el cliente.

- Contenga un bucle (loop) que le pregunte al usuario si quiere depositar, retirar o salir.

- Muestre el balance actual después de cada modificación (depósito o retiro).

Se puede asumir que el usuario ingresará siempre información apropiada, sin necesidad de implementar validaciones de datos exhaustivas (números, mayúsculas/minúsculas, etc.), a menos que se desee.