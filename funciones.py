
#Funciones necesarias para el conversor de nomenclaturas de rumbo y manteo

#author(github):pablomya

def cuad_to_azimut(rumbo_cuad, manteo_cuad):

    try:
        ew=rumbo_cuad[-1]
        angle=int(rumbo_cuad[1:-1])
        manteo_dir=manteo_cuad[2:]
        manteo_azim=manteo_cuad.upper()

        if ew.upper() in ['E'] and manteo_dir.upper() in ['SE']:
            rumbo_azim=angle
        elif ew.upper() in ['E'] and manteo_dir.upper() in ['NW']:
            rumbo_azim=angle+180
        elif ew.upper() in ['W'] and manteo_dir.upper() in ['NE']:
            rumbo_azim=360-angle
        elif ew.upper() in ['W'] and manteo_dir.upper() in ['SW']:
            rumbo_azim=angle-90
        elif ew.upper() in ['E'] and manteo_dir.upper()  in ['N']:
            rumbo_azim=270
        elif ew.upper() in ['E'] and manteo_dir.upper()  in ['S']:
            rumbo_azim=90       
        elif ew.upper() in ['E'] and manteo_dir.upper()  in ['E']:
            rumbo_azim=0
        elif ew.upper() in ['E'] and manteo_dir.upper()  in ['W']:
            rumbo_azim=180
        elif ew.upper() in ['W'] and manteo_dir.upper()  in ['N']:
            rumbo_azim=270
        elif ew.upper() in ['W'] and manteo_dir.upper()  in ['S']:
            rumbo_azim=90        
        elif ew.upper() in ['W'] and manteo_dir.upper()  in ['E']:
            rumbo_azim=0
        elif ew.upper() in ['W'] and manteo_dir.upper()  in ['W']:
            rumbo_azim=180
        else:
            rumbo_azim="N/A"
            print("Error, valor fuera de rango")

        rumbo_azim=str(rumbo_azim)
        manteo_azim=str(manteo_azim)
        conv=rumbo_azim.rstrip()+"/"+manteo_azim.rstrip()

        return conv  
    except Exception:
        print("Hubo un error inesperado, revisa si el formato de entrada es el correcto :)")
        return False

def azimut_to_cuad(rumbo_azim, manteo_azim):
    try:
        angle=int(rumbo_azim)
        manteo_cuad=manteo_azim.upper()

        if 270<=angle<=360:
            rumbo_cuad="N"+str(360-angle)+"W"
        elif 180<=angle<270:
            rumbo_cuad="N"+str(angle-180)+"E"
        elif 90<=angle<180:
            rumbo_cuad="N"+str(90-(angle-90))+"W"
        elif 0<=angle<90:
            rumbo_cuad="N"+str(angle)+"E"
        else:
            rumbo_cuad="N/A"
            print("Error, valor fuera de rango")

        rumbo_cuad=str(rumbo_cuad)
        manteo_cuad=str(manteo_cuad)
        conv=rumbo_cuad.rstrip()+"/"+manteo_cuad.rstrip()
        
        return conv  
    except Exception:
        print("Hubo un error inesperado, revisa si el formato de entrada es el correcto :)")
        return False

def azimut_to_dipdir(rumbo_azim, manteo_azim):
    try:
        dip=manteo_azim[:2]
        dir_manteo=manteo_azim[2:]
        angle=int(rumbo_azim)

        if dir_manteo.upper() in ['NW', 'NNW', 'NWW']:
            cuad=1
        elif dir_manteo.upper() in ['NE', 'NNE', 'NEE']:
            cuad=2
        elif dir_manteo.upper() in ['SW', 'SSW', 'SWW']:
            cuad=3
        elif dir_manteo.upper() in ['SE', 'SSE', 'SEE']:
            cuad=4

        if 0<angle<90 and cuad==1:
            dipdir=360+(angle-90)
        elif 0<angle<90 and cuad==4:
            dipdir=angle+90
        elif 90<angle<180 and cuad==2:
            dipdir=angle-90
        elif 90<angle<180 and cuad==3:
            dipdir=angle+90
        elif 180<angle<270 and cuad==1:
            dipdir=angle+90
        elif 180<angle<270 and cuad==4:
            dipdir=angle-90
        elif 270<angle<360 and cuad==2:
            dipdir=(angle+90)-360
        elif 270<angle<360 and cuad==3:
            dipdir=angle-90
        elif (angle==90 or angle==270) and dir_manteo.upper() in ['N']:
            dipdir=0
        elif (angle==90 or angle==270) and dir_manteo.upper() in ['S']:
            dipdir=180
        elif (angle==0 or angle==180) and dir_manteo.upper() in ['E']:
            dipdir=90
        elif (angle==0 or angle==180) and dir_manteo.upper() in ['W']:
            dipdir=270
        else:
            dipdir="N/A"
            print("Error, valor fuera de rango o incorrecto")

        dip=str(dip)
        dipdir=str(dipdir)
        conv=dip.rstrip()+"/"+dipdir.rstrip()
        
        return conv
    except Exception:
        print("Hubo un error inesperado, revisa si el formato de entrada es el correcto :)")
        return False

