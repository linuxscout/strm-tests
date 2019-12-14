import random
import sympy
from sympy.logic import SOPform
from sympy.logic import POSform
from sympy import symbols
from sympy.logic.boolalg import to_cnf, to_dnf

FUNCTIONS=[{"ID":"", "desc":"",
    "arabic":"",
    "minterms":[],
    "logigram":"",
},
]
import itertools

class logigram:
    """ Trace a latex logigram for a given function"""
    def __init__(self,):
        pass
    def draw_logigram(self, sop):
        """ draw a logigram from an sop """
        latex = " \\begin{tikzpicture}\n\n"
        terms = sop.upper().split("+")
        latex += self.draw_vars(len(terms))
        for cpt, term in enumerate(terms):
            latex += self.draw_gate(term, cpt)
        latex += self.draw_large_or(len(terms))
        latex += " \\end{tikzpicture}\n\n"        
        return latex
    def normalize_latex(self,s):
        """ normalize boolean string"""
        s= str(s)
        s = s.replace("A'","\\bar A")
        s = s.replace("B'","\\bar B")
        s = s.replace("C'","\\bar C")
        s = s.replace("D'","\\bar D")
        s = s.replace("a'","\\bar a")
        s = s.replace("b'","\\bar b")
        s = s.replace("c'","\\bar c")
        s = s.replace("d'","\\bar d")
        return s        
    def draw_vars(self,size):
        """ draw vars lines """
        latex ="""\\node (x) at (0, ID*1.5) {$A$};
            \\node (y) at (0.5, ID*1.5) {$B$};
            \\node (z) at (1, ID*1.5) {$C$};
            \\node (w) at (1.5, ID*1.5) {$D$};
            \\node[not gate US, draw, rotate=270] at ($(x) + (0.25, -0.3)$) (notx) {};
            \\draw (x) -- (notx.input); 
            \\node[not gate US, draw, rotate=270] at ($(y) + (0.25, -0.3)$) (noty) {};
            \\draw (y) -- (noty.input); 
            \\node[not gate US, draw, rotate=270] at ($(z) + (0.25, -0.3)$) (notz) {};
            \\draw (z) -- (notz.input);
            \\node[not gate US, draw, rotate=270] at ($(w) + (0.25, -0.3)$) (notw) {};
            \\draw (w) -- (notw.input);
        """
        latex = latex.replace("ID", str(size))
        return latex
                
    def draw_large_or(self, size):
        """ draw the final or gate"""
        latex = """\\node[or gate US, draw, rotate=0, logic gate inputs=n%s] at (5.5, %d*0.5) (xory) {};\n\n
                    \draw (xory.output) -- node[above]{\scriptsize$F$} ($(xory) + (1, 0)$);\n\n"""%("n"*size, size)
        offset = 1.4
        for i in range(size):
            latex +="""\\draw (xandy%d.output) -- ([xshift=%.2fcm]xandy%d.output) |- (xory.input %d);\n\n"""%(i, offset, i, size-i)
            if i < size/2:
                offset -=0.05
            else:
                offset +=0.05
        return latex

  
    def draw_gate(self, term, idg):
        """ id gate """
        latex_term = self.normalize_latex(term)
            
        #~ latex = """
        #~ \\begin{tikzpicture}"""
        latex = """        
           
            \\node[and gate US, draw, rotate=0, logic gate inputs=nnnn] at (2.5, ID*1.5) (xandyID) {};
            \\draw (xandyID.output) -- node[above]{\scriptsize $%s$} ($(xandyID) + (1.8, 0)$);
            """%latex_term
        if "A'" in term:
            latex += """
            %% X'

            \\draw  [line width=0.25mm,   red] (notx.output) -- ([xshift=0cm]notx.output) |- (xandyID.input 1);
            """
        elif "A" in term:
            latex += """%% X
            \\draw (x) -| ($(x) + (0, 0)$) |- (xandyID.input 1);
            """
        if "B'" in term:
            latex += """
            %Y'

            \\draw [line width=0.25mm,   red] (noty.output) -- ([xshift=0cm]noty.output) |- (xandyID.input 2);
          """
        elif "B" in term:
            latex +="""  
            %% Y
            \\draw (y) -| ($(y) + (0, 0)$) |- (xandyID.input 2);
        """
        if "C'" in term:
            latex += """
            %%Z'

            \\draw [line width=0.25mm,   red] (notz.output) -- ([xshift=0cm]notz.output) |- (xandyID.input 3);
          """
        elif "C" in term:
            latex +="""
            %%Z
            \\draw (z) -| ($(z) + (0, 0)$) |- (xandyID.input 3);
        """
        if "D'" in term:
            latex += """
            %%W

            \\draw [line width=0.25mm,   red] (notw.output) -- ([xshift=0cm]notw.output) |- (xandyID.input 4);
          """
        elif "D" in term:
            latex +="""    %%W
            \\draw (w) -| ($(w) + (0, 0)$) |- (xandyID.input 4);
        """
            
        #~ latex +=""" 
        #~ \\end{tikzpicture}
        #~ """
        latex = latex.replace("ID", str(idg))
        return latex        
