
import math
class Pais:
    provincias = []#list para contener objetos de clase Provincia
    nombre = ""
    def __init__(self, p):
        self.provincias = p
        self.nombre = "Argentina"

    #Devuelve todos: varones + mujeres
    def get_total_poblacion(self):
        total = 0
        for p in self.provincias:
            total = total + p.get_total_poblacion()
        return total

    #Devuelte el objeto Provincia por el cod recibido
    def get_provincia(self, cod_provincia):
        p = None
        for x in self.provincias:
            if(x.get_cod() == cod_provincia):
                p = x
                print(x.get_cod())
                break
        return p

    #PARA HACER :) ************************************************************
    """
        Mostrar el total de pob.
        Mostrar el total de pob. femenina
        Mostrar el total de pob. masculina
    """
    def mostrar_totales_poblacion(self):
        poblacion_totales=0 # variables de pobacion total 
        provincia_pobacion = None
        
        for x in self.provincias: # recorre el id de las provincias y toma el total de las personas alfabetos y analfabatos 
            provincia_pobacion = x.alfabetismo.get_total()
            poblacion_totales += provincia_pobacion
        print("La poblacion total es: " + str(poblacion_totales))
        
       # -------------------CANTIDAD DE VARONES -------------
    def cantidad_de_varones(self):
        poblacion_varones_totales =0
        provincia_pobacion_varones_analfabetos = 0
        provincia_pobacion_varones_alfabetos = 0
        poblacion_varonesTotales = 0
    
        for x in self.provincias:
            provincia_pobacion_varones_analfabetos = x.alfabetismo.analfabetos.varones # busca la cantidad de varones analfa por provincia
            provincia_pobacion_varones_alfabetos = x.alfabetismo.alfabetos.varones # busca la cantida de varones alfabetos 
            poblacion_varonesTotales = provincia_pobacion_varones_analfabetos + provincia_pobacion_varones_alfabetos # suma a todos los varones de provincia 
            poblacion_varones_totales +=  poblacion_varonesTotales
            
        print("La poblacion de varones total es: " + str(poblacion_varones_totales))    
            
           
        
    #----------------------------------------CANTIDAD DE MUJERES --------------------
    
    def cantidad_de_mujeres(self):
        poblacion_mujeres_totales =0
        provincia_pobacion_mujeres_analfabetos = 0
        provincia_pobacion_mujeres_alfabetos = 0
        poblacion_mujeresTotales = 0
    
        for x in self.provincias:
            provincia_pobacion_mujeres_analfabetos = x.alfabetismo.analfabetos.mujeres # busca la cantidad de mujeres analfa por provincia
            provincia_pobacion_mujeres_alfabetos = x.alfabetismo.alfabetos.mujeres # busca la cantida de mujeres alfabetos 
            poblacion_mujeresTotales = provincia_pobacion_mujeres_analfabetos + provincia_pobacion_mujeres_alfabetos # suma a todos los mujeres de provincia 
            poblacion_mujeres_totales +=  poblacion_mujeresTotales
        print("La poblacion de mujeres total es: " + str(poblacion_mujeres_totales))
            
            
         
            
       
     
     
     
       
        
    
   
    """
        Mostrar el nombre de provincia y su ratio de habitantes por vivienda
        Orderna por ratio descendentemente
    """
    def mostrar_ratio_habitantes_por_vivienda_por_provincia(self):
        porcentajes = []
       
        for x in self.provincias:
        
            provincia_pobacion_mujeres_analfabetos = x.alfabetismo.analfabetos.mujeres # busca la cantidad de mujeres analfa por provincia
            provincia_pobacion_mujeres_alfabetos = x.alfabetismo.alfabetos.mujeres # busca la cantida de mujeres alfabetos 
            poblacion_mujeresTotales = provincia_pobacion_mujeres_analfabetos + provincia_pobacion_mujeres_alfabetos # suma a todos los mujeres de provincia 
            
            provincia_pobacion_varones_analfabetos = x.alfabetismo.analfabetos.varones # busca la cantidad de varones analfa por provincia
            provincia_pobacion_varones_alfabetos = x.alfabetismo.alfabetos.varones # busca la cantida de varones alfabetos 
            poblacion_varonesTotales = provincia_pobacion_varones_analfabetos + provincia_pobacion_varones_alfabetos # suma a todos los varones de provincia 
           
            cantidad_vivienda  = 0 # cantidad de viviendas que tiene la provincia 
            
            for y in x.viviendas:
                cantidad_vivienda += y.cantidad
                viviendas_por_provincia = cantidad_vivienda
                
            ratio = (poblacion_mujeresTotales+poblacion_varonesTotales)/viviendas_por_provincia
            porcentajes.append((x.nombre, ratio))
            
            
        porcentajes_ordenados = sorted(porcentajes, key=lambda x: x[1], reverse=True)
        for provincia, porcentaje in porcentajes_ordenados:
           print(f"La provincia de {provincia} tiene un ratio de habitantes por vivienda de {round(porcentaje, 2)}% ")
    
    #------------------------------------------------------------------------------------------------------------------
    
    """
        Mostrar por sexo el % de analfabetismo
    """
    def mostrar_porcentaje_analfabetismo_por_sexo(self):
       
        
        poblacion_mujeresTotales = 0
        provincia_pobacion_varones_analfabetos = 0
        provincia_pobacion_varones_alfabetos = 0
        poblacion_varonesTotales = 0
        porcentaje_analfabetos_varones = 0
        porcentaje_analfabetos_mujeres = 0
      
           
        
        for x in self.provincias:
            
            provincia_pobacion_mujeres_analfabetos = x.alfabetismo.analfabetos.mujeres # busca la cantidad de mujeres analfa por provincia
            provincia_pobacion_mujeres_alfabetos = x.alfabetismo.alfabetos.mujeres # busca la cantida de mujeres alfabetos 
            poblacion_mujeresTotales += (provincia_pobacion_mujeres_analfabetos + provincia_pobacion_mujeres_alfabetos) # suma a todos los mujeres de provincia 
            porcentaje_analfabetos_mujeres += provincia_pobacion_mujeres_analfabetos
            provincia_pobacion_varones_analfabetos = x.alfabetismo.analfabetos.varones # busca la cantidad de varones analfa por provincia
            provincia_pobacion_varones_alfabetos = x.alfabetismo.alfabetos.varones # busca la cantida de varones alfabetos 
            poblacion_varonesTotales += (provincia_pobacion_varones_analfabetos + provincia_pobacion_varones_alfabetos) # suma a todos los varones de provincia 
            porcentaje_analfabetos_varones += provincia_pobacion_varones_analfabetos
            
            
        por_sexo_mujeres = (porcentaje_analfabetos_mujeres*100)/poblacion_mujeresTotales
        por_sexo_varones= (porcentaje_analfabetos_varones*100) / poblacion_varonesTotales
       
        print(f"Porcentaje de mujeres analfabetos de todo el pais es de:"+" " + str(round(por_sexo_mujeres,2))+"%")
        print(f"Porcentaje de varones analfabetos de todo el  pais es de:" +" " + str(round(por_sexo_varones,2))+"%")
   

    """
        Mostrar el nombre de provincia y el % de analfabetos.
        Ordenar la lista descendentemente por el %
    """
    def mostrar_porcentaje_analfabetismo_por_provincia(self):
       
        
        porcentajes = []
    
        for x in self.provincias:
           
            provincia_pobacion_mujeres_analfabetos = x.alfabetismo.analfabetos.mujeres # busca la cantidad de mujeres analfa por provincia
            provincia_pobacion_mujeres_alfabetos = x.alfabetismo.alfabetos.mujeres # busca la cantida de mujeres alfabetos 
            poblacion_mujeresTotales = provincia_pobacion_mujeres_analfabetos + provincia_pobacion_mujeres_alfabetos # suma a todos los mujeres de provincia 
            
            provincia_pobacion_varones_analfabetos = x.alfabetismo.analfabetos.varones # busca la cantidad de varones analfa por provincia
            provincia_pobacion_varones_alfabetos = x.alfabetismo.alfabetos.varones # busca la cantida de varones alfabetos 
            poblacion_varonesTotales = provincia_pobacion_varones_analfabetos + provincia_pobacion_varones_alfabetos # suma a todos los varones de provincia 
            porcentaje_analfabetos_totales = ((provincia_pobacion_varones_analfabetos+ provincia_pobacion_mujeres_analfabetos )*100)/(poblacion_mujeresTotales+poblacion_varonesTotales )
            porcentajes.append((x.nombre, porcentaje_analfabetos_totales))
        porcentajes = sorted(porcentajes, key=lambda x: x[1], reverse=True)
    
        for provincia, porcentaje in porcentajes:
            print(provincia)
            print("Porcentaje de personas analfabetos de la provincia es de: " + str(round(porcentaje,2))+"%")
           

    """
        Mostrar el nombre de provincia y el % de viviendas sin retrete
        Ordenar la lista descendentemente por el %
    """
    def mostrar_porcentaje_vivendas_sin_retrete_por_provincia(self):
         porcentajes = []
    
         for x in self.provincias:
             cantidad_viviendas = 0
             cantidad_viviendas_sin_retrete = 0 
        
             cantidad_viviendas_sin_retrete += x.sanitario.sin_retrete
             cantidad_viviendas += x.sanitario.con_retrete
             porcentaje_sin_retrete = (cantidad_viviendas_sin_retrete * 100) / cantidad_viviendas
        
             porcentajes.append((x.nombre, porcentaje_sin_retrete))
    
    # Ordenar la lista de porcentajes en orden descendente según el porcentaje
         porcentajes_ordenados = sorted(porcentajes, key=lambda x: x[1], reverse=True)
    
         for provincia, porcentaje in porcentajes_ordenados:
           print(f"El {round(porcentaje, 2)}% de las viviendas de la provincia de {provincia} no tienen retrete")
    """
        Mostrar el nombre de provincia y el % de los que no viven en una casa o departamento.
        Ordenar la lista descendentemente por el % .
    """
    
    def mostrar_porcentaje_vivienda_precaria_por_provincia(self):
        porcentajes= []
        viviendas_totales = 0
        porcentaje_viviendas_precarias =0
        for x in self.provincias:
            por_provincica_precaria1=( x.viviendas[1].cantidad + x.viviendas[2].cantidad + x.viviendas[4].cantidad + x.viviendas[5].cantidad +x.viviendas[6].cantidad+ x.viviendas[7].cantidad)
            viviendas_totales =(por_provincica_precaria1+ x.viviendas[0].cantidad + x.viviendas[3].cantidad )
            porcentaje_viviendas_precarias = (por_provincica_precaria1 *100)/ viviendas_totales
    
            porcentajes.append((x.nombre, porcentaje_viviendas_precarias))
    
    # Ordenar la lista de porcentajes en orden descendente según el porcentaje
        porcentajes_ordenados = sorted(porcentajes, key=lambda x: x[1], reverse=True)
    
        for provincia, porcentaje in porcentajes_ordenados:
           print(f"El {round(porcentaje, 2)}% son casas precarias de la provincia de {provincia} ")
    """
        Se quiere saber si hay una correlacion entre las variables: analfabetismos vs
        viviendas precarias y sin retrete. Por ello hacer:
        1) Ordenar la lista de provincias segun el % de analfabetismos de forma
        ascendente. Esto nos da una pendiente positiva.
        2) Calcular la pendiente de la regresion lineal para las variables 
        "viviendas precarias" y para "sin retetre" y compare:
        ¿Como es el signo de la pendiente de estas dos variables comparado con
        el signo de la pendientes del % de alfabetismo?
        ¿Que se puede concluir?
        # biografia: https://github.com/Galindo-lab/calculator/blob/972c439ce52c74265173ddd193a5238c29cddffc/python/old/regrecion_lineal.py#L44
    """
    def mostrar_correlacion_alfabetismo_vs_vivienda_y_retrete(self,  debug=True):
        porcentajes = []
        for x in self.provincias:
            cantidad_viviendas = 0
            cantidad_viviendas_sin_retrete = 0 
            procentaje_total =0
           # calculo el porcentaje de personas analfabetas 
            provincia_pobacion_mujeres_analfabetos = x.alfabetismo.analfabetos.mujeres # busca la cantidad de mujeres analfa por provincia
            provincia_pobacion_mujeres_alfabetos = x.alfabetismo.alfabetos.mujeres # busca la cantida de mujeres alfabetos 
            poblacion_mujeresTotales = provincia_pobacion_mujeres_analfabetos + provincia_pobacion_mujeres_alfabetos # suma a todos los mujeres de provincia 
            # calculo el porcentaje de las viviendas 
            provincia_pobacion_varones_analfabetos = x.alfabetismo.analfabetos.varones # busca la cantidad de varones analfa por provincia
            provincia_pobacion_varones_alfabetos = x.alfabetismo.alfabetos.varones # busca la cantida de varones alfabetos 
            poblacion_varonesTotales = provincia_pobacion_varones_analfabetos + provincia_pobacion_varones_alfabetos # suma a todos los varones de provincia 
            porcentaje_analfabetos_totales = ((provincia_pobacion_varones_analfabetos+ provincia_pobacion_mujeres_analfabetos )*100)/(poblacion_mujeresTotales+poblacion_varonesTotales )
            # calculo el porcentaje de viviendas precarias por provincia 
            por_provincica_precaria1=( x.viviendas[1].cantidad + x.viviendas[2].cantidad + x.viviendas[4].cantidad + x.viviendas[5].cantidad +x.viviendas[6].cantidad+ x.viviendas[7].cantidad)
            viviendas_totales =(por_provincica_precaria1+ x.viviendas[0].cantidad + x.viviendas[3].cantidad )
            porcentaje_viviendas_precarias = (por_provincica_precaria1 *100)/ viviendas_totales
            
            
            cantidad_viviendas_sin_retrete += x.sanitario.sin_retrete
            cantidad_viviendas += x.sanitario.con_retrete
            porcentaje_sin_retrete = (cantidad_viviendas_sin_retrete * 100) / cantidad_viviendas
            
            procentaje_total =  porcentaje_viviendas_precarias+ porcentaje_sin_retrete
            porcentajes.append(( x.nombre, porcentaje_analfabetos_totales, procentaje_total  ))
        for i in range(len(porcentajes)-1):
            for j in range(len(porcentajes)-i-1):
                if porcentajes[j][1] > porcentajes[j+1][1]:
                    porcentajes[j], porcentajes[j+1] = porcentajes[j+1], porcentajes[j]
       
        n = len(porcentajes)
        sumatoria_xy = 0.0
        sumatoria_x = 0.0
        sumatoria_y = 0.0
        sumatoria_x_2 = 0.0
        sumatoria_y_2 = 0.0
        a_1 = 0
        a_0 = 0
        for par in porcentajes:
            # Σxy
            sumatoria_xy += par[1] * par[2]
            # Σx
            sumatoria_x += par[1]
            # Σy
            sumatoria_y += par[2]
            # Σx²
            sumatoria_x_2 += par[1]**2
            #
            sumatoria_y_2 += par[2]**2
        a_1 = (n * (sumatoria_xy) - (sumatoria_y*sumatoria_x))/(n*(sumatoria_x_2)-sumatoria_x**2)
        a_0 = (sumatoria_y/n) - a_1 * (sumatoria_x/n)
        if debug == True:
            print("\n === debug ===")
            print("  Σxy: ", sumatoria_xy)
            print("  Σx : ", (sumatoria_x) )
            print("  Σy : ", (sumatoria_y) )
            print("  Σx²: ", sumatoria_x_2)
            print("  Σy²: ", sumatoria_y_2,"\n")
            print("%6.2fx + %6.2fy" % (a_0, a_1))
            numerador = (a_0 * sumatoria_y) + (a_1 * sumatoria_xy) - (len(porcentajes) * (sumatoria_y/len(porcentajes))**2)
            denominnador = sumatoria_y_2 - (sumatoria_y/len(porcentajes))**2
            coeficiente_determinacion = numerador / denominnador
            print("coeficiente ", coeficiente_determinacion)
        else:
             print("no se puede ejecutar esa operacion")

        
            





       
    
   
    

