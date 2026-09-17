'''
 Sistema Experto para el guiado de un robot
 Esta clase contendrá el código creado por los alumnos de RyRDC para el control 
 y guiado de un robot móvil sobre un plano cartesiano

 Creado por: Diego Viejo
 el 11/09/2026


'''

from objetivo import *
import time
class ExpertSystem:
    def __init__(self) -> None:
        self.objetivoActual = None
        self.nombreAlumno = "Jorge Sánchez Cerezo" #IMPORTANTE: Cambia el valor de esta propiedad por tu nombre completo
        self.inicio = True

    #   función setObjetivo
    #   Almacena en la propiedad objetivoActual el objetivo al que tiene que moverse el robot
    def setObjetivo(self, objetivo):
        self.objetivoActual = objetivo


    #   función tomarDecision. 
    #   Recibe una tupla de 3 valores con la pose del robot: posición X, posición Y, orientación
    #   Devuelve una tupla con la velocidad lineal y angular que se
    #   quiere dar al robot

    def orientarse(self, difx, dify):
        #Con trigonometria básica, calculamos el angulo (tan = dify/dix): angulo = arctan dify difx
        angulo = math.atan2(dify, difx) #Como esta en radianes, vamos a pasarlo a grados
        angulo_grados = angulo * 180/math.pi
        return angulo_grados

    def segmentoinicio(self, xrobot, yrobot, orientacion, poseRobot):
        inicio_obj = self.objetivoActual.getInicio()
        xiniobj = inicio_obj[0]
        yiniobj = inicio_obj[1]

        difx = xiniobj - xrobot
        dify = yiniobj - yrobot 
        print(difx+dify)
        #girar robot hasta alinearse con el punto
        angulo = self.orientarse(difx, dify)
        #print(angulo)
        #print(orientacion)
        x = 2
        y = 0.5
        if poseRobot[2] >= (angulo-5):
            x = 2
            y = -0.1
        estado_inicio = True

        if abs(difx)+abs(dify)<= 0.25:
            estado_inicio = False

        return x, y, estado_inicio

    '''
    def segmentofinal(self, xrobot, yrobot, orientacion, poseRobot):
        x, y = 0, 0
        fin_obj = self.objetivoActual.getFin()
        xfinobj = fin_obj[0]
        yfinobj = fin_obj[1]

        difx = xfinobj - xrobot
        dify = yfinobj - yrobot 
        print(difx+dify)
        angulo = self.orientarse(difx, dify)
        print(angulo)
        print(orientacion)


        if abs(difx)+abs(dify) >= 65 and poseRobot[2] <= angulo + 5:
            x = 1
            y = -1
        else:
            if poseRobot[2] >= (angulo):
                x = 3
                y = -0.2
            estado_inicio = False

            if abs(difx)+abs(dify)<= 0.5:
                estado_inicio = True
        return x, y, estado_inicio
        '''

    def tomarDecision(self, poseRobot):
        xrobot = poseRobot[0]
        yrobot = poseRobot[1]
        orientacion = poseRobot[2]
        if self.inicio:
            x, y, self.inicio = self.segmentoinicio(xrobot, yrobot, orientacion, poseRobot)
        else:
            x, y, self.inicio = self.segmentofinal(xrobot, yrobot, orientacion, poseRobot)
        return (x , y)
    