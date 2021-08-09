#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_builder.py
#  
#  Copyright 2019 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import random
from . import question
from . import boolquiz
from . import ieee754
from . import read_config
from . import test_format_factory
class test_builder:
    """ Generate the third test """
    def __init__(self, outformat="", config_file =""):
        self.qs = question.questionGenerator(latex=True)
        self.bq = boolquiz.bool_quiz()
        self.vf = ieee754.float_point()
        self.formater = test_format_factory.test_format_factory.factory(outformat)
        # if the file is not configured, use default config file
        if not config_file:
            config_file = "config/quiz.conf"
        self.config_file = config_file
        self.myconfig = read_config.read_config(config_file)
        #~ print(outformat)
        self.commands = ["float", 
         "intervalle",
         "complement",
         "exp",            
         "map",
         "map-sop",
        "function",
        "base",
        "arithm",
        "mesure",
        "static_funct", 
        "multi_funct",
        ]
        self.test_commands = {}
        self.test_commands[1] = [["base", "base", "arithm"],
        ["mesure", "base", "arithm"],
        ["base", "mesures", "arithm"],
        
        ]
        self.test_commands[2] = [["float", "map"],
        ["float", "map-sop"],
        ["float", "function"],
        ["complement","complement", "map"],
        ["function", "exp"],
        ["function", "exp"],        
        ]
        self.test_commands[3] =  [
#       ["float", "map"],
#        ["float", "map-sop"],
#        ["float", "function"],
#        ["complement","complement", "map"],
        ["function", "exp"],
        ["function", "exp"],
        ["function", "map"],
        ["function", "map"],
        ["function", "map"],
        ["function", "exp"],
        ]        
        self.test_commands[4] =  [
        ["static_funct",],
        ]        
        self.test_commands[5] =  [
        ["multi_funct",],
        ]
    def reset(self,):
        """
        reset output
        """
        self.formater.reset()
    def get_test_config(self, test_id):
        """
        return testif according to config file
        """
        return self.myconfig.get_test_config(test_id)

    def question_vf(self,):
        x = self.vf.vf_question()
        question = "Representer sous la norme IEEE-754 32 bits le nombre suivant"
        arabic = u"مثل العدد الآتي حسب المعيار IEEE-754 32 bits"
        data ="%0.3f"%x
        answer = "Representer sous la norme IEEE-754 32 bits le nombre suivant : %0.3f\n"%x
        answer += '\n\\begin{verbatim}'
        answer += self.vf.IEEE754(x, True)
        answer +='\n\\end{verbatim}'      
        return question, arabic, data, answer
        
    def question_cp(self,):
        n, a, cp1, cp2 = self.qs.comp_one(8)        

        question = u"Representer en complément à 1 et à 2 le nombre  : -%d"%n
        arabic = u"مثل  العدد الآتي في المتمم إلى الواحد وإلى الاثنين  : -%d"%n
        data = ""
        answer = u"Representer en complément à 1 et à 2 le nombre  : -%d"%n
        #~ answer += '\n\\begin{verbatim}'
        answer += self.qs.comp_one(8,n, method=True)
        #~ answer +='\n\\end{verbatim}'      
        return question, arabic, data, answer
    def question_intervalle(self,):
        
        n =self.qs.intervalle()        

        question = u"Donner les intervalles qu'on peut représenter en nombre positifs, valeur absolue, complément à 1 et complément à 2  sur %d bits\n"%n
        arabic = u"حدد المجالات التي يمكن تمثيلها لأعداد الموجبة والتمثيل بالقيمة المطلقة والمتمم إلى 1 و 2 على   : %d بت"%n
        data = ""
        answer = u"Les intervalles sur %d bits"%n
        #~ answer += '\n\\begin{verbatim}'
        answer += self.qs.intervalle(n, method=True)
        #~ answer +='\n\\end{verbatim}'      
        return question, arabic, data, answer
        
    def question_base(self,):
        
        res =self.qs.rand_numeral_system()       

        question =u"Faire les conversions suivantes: " 
        answer = res.get('reponse','')
        arabic = u"أنجز التحويلات الآتية"
        data =  res.get("question",'')
      
        return question, arabic, data, answer
    def question_arithm(self,):
        
        res =self.qs.rand_arithm()       

        question =u"Faire les opérations suivantes: " 
        answer = res.get('reponse','')
        arabic = u"أنجز العمليات الآتية: "
        data =  res.get("question",'')

        return question, arabic, data, answer
        
    def question_mesure(self,):
        
        res =self.qs.rand_arithm()       

        question =u"Faire les opérations suivantes: " 
        answer = res.get('reponse','')
        arabic = u"أنجز العمليات الآتية: "
        data =  res.get("question",'')

        return question, arabic, data, answer

    def question_map(self,):
        

        question = u"Simplifier les fonctions suivantes\n"
        arabic = u"بسّط الدوال الآتية"
        minterms_table =[] 
        data = ""   
        nb_table = 3                  
        for i in range(nb_table):
            minterms_table.append(self.bq.rand_funct())
            #~ if i  and i %2 ==0:
                #~ data+="\n\n"
            data += self.bq.draw_map(minterms_table[i], latex=True)
 

        answer = u"Simplifier les fonctions suivantes\n"

        #~ answer += '\n\\begin{verbatim}'
        for i in range(nb_table):
            answer += "table %d\n\n"%(i+1)
            sop, pos =self.bq.simplify(minterms_table[i])
            answer += self.bq.draw_map(minterms_table[i], latex=True, correct=True) 
            answer += "Simplified Sum of products : $%s$\n\n"%self.bq.normalize_latex(sop)
        #~ answer +='\n\\end{verbatim}'  
        return question, arabic, data, answer

    def question_map_for_sop(self,nb=2):
        question = u"Soit la fonction donnée par sa forme canonique, Tracer la table de karnaugh et simplifier.\n"
        arabic = u"لتكن الدالةالمعطاة بشكلها القانوني، ارسم جدول كارنو وبسطها"
        minterms_table =[] 
        data = ""                     
        for i in range(nb):
            minterms_table.append(self.bq.rand_funct())
            cnf, dnf = self.bq.form_canonique(minterms_table[i])    
            data += "F%d(a, b, c, d) = $%s$\n\n"%(i,self.bq.normalize_latex(dnf))
            data +=  "F%d(a, b, c, d) = $\\varSigma(%s)$\n\n"%(i,repr(minterms_table[i]))

        answer = u"Simplifier les fonctions suivantes\n\n"

        #~ answer += '\n\\begin{verbatim}'
        for i in range(nb):
            cnf, dnf = self.bq.form_canonique(minterms_table[i])    
            answer +=  "F%d(a, b, c, d) = $%s$\n\n"%(i,self.bq.normalize_latex(dnf))
            answer +=  "F%d(a, b, c, d) = $\\varSigma(%s)$\n\n"%(i,repr(minterms_table[i]))
            answer += self.bq.draw_map(minterms_table[i], latex=True, correct=True)           
            sop, pos =self.bq.simplify(minterms_table[i])    
            answer += "Simplified Sum of products : $%s$\n\n"%self.bq.normalize_latex(sop)
        #~ answer +='\n\\end{verbatim}'  
        return question, arabic, data, answer
        
                
    def question_funct(self,):
        

        question = u"Etudier la fonction suivante\n"
        arabic = u"ادرس الدالة الآتية"
        sop_quest, minterms =  self.bq.rand_exp()
        #~ minterms =  self.bq.rand_funct()
        
        cnf, dnf = self.bq.form_canonique(minterms)
        #~ sop_quest = dnf
        data = "f(a,b,c,d)= $%s$\n"%self.bq.normalize_latex(sop_quest)
        # answer
        answer = "f(a,b,c,d)=$%s$\n"%self.bq.normalize_latex(sop_quest)
        answer += "f(a,b,c,D)=$ \sum %s $ \n"%self.bq.normalize_latex(sop_quest).strip()
        answer +="\n"
        answer += self.bq.truth_table(minterms, latex =True)
        sop, pos = self.bq.simplify(minterms)
        answer += "\nSum of products \n f(a,b,c,d) = $%s$\n"%self.bq.normalize_latex(dnf)
        answer +="\nProduct of sums \n f(a,b,c,d) = $%s$\n"%self.bq.normalize_latex(cnf)
        answer +="\nKarnough map\n"
        answer += self.bq.draw_map(minterms, latex=True, correct=True)
        answer +="\n\n"
        answer += "Simplified Sum of products: $%s$\n"%self.bq.normalize_latex(sop)
        answer += "\nSimplified Product of sums: $%s$\n"%self.bq.normalize_latex(pos)

        answer += """\paragraph{Logigramme} de la fonction\\\\
        %%\missingfigure[figwidth=6cm]{Logigramme}\n\n"""
        
        answer += self.bq.draw_logigram(sop)
        return question, arabic, data, answer
        
    def question_static_funct(self, minterms):
        question = u""
        arabic = u""
        # prepare minterms
        # ~ minterms = minterms.split(',')
        # ~ minterms = [int(m) for m in minterms] 
               
        cnf, dnf = self.bq.form_canonique(minterms)
        data = "f(a,b,c,d)= $%s$\n"%minterms
        # answer
        answer = "f(a,b,c,d)=$%s$\n"%str(minterms)
        answer += "f(a,b,c,D)=$ \sum %s $ \n"%str(minterms)
        answer +="\n"
        answer += self.bq.truth_table(minterms, latex =True)
        sop, pos = self.bq.simplify(minterms)
        answer += "\nSum of products \n f(a,b,c,d) = $%s$\n"%self.bq.normalize_latex(dnf)
        answer +="\nProduct of sums \n f(a,b,c,d) = $%s$\n"%self.bq.normalize_latex(cnf)
        answer +="\n\\paragraph{Karnough map}\n"
        answer += self.bq.draw_map(minterms, latex=True, correct=True)
        answer +="\n\n"
        answer += "Simplified Sum of products: $%s$\n"%self.bq.normalize_latex(sop)
        answer += "\nSimplified Product of sums: $%s$\n"%self.bq.normalize_latex(pos)

        answer += """\paragraph{Logigramme} de la fonction\\\\
        %%\missingfigure[figwidth=6cm]{Logigramme}\n\n"""
        
        answer += self.bq.draw_logigram(sop)
        return question, arabic, data, answer        

    def question_multi_funct(self, minterms_list):
        question = u""
        arabic = u""
        answer = ""
        data   = ""
        # prepare minterms
        # ~ minterms_list = minterms_list.split(':')
        # ~ funct_list = []
        # ~ for one_funct in minterms_list:
            # ~ minterms = [int(m) for m in one_funct.split(",")]
            # ~ funct_list.append(minterms)
        funct_list = minterms_list    
        # step 1 draw truth table
        for i, minterms in enumerate(funct_list):
            data += "f%d(a,b,c,d)= $%s$\n\n"%(i, minterms)
        answer += self.bq.multiple_truth_table(funct_list, latex =True)
        for i, minterms in enumerate(funct_list):            
            # answer
            cnf, dnf = self.bq.form_canonique(minterms)            
            answer += "f%d(a,b,c,d)=$%s$\n\n"%(i, str(minterms))
            answer += "f%d(a,b,c,D)=$ \sum %s $ \n"%(i, str(minterms))
            answer +="\n"
            answer += "\nSum of products \n f%d(a,b,c,d) = $%s$\n"%(i,self.bq.normalize_latex(dnf))
            answer +="\nProduct of sums \n f%d(a,b,c,d) = $%s$\n"%(i, self.bq.normalize_latex(cnf))
        
        
        for i, minterms in enumerate(funct_list):
            answer +="\n\\paragraph{Karnough map}\n"
            answer += self.bq.draw_map(minterms, latex=True, correct=True)
            sop, pos = self.bq.simplify(minterms)
            answer +="\n\n"
            answer += "Simplified Sum of products f%d : $%s$\n"%(i,self.bq.normalize_latex(sop))
            answer += "\nSimplified Product of sums f%d: $%s$\n"%(i, self.bq.normalize_latex(pos))
        for i, minterms in enumerate(funct_list):
            answer += """\paragraph{Logigramme} de la fonction\\\\
            %%\missingfigure[figwidth=6cm]{Logigramme}\n\n"""
            sop, pos = self.bq.simplify(minterms)            
            answer += self.bq.draw_logigram(sop, function_name="F%d"%i)
        
        return question, arabic, data, answer        
    def question_exp(self,):
        

        question = u"Simplifier l'expression suivante par les proprietés algébreiques \n"
        arabic = u"بسط العبارة الآتية بالخواص الجبرية"
        sop_quest, minterms = self.bq.rand_exp(4)

        data = "S = $%s$\n"%self.bq.normalize_latex(sop_quest)        
        # answer
        sop_rep, _ = self.bq.simplify(minterms)

        # answer
        answer = "Simplifier l'expression suivante\n\n"
        answer += "S = $%s$\n\n"%self.bq.normalize_latex(sop_quest)
        answer += " = $%s$\n\n"%self.bq.normalize_latex(sop_rep)

        answer +="\nKarnough map\n"
        answer += self.bq.draw_map(minterms, latex=True, correct=True)
        answer +="\n\n"
        return question, arabic, data, answer
        

    def get_question(self, command, args={}):
        """
        return question from command
        """
        if command == "float":
            return self.question_vf()
        elif command == "intervalle":
            return self.question_intervalle()
        elif command == "complement":
            return self.question_cp()
        elif command == "exp":
            return self.question_exp()
        elif command == "map":

            return self.question_map()
        elif command == "map-sop":

            return self.question_map_for_sop()
        elif command == "function":

            return self.question_funct()
        elif command == "base":
            return self.question_base()

        elif command == "mesure":
            return self.question_mesure()

        elif command == "arithm":
            return self.question_arithm()
        elif command == "static_funct":
            return self.question_static_funct(args["minterms"][0])
        elif command == "multi_funct":
            return self.question_multi_funct(args["minterms"])
        else:
            return "Question Error: %s"%command.replace('_',''), "Arabic", "Data", "Answer"
            
    def test(self, questions_names, rand=True, nb=2, repeat=2, args={}):
        """ generate a test"""
        if rand:
            questions_names = random.sample(questions_names, nb)
        # generate question from  command
        questions = [self.get_question(q, args=args) for q in questions_names]
        for i in range(repeat):
            for cpt, value in enumerate(questions):
                q, ar, data, an = value
                q_no = "Q%d"%(cpt+1)
                self.formater.add_section(q_no,level=4)
                self.formater.add_text(q,ar)
                self.formater.add_text(data)
            self.formater.add_hrule()
        self.formater.add_newpage()
        self.formater.add_section("Correction",level=2)
        
        for cpt, value in enumerate(questions):
            q, ar, data, ans = value
            q_no = "Q%d"%(cpt+1)
            self.formater.add_section(q_no,level=4)
            self.formater.add_text(ans)

    
    def list_commands(self,):
        """ list all existing question types """
        return self.commands

    def get_test(self,test_no="test1"):
        randq = False
        # ~ if not args:
            # ~ args ={"minterms":[1,2,3]}
        repeat = self.myconfig.repeat
        args ={"minterms":self.myconfig.minterms}
        # ~ test_config = self.test_commands.get(test_no,[])
        # ~ test_config = self.get_test_config("test%d"%test_no)
        test_config = self.get_test_config(test_no)
        for test in test_config:
            self.formater.add_section("Question", level=1)
            self.test(test, rand=randq, repeat=repeat, args=args)        
            self.formater.add_newpage()
        return self.formater.display()



def main(args):
    builder = test_builder()
    args ={"minterms":[1,2,3]}
    test = builder.get_test(4,repeat=1, args=args)
    print(test)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
