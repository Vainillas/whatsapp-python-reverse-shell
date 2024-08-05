# Whatsapp Desktop Python Code Execution
## _Prueba de concepto para explotar la ejecución de código de python mediante Whatsapp Desktop_
### Descripción
Este repositorio aprovecha la ejecución accesible de código python en archivos con formato .pyzw en Whatsapp Desktop para dispositivos Windows.
### Uso
#### 1 - Modificar el archivo pythoncompressed.pyzw con el código que se desea ejecutar.
En este caso, hay una reverse shell que se conecta a un servidor en la dirección especificada 
#### 2 - Escuchar en el puerto especificado en el archivo pythoncompressed.pyzw
```sh
ncat -lvnp 9001
```
#### 3 - Enviar el archivo pythoncompressed.pyzw a la víctima
