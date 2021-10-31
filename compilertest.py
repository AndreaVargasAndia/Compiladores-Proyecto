from A_lexico.Analizer_lex import *
from ll1.parse import parse_tree


def ll1_(token_):
    archiv = open('archivTXT/grammar.txt','r')
    #archiv = open('archivTXT/grammar_prub.txt','r')
    grammar = archiv.read()
    parse_tree(grammar, token_)



if __name__ == '__main__':

    tokens_ = []

    archivo = open('archivTXT/correct.txt', 'r')
    for linea in archivo:
        tokens=analizador(linea)
     
    for t in tokens:
        #tokens_.append('$') 
        tokens_.append(t.tipo_tk)
        #ll1_(tokens_)
        #print(t.descrip_tk())
    #tokens_.append('$')  
    #for i in range(0,len(tokens_)):
    #    ll1_(tokens_[i])
    ll1_(tokens_)