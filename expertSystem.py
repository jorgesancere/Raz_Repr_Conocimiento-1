<<<<<<< HEAD
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
        self.orientarse = False

    #   función setObjetivo
    #   Almacena en la propiedad objetivoActual el objetivo al que tiene que moverse el robot
    def setObjetivo(self, objetivo):
        self.objetivoActual = objetivo


    #   función tomarDecision. 
    #   Recibe una tupla de 3 valores con la pose del robot: posición X, posición Y, orientación
    #   Devuelve una tupla con la velocidad lineal y angular que se
    #   quiere dar al robot
    
    def funcionangulo(self, difx, dify):
        #Con trigonometria básica, calculamos el angulo (tan = dify/dix): angulo = arctan dify difx
        angulo = math.atan2(dify, difx) #Como esta en radianes, vamos a pasarlo a grados
        angulo_objetivo = angulo * 180/math.pi
        return angulo_objetivo
        """
    def segmentoinicio(self, xrobot, yrobot, orientacion, poseRobot):
        inicio_obj = self.objetivoActual.getInicio()
        xiniobj = inicio_obj[0]
        yiniobj = inicio_obj[1]
        #Primero orientarse, cuando esta alineado con el objetivo avance
    
        difx = xiniobj - xrobot
        dify = yiniobj - yrobot 
        print(difx+dify)
        #girar robot hasta alinearse con el punto
        angulo = self.funcionangulo(difx, dify)
        estado_inicio = True

        x = 2
        y = 0
        #INICIO
        while self.orientarse and (orientacion >=angulo + 10 or orientacion <= angulo - 10):
            #ver a que lado debe girarse:
            #if derecha:
            x = 2
            y = -0.75
            #if izquierda:
            x = 2
            y = 0.75
            if (poseRobot[2] <= angulo +10) or (poseRobot[2] >= angulo -10):
                self.orientarse = False

        #Girar derecha
        if poseRobot[2] >= (angulo-5):
            x = 2
            y = -0.3
        #Girar izquierda
        if poseRobot[2] <= angulo+5:
            x = 2
            y = 0.3
        
        if abs(difx)+abs(dify)<= 0.25:
            estado_inicio = False
            self.orientarse = True

        return x, y, estado_inicio

    
    def segmentofinal(self, xrobot, yrobot, orientacion, poseRobot):
        x, y = 0, 0
        fin_obj = self.objetivoActual.getFin()
        xfinobj = fin_obj[0]
        yfinobj = fin_obj[1]

        difx = xfinobj - xrobot
        dify = yfinobj - yrobot 
        print(difx+dify)
        angulo = self.funcionangulo(difx, dify)
        print(angulo)
        print(orientacion)


        #INICIO:
        while self.orientarse and (orientacion >=angulo + 10 or poseRobot[2] <= angulo - 10):
            #ver a que lado debe girarse:
            #if derecha:
            x = 2
            y = -0.75
            #if izquierda:
            x = 2
            y = 0.75
            if (orientacion <= angulo +10) or (orientacion >= angulo -10):
                self.orientarse = False

        if orientacion>= (angulo-5):
            x = 2
            y = -0.15
        #Girar izquierda
        if orientacion <= angulo+5:
            x = 2
            y = 0.15

        if abs(difx)+abs(dify)<= 0.5:
            estado_inicio = True
        return x, y, estado_inicio
    
    """
    def tomarDecision(self, poseRobot):
        
        """
        x , y = 0 , 0
        """ 
        xrobot = poseRobot[0]
        yrobot = poseRobot[1]
        orientacion = poseRobot[2]
        print()
        inicio_obj = self.objetivoActual.getInicio()
        xiniobj = inicio_obj[0]
        yiniobj = inicio_obj[1]
    
        difx = xiniobj - xrobot
        dify = yiniobj - yrobot 
        angulo_objetivo = math.degrees(math.atan2(dify, difx)) #Como esta en radianes, vamos a pasarlo a grados
        print(angulo_objetivo)



        #Ahora lo que queremos es calcular la diferencia, es decir, el angulo objetivo le restamos nuestra orientacion, y asi obtenemos lo que debe girar nuestro robot
        diferencia  = angulo_objetivo - orientacion
        while diferencia > 180:
            diferencia -= 360 # si ha dado mas de media vuelta en sentido horario, es decir, mas alla de los 180 grados, lo ponemos en -180, y asi lo situamos como que esta en la parte izquierda del robot (zona negativa | zona positiva) 
        while diferencia < -180:
            diferncia += 360

        print(diferencia)

        """
        if self.inicio:
            x, y, self.inicio = self.segmentoinicio(xrobot, yrobot, orientacion, poseRobot)
        else:
            x, y, self.inicio = self.segmentofinal(xrobot, yrobot, orientacion, poseRobot)
        return (x , y)
    """
        return 0, -1








    #NOTAS

        #Me doy cuenta dce que el angulo del robot lo imprimo en grados (orientarse (que es poseRobot[2])), por lo tanto
        #para girar en sentido horario hay que usar el menos, por lo que el angulo bueno (el ue queremos en 360), hay que pillar el resto de dividir entre 360:
        # ejemplo -- 0 grados mira hacia arriba, 180 abajo, 360 arriba otra vez, por lo que lo reseteamos a 0, pero tenemos que calcular como que el 0 esta igual de cerca del 270 que del 90, por lo que if orientacion
