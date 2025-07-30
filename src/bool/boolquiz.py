import random
import sympy
from sympy.logic import SOPform
from sympy.logic import POSform
from sympy import symbols
from sympy.logic.boolalg import to_cnf, to_dnf

from . import logigram
from . import bool_const
FUNCTIONS=[{"ID":"", "desc":"",
    "arabic":"",
    "minterms":[],
    "logigram":"",
},
]
import itertools
     
class bool_quiz:
    def __init__(self):
        
        self.variables = ["A", "B","C", "D"]
        # ~ self.variables = ["A", "B","C", "D"]
        self.vars_outputs = ["S0","S1", "S2","S3", "S4", "S5", "S6", "S7", "S8", "S9","S10"]
        self.format = "latex"
        
    def set_vars(self, entries=[], outputs=["F"]):
        """ Set variable names instead of ABCD,
        """
        self.variables = entries
        self.vars_outputs = outputs

    def set_format(self, outformat):
        """ Set output format,
        """
        self.format = outformat

        
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

    #@deprecated_func
    def truth_table2(self, minterms, latex=False, dontcares=[]): 
        """ print truth table """
        variables = self.variables
        cases = itertools.product([0,1],[0,1],[0,1],[0,1])
        text = "N°\t" # line number
        text = "\t".join(variables)
        text = "\t"+ self.vars_outputs[0]
        
        
        
        tex = """%%\\begin{table}
        \\begin{tabular}{|c|c|c|c|c||c|}
    \\toprule
        """
        tex += "N° & " # line number
        tex += " & ".join(variables) 
        tex += " & "+self.vars_outputs[0]
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
            

    # deprecated
    def multiple_truth_table2(self, minterms_list, latex=False, dontcares_list=[]): 
        """ print truth table """
        
        outputs_len= len(minterms_list)
        cases = itertools.product([0,1],[0,1],[0,1],[0,1])
        text = "N°\t"  # line number
        text = "\t".join(self.variables + self.vars_outputs[:outputs_len])
        tex = """%%\\begin{table}\n
        \\begin{tabular}{|c|c|c|c|c||%s}\n
    \\toprule\n
        """%("c|"*outputs_len)
        tex += "N° &"  # line number
        tex += " & ".join(self.variables+self.vars_outputs[:outputs_len]) 
        tex += "\\\\ \\midrule\n"
           
        for counter, item in enumerate(cases):
            case = [counter] + list(item)          

            for minterms, dontcares in zip(minterms_list, dontcares_list) :
                if counter in minterms:
                    f = 1
                elif counter in dontcares:
                    f = "X"
                else:
                    f = 0
                case.append(f)
            if counter  and counter %4 == 0 :
                tex += "\\midrule\n"
            text += "\t".join([str(x) for x in case]) +"\n"
            tex += " & ".join([str(x) for x in case]) + "\\\\\n"

        tex += """\\bottomrule\n
        \\end{tabular}\n
        %%\\end{table}\n
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
        if mode: # Sum of product
            var_op = "."
            term_op = "+"
        else: # Prodect of sum
            var_op = "+"
            term_op = "."
        
        # treat as SOP
        # ajust terms and order them"""

        terms = s.split(term_op)
        # ~ print(terms)
        tmp = []
        for term in terms:
            # remove parenthesis
            # ~ if mode:
            term = term.replace('(','')
            term = term.replace(')','')
            varbs = term.split(var_op)
            varbs.sort()
            if mode:
                term = " %s "%var_op.join(varbs)
            else:
                term = "(%s)"%var_op.join(varbs)                
            tmp.append(term)
        return term_op.join(tmp)


    def simplify(self, minterms, dontcares=[]):
       
        # ~ var_names  = "a b c d"
        var_names  = " ".join(self.variables).lower()
        
        a,b,c,d = symbols(var_names)
        sop = sympy.SOPform([a,b,c,d], minterms, dontcares)
        pos = sympy.POSform([a,b,c,d], minterms, dontcares)
        
        sop = self.normalize(sop)
        pos = self.normalize(pos, False)
        return sop, pos
        

    # deprectaed
    def simplify_map2(self, minterms, dontcares=[]):
       
        var_names  = "a b c d"
        # ~ var_names  = " ".join(self.variables).lower()
        
        a,b,c,d = symbols(var_names)
        sop = sympy.SOPform([a,b,c,d], minterms, dontcares)
        pos = sympy.POSform([a,b,c,d], minterms, dontcares)
        
        sop = self.normalize(sop)
        pos = self.normalize(pos,False)
        terms = [t.strip() for t in sop.split(" + ")]

        simpls = []
        for term in terms:
            simpls.append(bool_const.REDUCTION_TABLE.get(term, ""))
      

        return "\n".join(simpls)
        
    def simplify_map(self, minterms, dontcares=[], method="sop"):
       
        var_names  = "a b c d"
        # ~ var_names  = " ".join(self.variables).lower()
        
        a,b,c,d = symbols(var_names)
        sop = sympy.SOPform([a,b,c,d], minterms, dontcares)
        pos = sympy.POSform([a,b,c,d], minterms, dontcares)
        
        sop = self.normalize(sop)
        pos = self.normalize(pos,False)
        if method.lower() in ("pos", "nor", "or"):
            terms = [t.strip() for t in pos.split(".")]
        else:
            terms = [t.strip() for t in sop.split(" + ")]            
            
        return terms

    def add_bar(self, var):
        """
        """
     
        if self.format == "latex":
            return ("\\bar "+var)
        else:
            return var +"'"

    def minterm(self, n):
        """ return a minterm for integer"""
        return bool_const.MINTERMS_TABLE.get(n,"")        
        term =[]
        for var in 'dcba':
            v = var if n % 2 ==1 else var +"'"
            n = n // 2
            term.append(v)
        term.sort()
        return ".".join(term)
    
    def maxterm(self, n):
        return bool_const.MAXTERMS_TABLE.get(n,"")
        term =[]         
        """ return a minterm for integer"""
        for var in 'dcba':
            v = var if n % 2 ==0 else var +"'"
            n = n // 2
            term.append(v)
        term.sort()
        return "(%s)"%("+".join(term))
        
    def maxterm_str(self, n):
        term =[]         
        """ return a minterm for integer"""
        myterm = bool_const.TermTables.get(n, (0,0,0,0))
        variables = self.variables[:4] # only four
        for i in range(len(variables)): 
            if myterm[i]:
                term.append(self.add_bar(variables[i]))
            else:
                term.append(variables[i])            
        return "(%s)"%("+".join(term))
        
    def minterm_str(self,n):
        term =[]         
        """ return a minterm for integer"""
        myterm = bool_const.TermTables.get(n, (0,0,0,0))
        variables = self.variables[:4] # only four
        for i in range(len(variables)):
            if myterm[i]:
                term.append(variables[i])
            else:
                term.append(self.add_bar(variables[i]))           
        return ".".join(term)
        
    def form_canonique(self, minterms, dontcares=[]):
        # ~ var_names  = "a b c d"
        var_names  = " ".join(self.variables)
        a,b,c,d = symbols(var_names)        
        # ~ a,b,c,d = symbols("a b c d")
        maxterms = [x for x in range(16) if x not in minterms and x not in dontcares]
        dnf = " + ".join([self.minterm_str(x) for x in minterms])
        cnf = " . ".join([self.maxterm_str(x) for x in range(16) if x in maxterms])
        
        return cnf, dnf
        
    def draw_map(self, minterms, dontcares=[], latex=False, correct = False):
        kmap=[]
        maxterms = [x for x in range(16) if x not in minterms and x not in dontcares]
        for x in range(16):
            if x  in minterms:
                kmap.append("1")
            elif x in dontcares:
                kmap.append("x")
            else:
                kmap.append("0")
        # ~ var_names  = "ab\\cd"
        var_names  = "".join(self.variables[:2])+"\\"+ "".join(self.variables[2:])
        table = [ [var_names,  "00","01", "11","10"],
        ["00", kmap[0], kmap[1],kmap[3],kmap[2]],
        ["00", kmap[4], kmap[5],kmap[7],kmap[6]],
        ["00", kmap[12], kmap[13],kmap[15],kmap[14]],
        ["00", kmap[8], kmap[9],kmap[11],kmap[10]],
        ]
        
        # draw simplification
        simplification = ""
        if correct:
            simplification = self.simplify_map(minterms, dontcares)
        
        text = "\n".join(["\t".join(r) for r in table])
        cd = "".join(self.variables[2:])
        ab = "".join(self.variables[:2])
        tex =  """\n\n\\begin{karnaugh-map}[4][4][1][%s][%s]"""%(cd, ab)
        tex +=  """
          \\minterms{%s}
          \\maxterms{%s}
        %%\\autoterms[0]
         \\terms{%s}{X}
        %% simplification
        %s
          %%\\implicant{5}{15}
          %%\\implicantedge{8}{8}{10}{10}
          %%\\implicantedge{8}{8}{10}{10}[8,10]
        \\end{karnaugh-map}\n"""%(", ".join([str(x) for x in minterms]), 
        ", ".join([str(x) for x in maxterms]),
        ", ".join([str(x) for x in dontcares])
        , simplification)
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
        
    def normalize_nand_nor(self, exp,type_exp="sop", method="NAND"):
        """ normalize boolean string into NOR or NAND
        """
        varlist_bar = ["A'","B'", "C'", "D'"]#,  "a'","b'", "c'", "d'"]
        varlist = ["A","B", "C", "D"]#,  "a","b", "c", "d"]
        s= str(exp).upper()
        opr_sym = ""
        # used to illiustrate the expression 
        explain_str = ""
        if method.upper()=="NAND":
            opr_sym = "\\uparrow "
            s= "(%s)"%s
            if type_exp == "sop":
                #
                explain_str = "$$"+exp+"$$\n"
                explain_str += "$$\\overline{\\overline{"+exp+"}}$$\n"
                explain_str += "$$\\overline{(\\overline{"+exp.replace("+", "}).(\\overline{")+"})}$$\n"
                # replace all 'not A' by 'A NAND A'
                for var in varlist:
                    s= s.replace("\\BAR %s"%var,"(%s %s %s)"%(var.upper(),opr_sym, var.upper()))
                    s= s.replace("%s'"%var,"(%s %s %s)"%(var.upper(),opr_sym, var.upper()))
                # replace all '+' by "NAND"
                s=s.replace("+",")\\big%s("%opr_sym)
                # replace all '.' by "NAND"            
                s=s.replace(".",opr_sym)
                
                
            elif type_exp == "pos":
                # if no parenthesis in expression
                exp2 = exp
                if "(" not in exp2:
                    exp2 = "("+exp2.replace(".", ").(")+")"
                    s = exp2.upper()
                
                exp2 = exp2.replace("(", "(\\overline{\\overline{")
                exp2 = exp2.replace(")", "}})")
                explain_str = "$$"+exp+"$$\n"
                explain_str += "$$"+exp2+"$$\n"
                explain_str += "$$\\overline{\\overline{"+exp2+"}}$$\n"
             
                # replace all 'not A' by 'W'
                for var in varlist:
                    # to avoid non suitable replacement
                    tmp_var = chr(ord(var.upper())+22)
                    s= s.replace("%s'"%var, tmp_var)
                    s= s.replace("\\BAR %s"%var, tmp_var)
                    
                # replace all 'A' by 'A NAND A'
                for var in varlist:
                    s= s.replace("%s"%var,"(%s %s %s)"%(var.upper(),opr_sym, var.upper()))
                    
                # replace temp vars
                for var in varlist:
                    # to avoid non suitable replacement
                    tmp_var = chr(ord(var.upper())+22)
                    s= s.replace(tmp_var, var)

                # replace all '+' by "NAND"
                s=s.replace("+","%s"%opr_sym)
                # replace all '.' by "NAND"            
                s=s.replace(".",opr_sym)
                # duplicate s
                s = s +opr_sym + s                
        elif method.upper()=="NOR":
            opr_sym = "\\downarrow "
            s= "(%s)"%s
            if type_exp == "pos":
                #
                explain_str = "$$"+exp+"$$\n"
                explain_str += "$$\\overline{\\overline{"+exp+"}}$$\n"
                explain_str += "$$\\overline{(\\overline{"+exp.replace(".", "}+\\overline{")+"})}$$\n"
                # replace all 'not A' by 'A NOR A'
                for var in varlist:
                    s= s.replace("\\BAR %s"%var,"(%s %s %s)"%(var.upper(),opr_sym, var.upper()))
                    s= s.replace("%s'"%var,"(%s %s %s)"%(var.upper(),opr_sym, var.upper()))
                # replace all '+' by "NOR"
                s=s.replace("+",opr_sym)
                # replace all '.' by "NOR"            
                s=s.replace(".","%s"%opr_sym)
                
                
            elif type_exp == "sop":
                # if no parenthesis in expression
                exp2 = exp
                if "(" not in exp2:
                    exp2 = "("+exp2.replace("+", ")+(")+")"
                    s = exp2.upper()                
                # ~ exp2 = "("+exp.replace("+",")+(")+")"
                exp2 = exp2.replace("(", "(\\overline{\\overline{")
                # ~ exp2 = exp2.replace("(", "(\\overline{\\overline{")
                exp2 = exp2.replace(")", "}})")
                explain_str = "$$"+exp+"$$\n"                
                explain_str += "$$"+exp2+"$$\n"                
                explain_str += "$$\\overline{\\overline{"+exp2+"}}$$\n"
             
                # replace all 'not A' by 'W'
                for var in varlist:
                    # to avoid non suitable replacement
                    tmp_var = chr(ord(var.upper())+22)
                    s= s.replace("%s'"%var, tmp_var)
                    s= s.replace("\\BAR %s"%var, tmp_var)

                    
                # replace all 'A' by 'A NOR A'
                for var in varlist:
                    s= s.replace("%s"%var,"(%s %s %s)"%(var.upper(),opr_sym, var.upper()))
                    
                # replace temp vars
                for var in varlist:
                    # to avoid non suitable replacement
                    tmp_var = chr(ord(var.upper())+22)
                    s= s.replace(tmp_var, var)

                # replace all '+' by "NOR"
                s=s.replace(".","%s"%opr_sym)
                # replace all '.' by "NOR"            
                s=s.replace("+",opr_sym)
                # duplicate s
                s = s +opr_sym + s                
        # add explaination to result string 
        result = explain_str +"$$" + s +"$$"
        result = self.normalize_latex(result)  
    
        return result

    # deprecated
    def draw_logigram2(self, sop, function_name = "F"):
        """ draw a logigram """
        varnames = {
            "A":self.variables[0],
            "B":self.variables[1],
            "C":self.variables[2],
            "D":self.variables[3],
        }
        lg = logigram.logigram(varnames)
        return lg.draw_logigram(sop, function_name)
    # deprecated    
    def draw_logigram_nand_nor2(self, sop, function_name = "F", method="NAND"):
        """ draw a logigram """
        varnames = {
            "A":self.variables[0],
            "B":self.variables[1],
            "C":self.variables[2],
            "D":self.variables[3],
        }
        lg_maker = logigram.logigram(varnames)
        lggrm = lg_maker.draw_logigram(sop, function_name)
        # substitute gates into nand
        if method.upper()=="NAND":
            lggrm = lggrm.replace("[and gate US,", "[nand gate US,")
            lggrm = lggrm.replace("[or gate US,", "[nand gate US,")
            lggrm = lggrm.replace("[not gate US, draw, rotate=270]", "[nand gate US, draw, rotate=270, scale=0.5, logic gate inputs=nn]")
        elif method.upper()=="NOR":
            lggrm = lggrm.replace("[and gate US,", "[nor gate US,")
            lggrm = lggrm.replace("[or gate US,", "[nor gate US,")
            lggrm = lggrm.replace("[not gate US, draw, rotate=270]", "[nor gate US, draw, rotate=270, scale=0.5, logic gate inputs=nn]")
        if method.upper()=="NAND" or method.upper()=="NOR":
            lggrm = lggrm.replace("(notx.input)", "(notx.input 1)")
            lggrm = lggrm.replace("(noty.input)", "(noty.input 1)")
            lggrm = lggrm.replace("(notz.input)", "(notz.input 1)")
            lggrm = lggrm.replace("(notw.input)", "(notw.input 1)")
        return lggrm
    # deprecated        
    def draw_logigram_list2(self, sop_list, function_namelist = ["F",]):
        """ draw a logigram """
        varnames = {
            "A":self.variables[0],
            "B":self.variables[1],
            "C":self.variables[2],
            "D":self.variables[3],
        }
        lg = logigram.logigram(varnames)
        return lg.draw_logigram_list(sop_list, function_namelist)

def test1():
    bq = bool_quiz()
    minterms = bq.rand_funct()
    print("minterms")
    print(minterms)
    print("maxnterms")
    maxterms = [x for x in range(16) if x not in minterms]
    maxterms = list(set(range(16)) -set(minterms))
    [x for x in range(16) if x not in minterms]
    print(maxterms)
    bq.truth_table(minterms)
    sop, pos =bq.simplify(minterms)
    print("Simplified Sum of products\n", sop)
    print("Simplified Product of sums\n", pos)
    cnf, dnf =bq.form_canonique(minterms)
    print("Sum of products\n", dnf)
    print("Product of sums\n", cnf)
    print("Karnough map")
    print(bq.draw_map(minterms))
    print("Karnough map Latex")
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

    
    

