operadores=["+","-",":","!=","==","="]
delimitadores=[",","(",")","{","}"]
reverdada=["func","if","elseif","else","while","print","read_vid","save_vid","cut_vid","extrac_audio"]
numeros=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","."]

def convert_s(s):
    str1 = ""
    return(str1.join(s))

class tokenClass:
    tipo_tk=""
    lexema=""
    def descrip_tk(self):
        return "[ Tipo: "+self.tipo_tk+"- LEXEMA: "+self.lexema+"]"

def Getchar(var,pos):
    l=var
    nx=pos+1
    if nx>=len(l):
        return var
    if nx<len(l):
        return var[nx]

def Peekchar(var,pos):
    next=var
    s_pos=pos+1
    if s_pos>=len(next):
        return next
    if s_pos<len(next):
        return next[s_pos]


def obtener_pos(list_,val):
    for i in range(0,len(list_)):
        if list_[i]==convert_s(val):
            return i
        else:
            return -1

def detec_number(lx):
    token=tokenClass()
    token.lexema=lx
    token.tipo_tk="Numero "
    if token.lexema.find(".")<0:
        token.tipo_tk+='int'
    else:
        token.tipo_tk+='double'
    return token

def detec_delimitador(lx):
    token=tokenClass()
    token.lexema=lx
    token.tipo_tk="Delimitador "    
    return token

result=[]
def gentokens(linea):
    #archivo):
    tokens=[]
    c=""
    #while id < len(linea):
    for id in range(0,len(linea)):
        #print(linea[id])   
        #pos=obtener_pos(delimitadores,linea[id])
        #comp=linea[id] in delimitadores
        if (convert_s(linea[id]) in delimitadores)==True:   
            #print(linea[id]) 
            tk="[ Tipo: Delimitador - LEXEMA: "+linea[id]+"]"
            result.append(tk)
            #token=detec_delimitador(convert_s(linea[id]))
            #tokens.append(token)
            #id +=1
        elif linea[id]==' ':
            print("<espacio>")
            #id=id+1
        elif(linea[id]=='\n'):	
            print("<salto de linea>")
        elif(convert_s(linea[id]) in operadores)==True:
            #if(Getchar(linea[id])) in operadores:  
            tk="[ Tipo: Operador - LEXEMA: "+linea[id]+"]"
            result.append(tk)
        elif(convert_s(linea[id]) in operadores)==True:
            if(Getchar(linea,id)) in operadores: 
                print("lim") 
                print(linea[id])
            tk="[ Tipo: Numero - LEXEMA: "+linea[id]+"]"
            result.append(tk)
        	
    return tokens    



if __name__ == '__main__':
    print("hola")
    #archivo = open('datos.txt', 'r')
   
    #analizadorlex.gentokens(archivo)
    archivo = open('datos.txt', 'r')
    for linea in archivo:
        tokens=gentokens(linea)
    for tk in result:
        print(tk)

    #for tk in tokens:
    #    print(tk.descrip_tk())
    #for linea in archivo:
    #    tokens=analizadorLexico(linea)
    