def dipdir_to_azimut (dip, dipdir):
    try:
        dipdir=int(dipdir)

        if 90<=dipdir<=360:
            rumbo_azim=dipdir-90
        elif 0<=dipdir<90:
            rumbo_azim=360+(dipdir-90)
        else:
            rumbo_azim="N/A"
            print("Error, valor fuera de rango")
        
        if dipdir==0 or dipdir==360:
            manteo_out="N"
        elif dipdir==90:
            manteo_out="E"
        elif dipdir==180:
            manteo_out="S"
        elif dipdir==270:
            manteo_out="W"
        elif 0<dipdir<90:
            manteo_out="NE"
        elif 90<dipdir<180:
            manteo_out="SE"
        elif 180<dipdir<270:
            manteo_out="SW"
        elif 270<dipdir<360:
            manteo_out="NW"
        else:
            manteo_out="N/A"
            print("Error, valor fuera de rango")
        
        rumbo_azim=str(rumbo_azim)
        manteo_azim=str(dip+manteo_out.upper())
        conv=rumbo_azim.rstrip()+"/"+manteo_azim.rstrip()

        return conv
    except Exception:
        print("Hubo un error inesperado, revisa si el formato de entrada es el correcto :)")
        return False
    
def cuad_to_dipdir (rumbo_cuad, manteo_cuad):
    try:
        ew=rumbo_cuad[-1]
        angle=int(rumbo_cuad[1:-1])
        dir_manteo=manteo_cuad[2:]
        dip=manteo_cuad[:2]

        if dir_manteo.upper() in ['NW', 'NNW', 'NWW']:
            cuad=1
        elif dir_manteo.upper() in ['NE', 'NNE', 'NEE']:
            cuad=2
        elif dir_manteo.upper() in ['SW', 'SSW', 'SWW']:
            cuad=3
        elif dir_manteo.upper() in ['SE', 'SSE', 'SEE']:
            cuad=4
        else:
            cuad=0

        if angle==0:
            if dir_manteo.upper() in ["E"]:
                dipdir=90
            elif dir_manteo.upper() in ["W"]:
                dipdir=270
            else:
                dipdir="N/A"
                print("Error, valor fuera de rango")

        elif ew.upper() in ["E"]:
            if cuad==1:
                dipdir=360+(angle-90)
            elif cuad==4:
                dipdir=angle+90
            elif dir_manteo.upper() in ["N"]:
                dipdir=0
            elif dir_manteo.upper() in ["S"]:
                dipdir=180
        elif ew.upper() in ["W"]:
            if cuad==2:
                dipdir=(angle-90)*(-1)
            elif cuad==3:
                dipdir=360-(angle+90)
            elif dir_manteo.upper() in ["S"]:
                dipdir=180
            elif dir_manteo.upper() in ["N"]:
                dipdir=0
        else:
            dipdir="N/A"
            print("Error, valor fuera de rango")
        
        dip=str(dip)
        dipdir=str(dipdir)
        conv=dip.rstrip()+"/"+dipdir.rstrip()

        return conv
    except Exception:
        print("Hubo un error inesperado, revisa si el formato de entrada es el correcto :)")
        return False

def dipdir_to_cuad (dip, dipdir):
    try:
        dipdir=int(dipdir)

        if 90<=dipdir<=180 or 270<dipdir<=360:
            ew="E"
        elif 0<=dipdir<=90 or 180<dipdir<=270:
            ew="W"
        else:
            ew="N/A"
            print("Error, valor fuera de rango")

        if dipdir==0 or dipdir==360:
            manteo_cuad=dip+"N"
        elif dipdir==90:
            manteo_cuad=dip+"E"
        elif dipdir==180:
            manteo_cuad=dip+"S"
        elif dipdir==270:
            manteo_cuad=dip+"W"
        elif 0<dipdir<90:
            manteo_cuad=dip+"NE"
        elif 90<dipdir<180:
            manteo_cuad=dip+"SE"
        elif 180<dipdir<270:
            manteo_cuad=dip+"SW"
        elif 270<dipdir<360:
            manteo_cuad=dip+"NW"
        else:
            manteo_cuad="N/A"
            print("Error, valor fuera de rango")
        
        prerumbo=dipdir-90
        if prerumbo<0:
            prerumbo=360+prerumbo

        if 90<=prerumbo<=180:
            rumbo_out=360-(prerumbo+180)
            rumbo_cuad="N"+str(rumbo_out)+str(ew)
        elif 270<prerumbo<=360:
            rumbo_out=360-prerumbo
            rumbo_cuad="N"+str(rumbo_out)+str(ew)
        elif 0<=prerumbo<=90:
            rumbo_out=prerumbo
            rumbo_cuad="N"+str(rumbo_out)+str(ew)
        elif 180<prerumbo<=270:
            rumbo_out=prerumbo-180
            rumbo_cuad="N"+str(rumbo_out)+str(ew)
        else:
            rumbo_cuad="N/A"
            print("Error, valor fuera de rango")

        rumbo_cuad=str(rumbo_cuad)
        manteo_cuad=str(manteo_cuad)
        conv=rumbo_cuad.rstrip()+"/"+manteo_cuad.rstrip()

        return conv
    except Exception:
        print("Hubo un error inesperado, revisa si el formato de entrada es el correcto :)")
        return False