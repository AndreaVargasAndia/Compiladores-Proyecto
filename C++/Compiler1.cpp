#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
vector<string> tk_operadores = { "OP-SUMA", "OP-RESTA", "OP-DP", "OP-DIFF", "OP-II","OP-I" };
vector<string> tk_reservada = { "R-FC", "R-IF", "R-EIF", "R-EL", "R-WHL", "R-P", "R-read_vid", "R-save_vid", "R-cut_vid", "R-extrac_audio" };
vector<string> tk_delimitadores = { "D-C", "D-P", "D-LL" };

//---------------------------------
vector<string> operadores = { "+", "-", ":", "!=", "==", "=" };
vector<string> delimitadores = { ",", "(", ")", "{", "}" };
vector<string> reservada = { "func", "if", "elseif", "else", "while", "print", "read_vid", "save_vid", "cut_vid", "extrac_audio" };
vector<string> numeros = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" };
vector<string> alf = {"a","b","c","d","e","f","g","h","i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};


class gentokens
{
public:
    string tipo_tkn;
    string lexema;
    gentokens();
    gentokens(string tk, string lx)
    {
        tipo_tkn = tk;
        lexema = lx;
    }
    string token_txt()
    {
        return " Token:" + tipo_tkn + " Lexema: " + lexema;
    }
};

class analizador_lexico {

public: 
    string resultado;

    char getchar(char* c) {
        c = (c + 1);
        return *c;// *(c + 1);

    }
    char peekchar(char* c) {
        char sig = *(c + 1);
        return sig;
    }

    int find_vector(vector<string> v, string f)
    {
        int tam = v.size();
        cout << "tam " << v.size() << endl;
        cout << "Buscar" << f << endl;
        int pos;
        for (int i = 0; i < tam; i++)
        {
            cout << "elementos" << v[i] << " ";
            if (v[i] == f)
            {
                pos = i;
                return pos;
            }            
        }
        return -2;
    }

    bool find_in_vector(vector<string> v, string f)
    {
        int tam = v.size();
        //cout << "tam " << v.size() << endl;
        //cout << "Buscar" << f << endl;
        int pos;
        for (int i = 0; i < tam; i++)
        {
            //cout << "elementos" << v[i] << " ";
            if (v[i] == f)
            {
                return true;
            }
        }
        return false;
    }

    bool detec_number(string l)
    {
        if (find_vector(numeros, l) > 0) { return true; }
        else { return false; }
    }
    bool detec_double(string l)
    {
        if (find_vector(numeros, l) > 0) { return true; }
        else { return false; }
    }
    int detec_OP(string val) {
        if (val == "+") {
            int i= find_vector(operadores, val);
            return i;
        }
        if (val == "-") {
            int i = find_vector(operadores, val);
            return i;
        }
        else
        {
            return -1;
        }      
    }
    string comprobar_palabra(string n) {
        string reconstruct = n;
        return n;
        //string n;
    }
    void analizar(string p){
        int j=0;
        vector<gentokens> tk;
        //for (int i = 0; i < p.size(); i++)
        //{
           // j = detec_OP(p);  
        
            if (find_in_vector(operadores,p)) {
                cout << "Operador: "<<p << endl;
            }
            else if (find_in_vector(delimitadores, p)) {
                cout << "Delimitador:"<<p << endl;
            }
            else if (find_in_vector(reservada, p)) {
                cout << "Reservada:"<<p << endl;
            }
            else if (find_in_vector(numeros, p)) {
                cout << "Numero:"<<p << endl;
            }
            else if (p.size()>1) {
                cout << "Palabra:" << p << endl;
            }
            else
            {
                cout << "Token no valido " << endl;
            }

//        }
        //cout << tk_operadores[j] << endl;

    }
    void prueba(string p) {
        cout << "----------------------- \n" << p << endl;
        cout << "-----------------------" << endl;
        //cout<<"get: "<<getchar(&p[1])<<endl;
        int j = 0;
        vector<string> w;
        string s;
        int k=0;
        
       /* while (p[k] != ' ')
        {
            w+= p[k];            
            k++;
        }*/
        //comprobar_palabra(w);
        //cout << "palabra " << w << endl;
        //analizar(w);

        for (int i = 0; i < p.size(); i++)
        {
            if (p[i] == ' ')
            {
                //cout << "espacio" << endl;
                cout << "palabraaaaa : " << s << endl;
                analizar(s);
                s = "";
            }
            
            else if(p[i] != '\n' )
            {
                string tmp="";
                tmp+= p[i];
                analizar(tmp);
                
                s += p[i];              
                
               // j = detec_OP(tmp);
               // cout << "j: "<<j << endl;
            }
            
            
            
            /*for (int h = 0; h < p[i].size(); h++)
            {
                string tmp = p[i];
                j = detec_OP(tmp[h]);
            }*/
            //j = detec_OP(p);
            else if (p[i] == '\n')
            {
                cout << "--> salto de linea"<<endl;
            }
        //j++;
           /*if (p[i + 1] == '\0')
           {
               cout << "fin";
           }*/
        }
        //cout << j << endl;
       // cout << tk_operadores[j] << endl;
       
    }


};
int main()
{
    //char cadena[128];
    ifstream archivo("D:/Compiladores21-2/Compiler1/datos.txt");
    string arch= string((std::istreambuf_iterator<char>(archivo)), std::istreambuf_iterator<char>());
    analizador_lexico AL;
    AL.prueba(arch);

    /*while (!archivo.eof()) {
        archivo >> cadena;
        cout << cadena << endl;
    }*/
    //archivo.close();
}