class Provincia:
    cod = None
    nombre = None
    alfabetismo = None #para contener un objeto de la clase Alfabetismo
    sanitario = None #para contener un objeto de la clase Sanitario
    viviendas = [] #list para contener todos los tipos de viviendas
    def __init__(self, c, n, a, r, v):
        self.cod = c
        self.nombre = n
        self.alfabetismo = a
        self.sanitario = r
        self.viviendas = v

    #Devuelve todos: varones más mujeres
    def get_total_poblacion(self):
        return self.alfabetismo.get_total()
        
    def get_cod(self):
        return self.cod


class PorSexo:
    varones = None
    mujeres = None
    def __init__(self, v, m):
        self.varones = v
        self.mujeres = m
   
    #Devuelve todos: varones más mujeres
    def get_total(self):
        return self.varones + self.mujeres
    def get_varones(self):
      return self.varones


class Alfabetismo:
    alfabetos = None #para contener un objeto de clase PorSexo con datos de la personas alfabetas
    analfabetos = None #para contener un objeto de clase PorSexo con datos de la personas analfabetas    
    def __init__(self, a, no_a):
        self.alfabetos = a
        self.analfabetos = no_a

    #Total de la población: alfabetas + analfabetas
    def get_total(self):
        return self.alfabetos.get_total() + self.analfabetos.get_total()


