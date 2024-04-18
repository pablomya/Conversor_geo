#Conversor de nomenclaturas de rumbo y manteo

#author(github):pablomya

import funciones as fn

def main():

    keep_going=True

    while keep_going:
        conv_type=input("""Hola!. Por favor selecciona una de las opciones:
        Cuadrante -> Azimutal                 (a)
        Cuadrante -> Dip/Dip direction        (b)
        Azimutal -> Cuadrante                 (c)
        Azimutal -> Dip/Dip direction         (d)
        Dip/ Dip direction -> Cuadrante       (e)
        Dip/Dip direction -> Azimutal         (f)
        """).lower()
    
        if conv_type=="a":
            rumbo=input("""Introduce el rumbo. Ejemplo: N00E
            """)
            manteo=input("""Introduce el manteo. Ejemplo: 00E
            """)
            converted=fn.cuad_to_azimut(rumbo, manteo)
            if converted!=False:
                print("El resultado de la conversión es: "+str(converted))
        elif conv_type=="b":
            rumbo=input("""Introduce el rumbo. Ejemplo: N00E
            """)
            manteo=input("""Introduce el manteo. Ejemplo: 00E
            """)
            converted=fn.cuad_to_dipdir(rumbo, manteo)
            if converted!=False:
                print("El resultado de la conversión es: "+str(converted))
        elif conv_type=="c":
            rumbo=input("""Introduce el rumbo. Ejemplo: 000
            """)
            manteo=input("""Introduce el manteo. Ejemplo: 00E
            """)
            converted=fn.azimut_to_cuad(rumbo, manteo)
            if converted!=False:
                print("El resultado de la conversión es: "+str(converted))
        elif conv_type=="d":
            rumbo=input("""Introduce el rumbo. Ejemplo: 000
            """)
            manteo=input("""Introduce el manteo. Ejemplo: 00E
            """)
            converted=fn.azimut_to_dipdir(rumbo, manteo)
            if converted!=False:
                print("El resultado de la conversión es: "+str(converted))
        elif conv_type=="e":
            dip=input("""Introduce el dip. Ejemplo: 00
            """)
            dipdir=input("""Introduce el dip direction. Ejemplo: 000
            """)
            converted=fn.dipdir_to_cuad(dip, dipdir)
            if converted!=False:
                print("El resultado de la conversión es: "+str(converted))
        elif conv_type=="f":
            dip=input("""Introduce el dip. Ejemplo: 00
            """)
            dipdir=input("""Introduce el dip direction. Ejemplo: 000
            """)
            converted=fn.dipdir_to_azimut(dip, dipdir)
            if converted!=False:
                print("El resultado de la conversión es: "+str(converted))
        else:
            print("Respuesta no válida.")

        answ=input("""¿Deseas realizar otra conversión? (si/no)
        """)
        if answ!="si":
            print("Hasta luego!")
            keep_going=False

if __name__=="__main__":
    main()

