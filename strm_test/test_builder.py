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
from . import tex_chronograms
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
        "nand_funct", 
        "nor_funct", 
        "multi_funct",
        "chronogram",
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
        ["static_funct","nand_funct"],
        ]        
        self.test_commands[5] =  [
        ["multi_funct",],
        ]
        self.test_commands[6] =  [
        ["chronogram",],
        ]
    def set_format(self, outformat="latex"):
        """ set a new format"""
        self.formater = test_format_factory.test_format_factory.factory(outformat)

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
        
    def question_static_funct(self, minterms, var_names=["A","B","C","D"], output_names=["S0","S1","S2","S3"], dont_care=[] ):
        question = u""
        arabic = u""
        # change vars names
        # prepare minterms
        # ~ minterms = minterms.split(',')
        # ~ minterms = [int(m) for m in minterms] 
        self.bq.set_vars(var_names, output_names)
        fname = output_names[0]+"(%s)"%(', '.join(var_names))

        cnf, dnf = self.bq.form_canonique(minterms)
        data = fname + " = $%s$\n"%(minterms)
        # answer
        answer = fname + " =$%s$\n"%str(minterms)
        answer += fname + " =$ \sum %s $ \n"%str(minterms)
        answer +="\n"
        answer += self.bq.truth_table(minterms, latex =True)
        sop, pos = self.bq.simplify(minterms, dont_care )
        answer += "\nSum of products \n "+fname + " = $%s$\n"%self.bq.normalize_latex(dnf)
        answer +="\nProduct of sums \n "+fname + " = $%s$\n"%self.bq.normalize_latex(cnf)
        answer +="\n\\paragraph{Karnough map}\n"
        answer += self.bq.draw_map(minterms, latex=True, correct=True, dontcares=dont_care)
        answer +="\n\n"
        answer += "Simplified Sum of products: $%s$\n"%self.bq.normalize_latex(sop)
        answer += "\nSimplified Product of sums: $%s$\n"%self.bq.normalize_latex(pos)

        answer += """\paragraph{Logigramme} de la fonction\\\\
        %%\missingfigure[figwidth=6cm]{Logigramme}\n\n"""
        
        answer += self.bq.draw_logigram(sop, function_name=output_names[0])
        return question, arabic, data, answer 
               
    def question_static_nand_exp(self, minterms, var_names=["A","B","C","D"], output_names=["S0","S1","S2","S3"], dont_care=[] , method="nand"):
        question = u""
        arabic = u""
        # change vars names
        self.bq.set_vars(var_names, output_names)
        fname = output_names[0]+"(%s)"%(', '.join(var_names))

        cnf, dnf = self.bq.form_canonique(minterms)
        data = fname + " = $%s$\n"%(minterms)
        # answer
        answer = fname + " =$%s$\n"%str(minterms)
        answer += fname + " =$ \sum %s $ \n"%str(minterms)
        answer +="\n"
        # ~ answer += self.bq.truth_table(minterms, latex =True)
        sop, pos = self.bq.simplify(minterms, dont_care )
        answer += "\nSum of products \n "+fname + " = $%s$\n"%self.bq.normalize_latex(dnf)
        answer +="\nProduct of sums \n "+fname + " = $%s$\n"%self.bq.normalize_latex(cnf)
        answer +="\n\\paragraph{Karnough map}\n"
        answer += self.bq.draw_map(minterms, latex=True, correct=True)
        answer +="\n\n"
        answer += "Simplified Sum of products: $%s$\n"%self.bq.normalize_latex(sop)
        answer += "\nSimplified Product of sums: $%s$\n"%self.bq.normalize_latex(pos)
        # Generate NAND or NOR form
        answer += "\n%s"%method.upper() 
        answer += " first simplified from: %s\n"%self.bq.normalize_nand_nor(sop,"sop", method)
        answer += "\n%s"%method.upper()
        answer += " second simplified from: %s\n"%self.bq.normalize_nand_nor(pos, "pos", method)
        answer += "\n%s"%method.upper() 
        answer += " first from: %s\n"%self.bq.normalize_nand_nor(dnf,"sop", method)
        answer += "\n%s"%method.upper()
        answer += " second from: %s\n"%self.bq.normalize_nand_nor(cnf, "pos", method)

        answer += """\paragraph{Logigramme} de la fonction\\\\
        %%\missingfigure[figwidth=6cm]{Logigramme}\n\n"""
        
        answer += self.bq.draw_logigram_nand_nor(sop, function_name=output_names[0], method=method)
        return question, arabic, data, answer        

    def question_multi_funct(self, minterms_list, var_names=["A","B","C","D"], output_names=["S0","S1","S2","S3"], dont_care_list=[]):
        question = u""
        arabic = u""
        answer = ""
        data   = ""
        sop_list= []
        # deprecated ; draw a unique logigramme
        separated_logigram = False
        # prepare minterms
        self.bq.set_vars(var_names, output_names)
           
        funct_list = minterms_list 
        # dontcare list:
        # init dontcare list with the same length of minterms_list
        if not dont_care_list:   
            dont_care_list = [[] for m in minterms_list]
        # step 1 draw truth table
        for i, minterms in enumerate(funct_list):
            data += "%s(%s)"%(output_names[i],', '.join(var_names) ) # function name and arguments
            data += "= $%s$\n\n"%(minterms)
            data += "DONT CARE= $%s$\n\n"%(dont_care_list[i])
            
        answer += "\\begin{enumerate}\n"
        # definition des entrées sorties
        answer += """ \\item Définition des entrées et des sorties \\aRL{تعريف المداخل والمخارج}\n
         \\begin{itemize}\n
         \\item Les entrées \\aRL{المداخل}:\n
         \\begin{itemize}
         """
        for v in var_names:
            answer += "\\item %s: \qquad 'on' noté 1 \qquad 'off' noté 0\n "%v
 
        answer += """\end{itemize}\n
          \\item  Les sorties \\aRL{المخارج}\n
          \\begin{itemize}
          """
        for v in output_names:
            answer += "\\item %s: \qquad 'on' noté 1\qquad 'off' noté  0\n"%v
        answer += """\\end{itemize}\n
         \\end{itemize}\n"""
         
        answer +="\\item Table de vérité \\aRL{جدول الحقيقة}\\\\\n"                        
        answer += self.bq.multiple_truth_table(funct_list, latex =True, dontcares_list=dont_care_list)

        
        answer +="\\item Les formes canoniques \\aRL{الأشكال القانونية}\\\\\n"   
        # ~ answer += "\\begin{itemize}\n"        # begin forme canoniques
        
        # ~ answer += "\\item La première forme canonique: \\aRL{الشكل القانوني الأول}\n\n"
        # ~ answer += "\\begin{itemize}\n"
        
        # tableaux dex forms canoniques
        functions_forms_table={}

        for i, minterms in enumerate(funct_list):  
            
            maxterms = [k for k in range(16) if not k in minterms and not k in dont_care_list[i]]  
      
            # answer
            cnf, dnf = self.bq.form_canonique(minterms)
            
            fname  = "%s(%s)"%(output_names[i],', '.join(var_names) ) # function name and arguments          

            functions_forms_table[i]= {"fname": fname,
            "maxterms": "$\prod %s$"%maxterms,
            "minterms": "$\sum %s$"%minterms,
            "dnf": "$\sum %s$"%(self.bq.normalize_latex(dnf)),
            "cnf": "$\prod %s$"%(self.bq.normalize_latex(cnf)),
            }  

            # ~ answer +="\\item La fonction %s \\aRL{الدالة}\\\\\n"%fname
            # ~ answer += "%%"+fname+ " =$%s$\n\n"%(str(minterms))            
            # ~ answer +="\n"

            # ~ answer += "\\begin{itemize}\n"           

            # ~ answer += "\\item La première forme canonique: \\aRL{الشكل القانوني الأول}\n\n"+fname+ " = $%s$\n"%(self.bq.normalize_latex(dnf))
            # ~ answer +="\\item La deuxième forme canonique: \\aRL{الشكل القانوني الثاني}≠\n\n "+fname+ " = $%s$\n"%(self.bq.normalize_latex(cnf))
            #answer +="\n Les formes canoniques numériques"            
            # ~ answer += "\\item La première forme canonique; \\aRL{الشكل القانوني الرقمي الأول}\n\n"+fname+ " = $\sum %s$\n"%(str(minterms))
            # ~ answer +="\\item La deuxième forme canonique;  \\aRL{الشكل القانوني الرقمي الثاني}\n\n "+fname+ " = $\prod %s$\n"%(str(maxterms))
            # ~ answer += "\\end{itemize}\n"           
        # ~ answer += "\n\\end{itemize}"           # end formes canoniques


        forms_types_table = {"dnf": "La première forme canonique: \\aRL{الشكل القانوني الأول}",
        "cnf": "La deuxième forme canonique: \\aRL{الشكل القانوني الثاني}",
        "minterms": "La première forme canonique numérique; \\aRL{الشكل القانوني الرقمي الأول}",            
        "maxterms": "La deuxième forme canonique numérique;  \\aRL{الشكل القانوني الرقمي الثاني}",        
        }
        answer += "\\begin{itemize}% begin listing forms\n"         
        for ftype in forms_types_table:
            answer += "\\item %s \n\n"% forms_types_table[ftype]
            answer += "\\begin{itemize}\n"   
            for funct_id in functions_forms_table: 
                # list all functions
                fname = functions_forms_table[funct_id].get("fname", "")
                form = functions_forms_table[funct_id].get(ftype, "")
                answer+= "\\item %s = %s \n"%(fname, form)
            answer += "\\end{itemize}\n"                         
        # ~ answer += "\\end{itemize}\n"                         

        answer += "\n\\end{itemize}"           # end formes canoniques                  
        answer +="\n\\item Tableaux de Karnough \hfill\\aRL{مخطط كارنوف}\n"  
        answer += "\n\\begin{itemize} % begin all karnaugh \n"        # begin karnaugh
        
        for i, minterms in enumerate(funct_list):
            answer += "\\begin{minipage}{.5\\textwidth}\n"
            answer +="\\item La fonction  %s \\aRL{الدالة}\n\n"%output_names[i]
            answer += self.bq.draw_map(minterms, latex=True, correct=True,dontcares=dont_care_list[i])
            sop, pos = self.bq.simplify(minterms, dont_care_list[i])
            functions_forms_table[i]['simplified'] = self.bq.normalize_latex(sop)
            answer +="\n\n"
            # ~ answer += "\\begin{itemize}\n"
            answer += "\\textbf{La forme simplifiée \\aRL{الشكل المبسط}} \n\n %s = $%s$\n\n"%(output_names[i],self.bq.normalize_latex(sop))
            # ~ answer += "\\item La deuxième forme simplifiée \\aRL{الشكل المبسط الثاني} \n\n%s = $%s$\n"%(output_names[i], self.bq.normalize_latex(pos))
            # ~ answer += "\n\\end{itemize}\n"
            answer += "\n\\end{minipage}\n"

            
        answer += "\n\\end{itemize} %end all karnaugh\n"        # end all karnaugh
       
       
        # display all simplified as a list
        answer += " Les formes simplifiées \n"
        answer += "\\begin{itemize}\n"
        for i in range(len(functions_forms_table)):
            fname = functions_forms_table[i].get('fname',"")
            simplified = functions_forms_table[i].get('simplified',"")
            answer += "\\item %s = $%s$\n\n"%(fname, simplified)
        answer += "\n\\end{itemize}\n"
        
        answer += "\\item Logigrammes \\aRL{المخططات المنطقية }\\\\"  
        
        # deprecated ; draw a unique logigramme
        if separated_logigram :
            answer += "\\begin{itemize}\n"        # begin logigram 
            sop_list = []       
            for i, minterms in enumerate(funct_list):
                answer += """\\item Logigramme de la fonction %s \\aRL{المخطط المنطقي للدالة}\\\\"""%output_names[i]
                answer += """%%\missingfigure[figwidth=6cm]{Logigramme}\n\n"""
                sop, pos = self.bq.simplify(minterms, dont_care_list[i])       
                sop_list.append(sop)     
                answer += self.bq.draw_logigram(sop, function_name=output_names[i])
                
            answer += "\\end{itemize}\n"        # end logigram fonction
        else:
            sop_list = []       
            for i, minterms in enumerate(funct_list):
                sop, pos = self.bq.simplify(minterms, dont_care_list[i])       
                sop_list.append(sop)     
        answer +="\section{Schéma globale du circuit}\n"
        answer += self.bq.draw_logigram_list(sop_list, output_names)

        answer += "\\end{enumerate}\n"        
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
        
        
    def question_chronogram(self, varlist={}, flip_type="D", length=20, synch_type="rising", output_vars=["Q",]):
        
        """
        Generate Chronogram question
        """      
        chrono = tex_chronograms.Tex_Chronograms();
        # generate random signals 
        # according to prameters
        # ~ signals = {"D":[-1, 3, -0.5, +1.5, -5, 3.5, -6.5],
                   # ~ "Q":[-1] }
        if not varlist:
            varlist = {"D":1, "R":-1, "S":-1}
        signals ={}
        for key in varlist:
            if key in output_vars:
                # add an empty signal
                signals[key] = [varlist[key],]
            else:
                signal_dict = chrono.question({key:varlist[key]}, length=length)
                signals[key] = signal_dict[key]
        # ~ signals = chrono.question(varlist, length=length)
        print("test_builder:signals", signals)
        # set synchronization type
        chrono.set_synch_type(synch_type)
        
        # generate question
        # 1- clock
        # 2- signals without solution
        clock = chrono.clock_signal(length=length, period=1)        
        tex_data_question = chrono.draw(signals, clock)        
        
        # generate soltution
        # get solution for signal
        # 2 generate chrono for answer
        # if we want to generate multiple cases using "dual" or "all"
        print("initial: ",signals)  
        if synch_type =="all" or synch_type =="dual":
            # set synchronization type
            chrono.set_synch_type("rising")
        out_signal = chrono.resolve(flip_type=flip_type,signals=signals.copy(), period=2) 
        # output signal    
        tmp_signals =    signals
        tmp_signals[output_vars[0]] = out_signal
        print("rising: ",out_signal)
        print("rising: ",signals)  
        # add more signals for multi cases
        if synch_type =="all" or synch_type =="dual":
            # set synchronization type
            chrono.set_synch_type("falling")

            out_signal = chrono.resolve(flip_type=flip_type,signals=signals.copy(), period=2) 
            print("falling: ",signals)  
            print("falling: ",out_signal)
            # output signal       
            tmp_signals[output_vars[0]+".desc"] = out_signal
        if synch_type =="all":
            # set synchronization type
            chrono.set_synch_type("asynch")
            out_signal = chrono.resolve(flip_type=flip_type,signals=signals.copy(), period=2) 
            # output signal       
            print("asynch: ",out_signal)            
            print("asynch: ",signals)            
            tmp_signals[output_vars[0]+".asyn"] = out_signal
        
        if synch_type =="all" or synch_type =="dual":
            # set synchronization type
            chrono.set_synch_type("dual")            
        
        tex_data_answer = chrono.draw(tmp_signals, clock)
            
        question =u"Compléter le chronogramme suivant:\n\n "
        arabic = u"أكمل المخطط الزمني: "
        
        # make a figure
        answer ="""Chronogramme\n\n\n
        \\scalebox{2}{ %% scale
        %s
        } %%scale\n\n"""%tex_data_answer
        
        data ="""\n\n\\scalebox{2}{ %% scale
        %s
        } %%scale \n\n"""%tex_data_question

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
        elif command == "chronogram":
            print("test_builder:debug:arguments",args)
            return self.question_chronogram(
            varlist= args.get("varlist",{}),
            flip_type=args.get("flip_type","D"),
            length=args.get("length",10),
            synch_type=args.get("synch_type","rising"),
            output_vars=args.get("output","Q")
            )
        elif command == "static_funct":
            return self.question_static_funct(args["minterms"][0],
             args["var_names"], args["output_names"]
             ,args["dontcare"][0])
        elif command == "nand_funct":
            return self.question_static_nand_exp(args["minterms"][0],
             args["var_names"], args["output_names"]
             ,args["dontcare"][0], method="nand")
        elif command == "nor_funct":
            return self.question_static_nand_exp(args["minterms"][0],
             args["var_names"], args["output_names"]
             ,args["dontcare"][0], method="nor")
        elif command == "multi_funct":
            return self.question_multi_funct(args["minterms"], 
                   args["var_names"], args["output_names"],
                   args["dontcare"])
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
        args ={"minterms":self.myconfig.minterms,
        "var_names": self.myconfig.var_names,
        "output_names": self.myconfig.output_names,
        "dontcare": self.myconfig.dontcare,
        "length":self.myconfig.length,
        "varlist":self.myconfig.varlist,
        "synch_type":self.myconfig.synch_type,
        "flip_type":self.myconfig.flip_type,
        "output":self.myconfig.output,
        }
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
