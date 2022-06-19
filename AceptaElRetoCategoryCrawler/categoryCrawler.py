
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser

def getCategoria():
    
    ej = int(input("Dame la id del ejercicio tron: "))
    
    dict = {}
    for i in range(4,124):        
		#vamos a saltarnos las categorias que tienen subcategorias en vez de ejercicios
        if i!=12 and i!=30 and i!=45 and i!=50 and i!=62 and i!=69 and i!=24 and i!=35 and i!=46 and i!=47 \
		and i!=95 and i!=51 and i!=82 and i!=101 and i!=83 and i!=89 and i!=103 and i!=112 and i!=121 and i!=52 \
		and i!=55 and i!=58 and i!=73 and i!=79 and i!=92 and i!=97 and i!=107 and i!=116:     
            browser = RoboBrowser(history=True,parser="html.parser")
            browser.open("https://www.aceptaelreto.com/problem/statement.php?id=" + str(ej) + "&cat=" + str(i))
            soup = browser.parsed
            soup.encode("utf-8")
            j = 0
            name = ""
            mostrar = False
            aux2=""
            for content in soup.find_all("a"):
                aux = content.findAll(text=True)
                aux = str(aux)
                if(mostrar==True):
                    if "Enunciado" in aux:                
                        mostrar=False
                        print(str(i) + ":" + aux2)
                    else:
                        aux2 = aux2+aux
                if "Por cat" in aux: 
                    mostrar = True      
getCategoria()
