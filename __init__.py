# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import sys
from random import *
"""
    Obtengo el modulo que fueron invocados
"""

module = GetParams("module")

if module == "export":
    path = GetParams("path")

    with open(path, 'w') as f:
        f.write(str(vars_))

if module == "setVariable":
    data = GetParams("data")
    variables = GetParams("vars")

    try:
        data = eval(data)
        variables =  variables.split(",")

        for i, var in enumerate(variables):
            SetVar(var, data[i])
    except Exception as e:
        PrintException()
        raise e



if module == "backup":
    try:
        try:
            os.mkdir("Logs")
        except:
            pass
        name = "Logs/app_{}.log".format(datetime.now()).replace(":", ".")
        os.rename("app.log", name)
    except Exception as e:
        PrintException()
        raise e

if module == "cleanVars":

    vars = GetParams('vars')
    vars = vars.split(',')
    for var in vars:
        print(GetVar(var))
        SetVar(var, '')

if module == "random_":
    option = GetParams('option')
    value = GetParams('value')
    result = GetParams('var')

    try:
        value = eval(value)
        if option == "randint":
            rand_number = eval(option)(value[0], value[1])
        else:
            rand_number = eval(option)(value)

        if result:
            SetVar(result, rand_number)
    except Exception as e:
        PrintException()
        raise e



# if module == "import":
#     path = GetParams("path")

#     with open(path, 'r') as f:
#         var = f.read()
#         variables = eval(var)

#     for v in variables:
#         v.pop('$$hashKey')
    

#     vars_ = variables
#     print(vars_)