class bool_quiz:
    def __init__(self):
        pass
        
    def rand_funct(self,):
        """ generate random function"""
        minterms = random.sample(range(16),random.randrange(4,12))
        minterms.sort()
        return  minterms
        
        
    def rand_exp(self, nb=2):
        """ generate random expression"""
        minterms_table = []
        sop_quest  = []
        for i in range(nb):
            minterms = random.sample(range(16),random.randrange(3,12))
            minterms.sort()
            minterms_table +=minterms
            sop, _ = self.simplify(minterms)            
            sop_quest.append(sop)
        sop_quest = " + ".join(sop_quest)
        minterms_table =list(set(minterms_table))
        minterms_table.sort()
        
        return  sop_quest, minterms_table      


    def truth_table(self, minterms, latex=False, dontcares=[]): 
        """ print truth table """
        variables = ["","A", "B","C", "D", "F"]
        cases = itertools.product([0,1],[0,1],[0,1],[0,1])
        text = "\t".join(variables)
        tex = """%%\\begin{table}
        \\begin{tabular}{|c|c|c|c|c||c|}
    \\toprule
        """
        tex += " & ".join(variables) 
        tex += "\\\\ \\midrule"
           
        for counter, item in enumerate(cases):
            f = 1 if counter in minterms else 0
            case = [counter] + list(item)+ [f]
            if counter  and counter %4 ==0 :
                tex += "\\midrule"
            text += "\t".join([str(x) for x in case]) +"\n"
            tex += " & ".join([str(x) for x in case]) + "\\\\"

        tex += """\\bottomrule
        \\end{tabular}
        %%\\end{table}
        """
        if latex:
            return tex
        else:
            return text
            
    def normalize(self, s, mode=True):
        """ normalize boolean string
        mode SOP True, False is POS
        """
        s= str(s)
        s = s.replace(" & ",".")
        s = s.replace(" | ","+")
        s = s.replace("~a","a'")
        s = s.replace("~b","b'")
        s = s.replace("~c","c'")
        s = s.replace("~d","d'")
        # reorder terms
        if mode:
            var_op = "."
            term_op = "+"
        else:
            var_op = "+"
            term_op = "-"
        
        # treat as SOP
        # ajust terms and order them"""
        terms = s.split(term_op)
        tmp = []
        for term in terms:
            # remove parenthesis
            if mode:
                term = term.replace('(','')
                term = term.replace(')','')
            varbs = term.split(var_op)
            varbs.sort()
            term = var_op.join(varbs)
            tmp.append(term)
        return term_op.join(tmp)


    def simplify(self, minterms, dontcares=[]):
       
        a,b,c,d = symbols("a b c d")
        sop = sympy.SOPform([a,b,c,d], minterms, dontcares)
        pos = sympy.POSform([a,b,c,d], minterms, dontcares)
        
        sop = self.normalize(sop)
        pos = self.normalize(pos, False)
        return sop, pos
    
    def minterm(self, n):
        """ return a minterm for integer"""
        term =[]
        for var in 'dcba':
            v = var if n % 2 ==1 else var +"'"
            n = n / 2
            term.append(v)
        term.sort()
        return ".".join(term)
        
    def maxterm(self,n):
        term =[]         
        """ return a minterm for integer"""
        for var in 'dcba':
            v = var if n % 2 ==0 else var +"'"
            n = n / 2
            term.append(v)
        term.sort()
        return ".".join(term)
        
    def form_canonique(self, minterms, dontcares=[]):
        a,b,c,d = symbols("a b c d")
        maxterms = [x for x in range(16) if x not in minterms and x not in dontcares]
        dnf = " + ".join([self.minterm(x) for x in minterms])
        cnf = ".".join([self.maxterm(x) for x in range(16) if x in maxterms])
        
        return cnf, dnf
        
    def draw_map(self, minterms, dontcares=[], latex=False):
        kmap=[]
        maxterms = [x for x in range(16) if x not in minterms and x not in dontcares]
        for x in range(16):
            if x  in minterms:
                kmap.append("1")
            elif x in dontcares:
                kmap.append("x")
            else:
                kmap.append("0")
        table = [ ["ab\\cd", "00","01", "11","10"],
        ["00", kmap[0], kmap[1],kmap[3],kmap[2]],
        ["00", kmap[4], kmap[5],kmap[7],kmap[6]],
        ["00", kmap[12], kmap[13],kmap[15],kmap[14]],
        ["00", kmap[8], kmap[9],kmap[11],kmap[10]],
        ]
        text = "\n".join(["\t".join(r) for r in table])
        tex =  """\\begin{karnaugh-map}[4][4][1][cd][ab]
          \\minterms{%s}
          \\maxterms{%s}
        %%\\autoterms[0]
          %%\\implicant{5}{15}
          %%\\implicantedge{8}{8}{10}{10}
          %%\\implicantedge{8}{8}{10}{10}[8,10]
        \\end{karnaugh-map}"""%(", ".join([str(x) for x in minterms]), ", ".join([str(x) for x in maxterms]))
        if latex:
            return tex         
        else:
            return text
    def normalize_latex(self,s):
        """ normalize boolean string"""
        s= str(s)
        s = s.replace("A'","\\bar A")
        s = s.replace("B'","\\bar B")
        s = s.replace("C'","\\bar C")
        s = s.replace("D'","\\bar D")
        s = s.replace("a'","\\bar a")
        s = s.replace("b'","\\bar b")
        s = s.replace("c'","\\bar c")
        s = s.replace("d'","\\bar d")
        return s

            
    def draw_logigram(self, sop):
        """ draw a logigram """
        lg = logigram()
        return lg.draw_logigram(sop)
def test1():
    bq = bool_quiz()
    minterms = bq.rand_funct()
    print "minterms"
    print(minterms)
    print "maxnterms"
    maxterms = [x for x in range(16) if x not in minterms]
    maxterms = list(set(range(16)) -set(minterms))
    [x for x in range(16) if x not in minterms]
    print(maxterms)
    bq.truth_table(minterms)
    sop, pos =bq.simplify(minterms)
    print "Simplified Sum of products\n", sop
    print "Simplified Product of sums\n", pos
    cnf, dnf =bq.form_canonique(minterms)
    print "Sum of products\n", dnf
    print "Product of sums\n", cnf
    print "Karnough map"
    print(bq.draw_map(minterms))
    print "Karnough map Latex"
    print(bq.draw_map(minterms, latex=True))
    print(bq.draw_logigram(sop))
def test2():
    bq = bool_quiz()
    minterms = bq.rand_funct()
    maxterms = list(set(range(16)) -set(minterms))
    sop, pos =bq.simplify(minterms)
    print(bq.draw_logigram(sop))    
# Driver Code 
if __name__ == "__main__" :
    test2()

    
    