class Sanitario:
    con_retrete = None
    sin_retrete = None
    def __init__(self, c, s):
        self.con_retrete = c
        self.sin_retrete = s


class Vivienda:
    """
     TIPO (según INDEC):
        0: Casa
        1: Rancho
        2: Casilla
        3: Departamento
        4: Pieza/s en inquilinato
        5: Pieza/s en hotel o pensión
        6: Local no construido para habitación
        7: Vivienda móbil
    """
    tipo = None
    cantidad = None
    def __init__(self, t, c):
        self.tipo = t
        self.cantidad = c


#Fuente de datos: https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-135

arg = Pais([
    Provincia(0, 'Ciudad Autónoma de Buenos Aires', Alfabetismo(PorSexo(1160483, 1395255), PorSexo(5344, 7059)), Sanitario(1061211, 21787), [Vivienda(0, 252771), Vivienda(1, 565), Vivienda(2, 1884), Vivienda(3, 788791), Vivienda(4, 19571), Vivienda(5, 17082), Vivienda(6, 2237), Vivienda(7, 97)]),
    Provincia(1, '24 partidos del Gran Buenos Aires', Alfabetismo(PorSexo(3917957, 4223950), PorSexo(55416, 61809)), Sanitario(2294650, 358638), [Vivienda(0, 2212645), Vivienda(1, 17794), Vivienda(2, 73827), Vivienda(3, 329731), Vivienda(4, 12452), Vivienda(5, 1405), Vivienda(6, 5091), Vivienda(7, 343)]),
    Provincia(2, 'Interior de la provincia de Buenos Aires', Alfabetismo(PorSexo(2285525, 2438254), PorSexo(33289, 28494)), Sanitario(1625106, 146799), [Vivienda(0, 1502191), Vivienda(1, 12283), Vivienda(2, 35724), Vivienda(3, 212714), Vivienda(4, 4117), Vivienda(5, 817), Vivienda(6, 3026), Vivienda(7, 1033)]),
    Provincia(3, 'Catamarca', Alfabetismo(PorSexo(144528, 148625), PorSexo(3108, 2928)), Sanitario(75871, 13505), [Vivienda(0, 83578), Vivienda(1, 2134), Vivienda(2, 400), Vivienda(3, 2666), Vivienda(4, 427), Vivienda(5, 30), Vivienda(6, 96), Vivienda(7, 45)]),
    Provincia(4, 'Chaco', Alfabetismo(PorSexo(394795, 411225), PorSexo(22440, 24292)), Sanitario(916669, 61884), [Vivienda(0, 236946), Vivienda(1, 12558), Vivienda(2, 5696), Vivienda(3, 12052), Vivienda(4, 2048), Vivienda(5, 165), Vivienda(6, 424), Vivienda(7, 244)]),
    Provincia(5, 'Chubut', Alfabetismo(PorSexo(205779, 206044), PorSexo(4049, 4265)), Sanitario(197102, 51742), [Vivienda(0, 122955), Vivienda(1, 1479), Vivienda(2, 1917), Vivienda(3, 19318), Vivienda(4, 1068), Vivienda(5, 58), Vivienda(6, 237), Vivienda(7, 144)]),
    Provincia(6, 'Córdoba', Alfabetismo(PorSexo(1314229, 1425717), PorSexo(22334, 18451)), Sanitario(176147, 93986), [Vivienda(0, 840488), Vivienda(1, 5929), Vivienda(2, 2775), Vivienda(3, 124044), Vivienda(4, 2852), Vivienda(5, 791), Vivienda(6, 1199), Vivienda(7, 475)]),
    Provincia(7, 'Corrientes', Alfabetismo(PorSexo(372493, 399455), PorSexo(17969, 16523)), Sanitario(136043, 11133), [Vivienda(0, 210288), Vivienda(1, 13056), Vivienda(2, 8147), Vivienda(3, 14201), Vivienda(4, 2293), Vivienda(5, 236), Vivienda(6, 393), Vivienda(7, 230)]),
    Provincia(8, 'Entre Ríos', Alfabetismo(PorSexo(486281, 519080), PorSexo(12294, 9610)), Sanitario(326978, 30272), [Vivienda(0, 317956), Vivienda(1, 3805), Vivienda(2, 7273), Vivienda(3, 26680), Vivienda(4, 644), Vivienda(5, 176), Vivienda(6, 495), Vivienda(7, 221)]),
    Provincia(9, 'Formosa', Alfabetismo(PorSexo(200956, 206992), PorSexo(7821, 9575)), Sanitario(79122, 51012), [Vivienda(0, 109807), Vivienda(1, 12203), Vivienda(2, 1514), Vivienda(3, 4124), Vivienda(4, 2104), Vivienda(5, 44), Vivienda(6, 229), Vivienda(7, 109)]),
    Provincia(10, 'Jujuy', Alfabetismo(PorSexo(261419, 269965), PorSexo(5404, 11784)), Sanitario(122201, 32710), [Vivienda(0, 134293), Vivienda(1, 7286), Vivienda(2, 2595), Vivienda(3, 7824), Vivienda(4, 2510), Vivienda(5, 74), Vivienda(6, 245), Vivienda(7, 84)]),
    Provincia(11, 'La Pampa', Alfabetismo(PorSexo(128679, 133208), PorSexo(2805, 2227)), Sanitario(101706, 3091), [Vivienda(0, 95356), Vivienda(1, 458), Vivienda(2, 169), Vivienda(3, 8239), Vivienda(4, 317), Vivienda(5, 10), Vivienda(6, 177), Vivienda(7, 71)]),
    Provincia(12, 'La Rioja', Alfabetismo(PorSexo(131833, 136616), PorSexo(2843, 2154)), Sanitario(75564, 10803), [Vivienda(0, 77743), Vivienda(1, 1970), Vivienda(2, 1643), Vivienda(3, 4208), Vivienda(4, 597), Vivienda(5, 56), Vivienda(6, 105), Vivienda(7, 45)]),
    Provincia(13, 'Mendoza', Alfabetismo(PorSexo(681053, 730907), PorSexo(15527, 16003)), Sanitario(421292, 38258), [Vivienda(0, 398510), Vivienda(1, 7618), Vivienda(2, 1985), Vivienda(3, 48846), Vivienda(4, 1686), Vivienda(5, 216), Vivienda(6, 595), Vivienda(7, 94)]),
    Provincia(14, 'Misiones', Alfabetismo(PorSexo(412901, 422882), PorSexo(17110, 18662)), Sanitario(201604, 88659), [Vivienda(0, 249745), Vivienda(1, 7866), Vivienda(2, 11548), Vivienda(3, 16938), Vivienda(4, 3376), Vivienda(5, 77), Vivienda(6, 560), Vivienda(7, 153)]),
    Provincia(15, 'Neuquén', Alfabetismo(PorSexo(219539, 225070), PorSexo(5120, 5339)), Sanitario(145697, 13605), [Vivienda(0, 130466), Vivienda(1, 1924), Vivienda(2, 3425), Vivienda(3, 21312), Vivienda(4, 1743), Vivienda(5, 83), Vivienda(6, 228), Vivienda(7, 121)]),
    Provincia(16, 'Río Negro', Alfabetismo(PorSexo(255390, 262917), PorSexo(6541, 6539)), Sanitario(171370, 19227), [Vivienda(0, 155561), Vivienda(1, 2149), Vivienda(2, 4091), Vivienda(3, 27071), Vivienda(4, 1230), Vivienda(5, 72), Vivienda(6, 331), Vivienda(7, 92)]),
    Provincia(17, 'Salta', Alfabetismo(PorSexo(459258, 478751), PorSexo(12710, 17657)), Sanitario(202113, 64962), [Vivienda(0, 220293), Vivienda(1, 14806), Vivienda(2, 11076), Vivienda(3, 17161), Vivienda(4, 2881), Vivienda(5, 120), Vivienda(6, 450), Vivienda(7, 288)]),
    Provincia(18, 'San Juan', Alfabetismo(PorSexo(260076, 278149), PorSexo(6360, 5133)), Sanitario(142970, 19234), [Vivienda(0, 134753), Vivienda(1, 11219), Vivienda(2, 1075), Vivienda(3, 14489), Vivienda(4, 405), Vivienda(5, 43), Vivienda(6, 196), Vivienda(7, 24)]),
    Provincia(19, 'San Luis', Alfabetismo(PorSexo(170030, 177358), PorSexo(3674, 2838)), Sanitario(108089, 9677), [Vivienda(0, 104692), Vivienda(1, 1125), Vivienda(2, 470), Vivienda(3, 10380), Vivienda(4, 654), Vivienda(5, 106), Vivienda(6, 208), Vivienda(7, 131)]),
    Provincia(20, 'Santa Cruz', Alfabetismo(PorSexo(113297, 106023), PorSexo(1291, 1213)), Sanitario(72841, 3392), [Vivienda(0, 64118), Vivienda(1, 524), Vivienda(2, 852), Vivienda(3, 9339), Vivienda(4, 1181), Vivienda(5, 43), Vivienda(6, 118), Vivienda(7, 58)]),
    Provincia(21, 'Santa Fe', Alfabetismo(PorSexo(1273525, 1383361), PorSexo(25003, 23092)), Sanitario(862253, 86116), [Vivienda(0, 793209), Vivienda(1, 10303), Vivienda(2, 8279), Vivienda(3, 132409), Vivienda(4, 2023), Vivienda(5, 796), Vivienda(6, 1119), Vivienda(7, 231)]),
    Provincia(22, 'Santiago del Estero', Alfabetismo(PorSexo(328348, 340598), PorSexo(14809, 13061)), Sanitario(122529, 75377), [Vivienda(0, 169162), Vivienda(1, 20833), Vivienda(2, 1097), Vivienda(3, 5830), Vivienda(4, 463), Vivienda(5, 75), Vivienda(6, 223), Vivienda(7, 223)]),
    Provincia(23, 'Tierra del Fuego, Antártida e Islas del Atlántico Sur', Alfabetismo(PorSexo(52991, 50430), PorSexo(347, 358)), Sanitario(35041, 1648), [Vivienda(0, 25108), Vivienda(1, 102), Vivienda(2, 3817), Vivienda(3, 7326), Vivienda(4, 226), Vivienda(5, 43), Vivienda(6, 44), Vivienda(7, 23)]),
    Provincia(24, 'Tucumán', Alfabetismo(PorSexo(557210, 596990), PorSexo(15859, 13295)), Sanitario(276897, 58924), [Vivienda(0, 287900), Vivienda(1, 4931), Vivienda(2, 11031), Vivienda(3, 30431), Vivienda(4, 897), Vivienda(5, 184), Vivienda(6, 344), Vivienda(7, 103)])
])