=======
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
        self.orientarse = False

    #   función setObjetivo
    #   Almacena en la propiedad objetivoActual el objetivo al que tiene que moverse el robot
    def setObjetivo(self, objetivo):
        self.objetivoActual = objetivo


    #   función tomarDecision. 
    #   Recibe una tupla de 3 valores con la pose del robot: posición X, posición Y, orientación
    #   Devuelve una tupla con la velocidad lineal y angular que se
    #   quiere dar al robot

    def funcionangulo(self, difx, dify):
        #Con trigonometria básica, calculamos el angulo (tan = dify/dix): angulo = arctan dify difx
        angulo = math.atan2(dify, difx) #Como esta en radianes, vamos a pasarlo a grados
        angulo_grados = angulo * 180/math.pi
        return angulo_grados

    def segmentoinicio(self, xrobot, yrobot, orientacion, poseRobot):
        inicio_obj = self.objetivoActual.getInicio()
        xiniobj = inicio_obj[0]
        yiniobj = inicio_obj[1]
        #Primero orientarse, cuando esta alineado con el objetivo avance
        
        difx = xiniobj - xrobot
        dify = yiniobj - yrobot 
        print(difx+dify)
        #girar robot hasta alinearse con el punto
        angulo = self.funcionangulo(difx, dify)
        estado_inicio = True

        x = 2
        y = 0
        #INICIO
        while self.orientarse and (poseRobot[2] >=angulo + 10 or poseRobot[2] <= angulo - 10):
            #ver a que lado debe girarse:
            #if derecha:
            x = 2
            y = -0.75
            #if izquierda:
            x = 2
            y = 0.75
            if (poseRobot[2] <= angulo +10) or (poseRobot[2] >= angulo -10):
                self.orientarse = False

        #Girar derecha
        if poseRobot[2] >= (angulo-5):
            x = 2
            y = -0.3
        #Girar izquierda
        if poseRobot[2] <= angulo+5:
            x = 2
            y = 0.3
        
        if abs(difx)+abs(dify)<= 0.25:
            estado_inicio = False
            self.orientarse = True

        return x, y, estado_inicio

    
    def segmentofinal(self, xrobot, yrobot, orientacion, poseRobot):
        x, y = 0, 0
        fin_obj = self.objetivoActual.getFin()
        xfinobj = fin_obj[0]
        yfinobj = fin_obj[1]

        difx = xfinobj - xrobot
        dify = yfinobj - yrobot 
        print(difx+dify)
        angulo = self.funcionangulo(difx, dify)
        print(angulo)
        print(orientacion)


        #INICIO:
        while self.orientarse and (poseRobot[2] >=angulo + 10 or poseRobot[2] <= angulo - 10):
            #ver a que lado debe girarse:
            #if derecha:
            x = 2
            y = -0.75
            #if izquierda:
            x = 2
            y = 0.75
            if (poseRobot[2] <= angulo +10) or (poseRobot[2] >= angulo -10):
                self.orientarse = False

        if poseRobot[2] >= (angulo-5):
            x = 2
            y = -0.15
        #Girar izquierda
        if poseRobot[2] <= angulo+5:
            x = 2
            y = 0.15

        if abs(difx)+abs(dify)<= 0.5:
            estado_inicio = True
        return x, y, estado_inicio
    

    def tomarDecision(self, poseRobot):
        x , y = 0 , 0
        xrobot = poseRobot[0]
        yrobot = poseRobot[1]
        orientacion = poseRobot[2]

        if self.inicio:
            x, y, self.inicio = self.segmentoinicio(xrobot, yrobot, orientacion, poseRobot)
        else:
            x, y, self.inicio = self.segmentofinal(xrobot, yrobot, orientacion, poseRobot)
        return (x , y)
    
>>>>>>> 19d2e5b5f07734f07b2068d3f576a2682751c2d1
