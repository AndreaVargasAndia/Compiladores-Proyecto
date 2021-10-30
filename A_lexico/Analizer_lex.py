
T_operadores=["OP-SUM","OP-REST","OP-DoblePunt","OP-DIFIG","OP-EXIG","OP-IG"]
T_delimitadores=["D-COMA","D-PIZQ","D-PDER","D-CIZQ","D-CDER"]
T_reservada=["R-STRT","R-END","R-FUNC","R-IF","R-ELSEIF","R-ELSE","R-WHL","R-PRNT","R-RV","R-SV","R-CV","R-EA"]
T_val=["VL-INT","VL-DBL","VL-STRNG","VL-VAR"]
T_ID=["ID"]
operadores=["+","-",":","!=","==","="]
delimitadores=[",","(",")","{","}"]
reservada=["start","end","func","if","elseif","else","while","print","read_vid","save_vid","cut_vid","extrac_audio"]
numeros=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","."]

def convert_s(s):
    str1 = ""
    return(str1.join(s))

class tokenClass:
    tipo_tk=""
    lexema=""
    def descrip_tk(self):
        return "[ Tipo: "+self.tipo_tk+" / LEXEMA: "+self.lexema+" ]"

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
    p=list_.index(val)
    #print("p",p)
    return p
    #for i in range(0,len(list_)):
    #    print("i",i)
    #    if list_[i]==convert_s(val):
    #        return i
    #    else:
    #        return -1
        

def detec_number(lx):
    token=tokenClass()
    token.lexema=lx
    #token.tipo_tk="Numero "
    if token.lexema.find(".")<0:
        token.tipo_tk+=T_val[0]#'int'
    else:
        token.tipo_tk+=T_val[1]#'double'
    return token

def detec_delimitador(lx):
    token=tokenClass()
    token.lexema=lx
    pos=obtener_pos(delimitadores,lx)
    #print("val ",lx)
    #print("pos ",pos)
    token.tipo_tk=T_delimitadores[pos]    
    return token

def detec_operator(lx):
    token=tokenClass()
    token.lexema=lx
    pos=obtener_pos(operadores,lx)
    token.tipo_tk=T_operadores[pos]#"Operador "    
    return token

def detec_reservada(lx):
    token=tokenClass()
    token.lexema=lx
    pos=obtener_pos(reservada,lx)
    token.tipo_tk=T_reservada[pos] #"Reservada "    
    return token

def detec_variable(lx):
    token=tokenClass()
    token.lexema=lx
    token.tipo_tk=T_val[3]#"Variable "    
    return token

def detec_cadena(lx):
    token=tokenClass()
    token.lexema=lx
    token.tipo_tk=T_val[2]#"Cadena "    
    return token
    
#def detec_coment(lx):
    token=tokenClass()
    token.lexema=lx
    token.tipo_tk="Comentario "    
    return token

def isDigit_(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

tokn_=[]

def analizador(linea):

    letr_sp=[]
    pal=""
    idx=0
    comilla=1
    while idx<len(linea):
        #print("idx: ",linea[idx])
        if linea[idx]==' ':
            #print("<espacio>")
            letr_sp.append(pal)
            pal=""

        elif(linea[idx]=='\n'):	
            #print("<salto de linea>")
            letr_sp.append(pal)
            pal=""

        elif(linea[idx]=='"' and comilla<=2):
            pal+=linea[idx]
            if(comilla==2):
                letr_sp.append(pal)
                pal=""
            comilla=comilla+1

        elif (convert_s(linea[idx]) in delimitadores)==True: 
            #print("pal",pal)
            letr_sp.append(linea[idx])
            pal=""

        elif(linea[idx]=='#' ):
            pal+=linea[idx]
            if(linea[idx]==' '):
                letr_sp.append(pal)
                pal=""
        else:
            pal+=linea[idx]
        idx=idx+1

    j=0
    for h in letr_sp:
        h_=convert_s(h)
        #print("h: ",h) 
        if h !='\0':
            #print("tipo",type(h_))
            ch=h_[:1]
            #ch=[x[0] for x in h_]
            #print("ch", ch)
            if isDigit_(h_):
                #print("digit h: ",h)    
                tk_=detec_number(h)
                tokn_.append(tk_)
                #print(tk_.descrip_tk())
            elif h in operadores:
                tk_=detec_operator(h)
                tokn_.append(tk_)
                #print(tk_.descrip_tk())
            elif h in delimitadores:
                tk_=detec_delimitador(h)
                tokn_.append(tk_)
                #print(tk_.descrip_tk())
            elif h in reservada:
                tk_=detec_reservada(h)
                tokn_.append(tk_)
                #print(tk_.descrip_tk())
            elif h.isalpha():
                tk_=detec_variable(h)
                tokn_.append(tk_)
                #print(tk_.descrip_tk())
            elif ch=='"':
                #print("holaaaa",h_[0])
                tk_=detec_cadena(h)
                tokn_.append(tk_)
            #elif ch=='#':
                #print("holaaaa",h_[0])
                #tk_="[Comentario :  "+h+"]"
                #tokn_.append(tk_)
                #print(tk_.descrip_tk())
            	
    return tokn_   



if __name__ == '__main__':
    #print("hola")
    #archivo = open('datos.txt', 'r')
   
    #analizadorlex.gentokens(archivo)
    archivo = open('archivTXT/datos.txt', 'r')
    
    for linea in archivo:
        #print("linea",linea)
        tokens=analizador(linea)
    #t=tokenClass()
    for t in tokens:
        print(t.descrip_tk())

    #for tk in tokens:
    #    print(tk.descrip_tk())
    #for linea in archivo:
    #    tokens=analizadorLexico(linea)
    

