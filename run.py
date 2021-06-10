import asyncio

async def funcion_c():
    print('1')
    await asyncio.sleep(1)
    print('2')
    return {'respuesta':'funcion_c'}

async def funcion_b():
    tarea = asyncio.create_task(funcion_c())
    valor = await tarea
    print(valor)

def funcion_a():
    print('Estamos en la funcion_a')
    asyncio.run(funcion_b())
    print('Fin de la funcion_a')

funcion_a()