while True:
            print("1. ¿Queres saber la poblacion total?")
            print("2. ¿Querés saber la cantidad de personas censadas por sexo?")
            print("3. Mostrar ratio de habitantes por vivienda por provincia")
            print("4. Mostrar el porcentaje de analfabetismo por sexo")
            print("5. Mostrar el porcentaje de analfabetismo por provincias")
            print("6. Mostrar el porcentaje de viviendas sin retrete por provincias")
            print("7. Mostrar el porcentaje de viviendas precarias por provincias")
            print("8. Mostrar correlacion lineal")
            print("9. Salir")
            
            
            opcion = input("Elija la opción deseada: ")
            # Mostramos un menú de opciones al usuario y le solicitamos que elija una opción.

            if opcion == "1":
                 Pais.mostrar_totales_poblacion(arg) # muestra la poblacion total censada
                
            elif opcion == "2":
                 Pais.cantidad_de_varones(arg) # cantidad de varones censados 
                 Pais.cantidad_de_mujeres(arg)# cantidad de mujeres censadas 
                
                

            elif opcion == "3":
                 Pais.mostrar_ratio_habitantes_por_vivienda_por_provincia(arg) # Nos muestra el ratio de habitantes por viviendas 
            elif opcion == "4": 
                Pais.mostrar_porcentaje_analfabetismo_por_sexo(arg) # Nos muestra el porcetaje de analfabetismo por sexo
            elif opcion == "5":  
                 Pais.mostrar_porcentaje_analfabetismo_por_provincia(arg) # Nos muestra el porcetaje de analfabetismo por sexo pero por provincia 
                
            elif opcion == "6":     
                 Pais.mostrar_porcentaje_vivendas_sin_retrete_por_provincia(arg) # Nos muestra el porcentaje de viviendas sin retrete por provincia 
                
            elif opcion == "7":  
                 Pais.mostrar_porcentaje_vivienda_precaria_por_provincia(arg) # Nos muestra el porcentaje de viviendas precaria por provincia 
                
            elif opcion == "8":
                 Pais.mostrar_correlacion_alfabetismo_vs_vivienda_y_retrete(arg) #Noe mestra la correlacion con  el porcentaje de analfabetos y viviendas precarias 

            elif opcion == "9":# opcion 8 de terminar el programa 
                break
            else:
                print("Opción inválida.")
                # Si el usuario elige una opción inválida, mostramos un mensaje de error.









