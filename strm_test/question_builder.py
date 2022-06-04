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
from .codage import question_codage as question
from .bool import boolquiz
from .codage import ieee754
from .display import test_format_factory
from .sequentiel import tex_chronograms

class Question_Builder:
    """ Generate the question """
    def __init__(self, outformat="", config_file =""):
        self.qs = question.questionGenerator(latex=True)
        self.bq = boolquiz.bool_quiz()
        self.vf = ieee754.float_point()
        self.formater = test_format_factory.test_format_factory.factory(outformat)
        self.answer_formater = test_format_factory.test_format_factory.factory(outformat)

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
        answer += self.qs.comp_one(8,n, method=True)
        return question, arabic, data, answer
        
    def question_intervalle(self,):
        
        n =self.qs.intervalle()        

        question = u"Donner les intervalles qu'on peut représenter en nombre positifs, valeur absolue, complément à 1 et complément à 2  sur %d bits\n"%n
        arabic = u"حدد المجالات التي يمكن تمثيلها لأعداد الموجبة والتمثيل بالقيمة المطلقة والمتمم إلى 1 و 2 على   : %d بت"%n
        data = ""
        answer = u"Les intervalles sur %d bits"%n
        answer += self.qs.intervalle(n, method=True)
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
            # ~ data += self.bq.draw_map(minterms_table[i], latex=True)
            data += self.formater.draw_map(minterms_table[i], dontcares=[],
                    variables = self.bq.variables)            
 

        answer = u"Simplifier les fonctions suivantes\n"

        for i in range(nb_table):
            answer += "table %d\n\n"%(i+1)
            sop, pos =self.bq.simplify(minterms_table[i])
            # ~ answer += self.bq.draw_map(minterms_table[i], latex=True, correct=True)
            simply_terms= self.bq.simplify_map(minterms_table[i])
            answer += self.formater.draw_map(minterms_table[i], 
                       variables = self.bq.variables,
                       correct=True,
                       simply_terms=simply_terms) 
            
            answer += "Simplified Sum of products : $%s$\n\n"%self.formater.normalize_formula(sop)

        return question, arabic, data, answer

    def question_map_for_sop(self,nb=2):
        question = u"Soit la fonction donnée par sa forme canonique, Tracer la table de karnaugh et simplifier.\n"
        arabic = u"لتكن الدالةالمعطاة بشكلها القانوني، ارسم جدول كارنو وبسطها"
        minterms_table =[] 
        data = ""                     
        for i in range(nb):
            minterms_table.append(self.bq.rand_funct())
            cnf, dnf = self.bq.form_canonique(minterms_table[i])    
            data += "F%d(a, b, c, d) = $%s$\n\n"%(i,self.formater.normalize_formula(dnf))
            data +=  "F%d(a, b, c, d) = $\\varSigma(%s)$\n\n"%(i,repr(minterms_table[i]))

        answer = u"Simplifier les fonctions suivantes\n\n"

        for i in range(nb):
            cnf, dnf = self.bq.form_canonique(minterms_table[i])    
            answer +=  "F%d(a, b, c, d) = $%s$\n\n"%(i,self.formater.normalize_formula(dnf))
            answer +=  "F%d(a, b, c, d) = $\\varSigma(%s)$\n\n"%(i,repr(minterms_table[i]))
            # ~ answer += self.bq.draw_map(minterms_table[i], latex=True, correct=True)
            simply_terms= self.bq.simplify_map(minterms_table[i])
            answer += self.formater.draw_map(minterms_table[i], correct=True,
                       variables = self.bq.variables,
                       simply_terms = simply_terms) 
            sop, pos =self.bq.simplify(minterms_table[i])    
            answer += "Simplified Sum of products : $%s$\n\n"%self.formater.normalize_formula(sop)

        return question, arabic, data, answer
        
                
    def question_funct(self,):
        

        question = u"Etudier la fonction suivante\n"
        arabic = u"ادرس الدالة الآتية"
        sop_quest, minterms =  self.bq.rand_exp()
        #~ minterms =  self.bq.rand_funct()
        
        cnf, dnf = self.bq.form_canonique(minterms)
        #~ sop_quest = dnf
        data = "f(a,b,c,d)= $%s$\n"%self.formater.normalize_formula(sop_quest)
        # answer
        answer_formater = self.answer_formater
        answer_formater.reset()
        answer = "f(a,b,c,d)=$%s$\n"%self.formater.normalize_formula(sop_quest)
        answer += "f(a,b,c,D)=$ \sum %s $ \n"%self.formater.normalize_formula(sop_quest).strip()
        answer +="\n"
        # ~ answer += self.bq.truth_table(minterms, latex =True)
        answer += self.formater.truth_table(minterms, dontcares=[], variables=self.bq.variables, vars_outputs=self.bq.vars_outputs )
        sop, pos = self.bq.simplify(minterms)
        answer += "\nSum of products \n f(a,b,c,d) = $%s$\n"%self.formater.normalize_formula(dnf)
        answer +="\nProduct of sums \n f(a,b,c,d) = $%s$\n"%self.formater.normalize_formula(cnf)
        answer +="\nKarnough map\n"
        # ~ answer += self.bq.draw_map(minterms, latex=True, correct=True)
        simply_terms= self.bq.simplify_map(minterms)
        answer += self.formater.draw_map(minterms,  correct = True,
                variables = self.bq.variables,
                simply_terms= simply_terms)        
        answer +="\n\n"
        answer += "Simplified Sum of products: $%s$\n"%self.formater.normalize_formula(sop)
        answer += "\nSimplified Product of sums: $%s$\n"%self.formater.normalize_formula(pos)

        answer += """\paragraph{Logigramme} de la fonction\\\\
        %%\missingfigure[figwidth=6cm]{Logigramme}\n\n"""
        
        # ~ answer += self.bq.draw_logigram(sop)
        answer += self.formater.draw_logigram(sop, function_name='F',
           variables = self.bq.variables)
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
        sop, pos = self.bq.simplify(minterms, dont_care )        
        simply_terms= self.bq.simplify_map(minterms, dont_care)        
        # answer
        answer_items = [fname + " =$%s$\n"%str(minterms)
        , fname + " =$ \sum %s $ \n"%str(minterms)
        ,"\n"
        # ~ , self.bq.truth_table(minterms, latex =True)
        ,self.formater.truth_table(minterms, dontcares=dont_care, variables=var_names, vars_outputs=output_names )        

        , "\nSum of products \n "+fname + " = $%s$\n"%self.formater.normalize_formula(dnf)
        ,"\nProduct of sums \n "+fname + " = $%s$\n"%self.formater.normalize_formula(cnf)
        , self.formater.add_section("Karnough map", level=4) +"\n"
        # ~ , self.bq.draw_map(minterms, latex=True, correct=True, dontcares=dont_care)
        # ~ , self.bq.draw_map(minterms, latex=True, correct=True, dontcares=dont_care)
        , self.formater.draw_map(minterms, dontcares=dont_care, correct = True,
                variables = self.bq.variables,
                simply_terms= simply_terms)
        ,"\n\n"
        , "Simplified Sum of products: $%s$\n"%self.formater.normalize_formula(sop)
        , "\nSimplified Product of sums: $%s$\n"%self.formater.normalize_formula(pos)
        , self.formater.add_section("Logigramme de la fonction",  level=4)
        # ~ , self.bq.draw_logigram(sop, function_name=output_names[0])
        , self.formater.draw_logigram(sop, function_name=output_names[0], variables=var_names)

        ]
        answer  = "\nataha".join(answer_items)
        return question, arabic, data, answer 
               
    def question_static_nand_exp(self, minterms, var_names=["A","B","C","D"], output_names=["S0","S1","S2","S3"], dont_care=[] , method="nand"):
        question = u""
        arabic = u""
        # change vars names
        self.bq.set_vars(var_names, output_names)
        fname = output_names[0]+"(%s)"%(', '.join(var_names))

        cnf, dnf = self.bq.form_canonique(minterms)
        data = fname + " = $%s$\n"%(minterms)
        sop, pos = self.bq.simplify(minterms, dont_care )
        simply_terms= self.bq.simplify_map(minterms, dont_care)
        # answer
        answer_items = [fname + " =$%s$\n"%str(minterms)
        , fname + " =$ \sum %s $ \n"%str(minterms)
        ,"\n"
        # ~ , self.bq.truth_table(minterms, latex =True)

        , "\nSum of products \n "+fname + " = $%s$\n"%self.formater.normalize_formula(dnf)
        ,"\nProduct of sums \n "+fname + " = $%s$\n"%self.formater.normalize_formula(cnf)
        ,self.formater.add_section("Karnough map", level=4)
        # ~ , self.bq.draw_map(minterms, latex=True, correct=True)

        , self.formater.draw_map(minterms, dontcares=dont_care, correct = True,
                variables = self.bq.variables,
                simply_terms= simply_terms)        
        ,"\n\n"
        , "Simplified Sum of products: $%s$\n"%self.formater.normalize_formula(sop)
        , "\nSimplified Product of sums: $%s$\n"%self.formater.normalize_formula(pos)
        # Generate NAND or NOR form
        , "\n%s"%method.upper() 
        , " first simplified from: %s\n"%self.bq.normalize_nand_nor(sop,"sop", method)
        , "\n%s"%method.upper()
        , " second simplified from: %s\n"%self.bq.normalize_nand_nor(pos, "pos", method)
        , "\n%s"%method.upper() 
        , " first from: %s\n"%self.bq.normalize_nand_nor(dnf,"sop", method)
        , "\n%s"%method.upper()
        , " second from: %s\n"%self.bq.normalize_nand_nor(cnf, "pos", method)

        , self.formater.add_section("Logigramme de la fonction", level=4)

        
        # ~ , self.bq.draw_logigram_nand_nor(sop, function_name=output_names[0], method=method)
        , self.formater.draw_logigram_nand_nor(sop, function_name=output_names[0],
            method=method, variables = var_names)
        ]
        answer = "\n".join(answer_items)
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
            
        answer += self.formater.open_enumerate()
        # definition des entrées sorties
        answer += """ \\item Définition des entrées et des sorties \\aRL{تعريف المداخل والمخارج}\n
         \\begin{itemize}\n
         \\item Les entrées \\aRL{المداخل}:\n
         \\begin{itemize}
         """
        answer_parts = [self.formater.open_enumerate(),
        self.formater.add_item("Définition des entrées et des sorties \\aRL{تعريف المداخل والمخارج}"),
        self.formater.open_itemize(),
        self.formater.add_item("Les entrées \\aRL{المداخل}:"),
        self.formater.open_itemize(),
        ]
        for v in var_names:
            answer += "\\item %s: \qquad 'on' noté 1 \qquad 'off' noté 0\n "%v
            answer_parts.append(self.formater.add_item("%s: \qquad 'on' noté 1 \qquad 'off' noté 0\n "%v))
 
        answer += """\end{itemize}\n
          \\item  Les sorties \\aRL{المخارج}\n
          \\begin{itemize}
          """
        answer_parts.append(self.formater.close_itemize())          
        answer_parts.append(self.formater.add_item("Les sorties \\aRL{المخارج}"))  
        answer_parts.append(self.formater.open_itemize())          
        
        for v in output_names:
            answer += "\\item %s: \qquad 'on' noté 1\qquad 'off' noté  0\n"%v
            answer_parts.append(self.formater.add_item("%s: \qquad 'on' noté 1\qquad 'off' noté  0\n"%v))

        answer += """\\end{itemize}\n
         \\end{itemize}\n"""
        answer_parts.append(self.formater.close_itemize())            
        answer_parts.append(self.formater.close_itemize())            
         
        answer +="\\item Table de vérité \\aRL{جدول الحقيقة}\\\\\n" 
        answer_parts.append(self.formater.add_item("Table de vérité \\aRL{جدول الحقيقة}"))  
        # ~ answer += self.bq.multiple_truth_table(funct_list, latex =True, dontcares_list=dont_care_list)
        answer += self.formater.multiple_truth_table(funct_list, dontcares_list=dont_care_list, variables = self.bq.variables, vars_outputs= self.bq.vars_outputs)
        truth_table = self.formater.multiple_truth_table(funct_list, dontcares_list=dont_care_list, variables = self.bq.variables, vars_outputs= self.bq.vars_outputs)
        answer_parts.append(truth_table)

        
        answer +="\\item Les formes canoniques \\aRL{الأشكال القانونية}\\\\\n"   
        answer_parts.append(self.formater.add_item("Les formes canoniques \\aRL{الأشكال القانونية}"))
        
        answer =  "\n".join(answer_parts)
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
            "dnf": "$\sum %s$"%(self.formater.normalize_formula(dnf)),
            "cnf": "$\prod %s$"%(self.formater.normalize_formula(cnf)),
            }  



        forms_types_table = {"dnf": "La première forme canonique: \\aRL{الشكل القانوني الأول}",
        "cnf": "La deuxième forme canonique: \\aRL{الشكل القانوني الثاني}",
        "minterms": "La première forme canonique numérique; \\aRL{الشكل القانوني الرقمي الأول}",            
        "maxterms": "La deuxième forme canonique numérique;  \\aRL{الشكل القانوني الرقمي الثاني}",        
        }
        answer += "\\begin{itemize}% begin listing forms\n" 
        answer_parts.append(self.formater.open_itemize())
                
        for ftype in forms_types_table:
            answer += "\\item %s \n\n"% forms_types_table[ftype]
            answer_parts.append(self.formater.add_item("%s \n\n"% forms_types_table[ftype]))            
            answer += "\\begin{itemize}\n"  
            answer_parts.append(self.formater.open_itemize())
            for funct_id in functions_forms_table: 
                # list all functions
                fname = functions_forms_table[funct_id].get("fname", "")
                form = functions_forms_table[funct_id].get(ftype, "")
                answer+= "\\item %s = %s \n"%(fname, form)
                answer_parts.append(self.formater.add_item("%s = %s \n"%(fname, form)))
            answer += "\\end{itemize}\n" 
            answer_parts.append(self.formater.close_itemize())
        # ~ answer += "\\end{itemize}\n"                         

        answer += "\n\\end{itemize}"           # end formes canoniques    
        answer_parts.append(self.formater.close_itemize())
        answer +="\n\\item Tableaux de Karnough \hfill\\aRL{مخطط كارنوف}\n"  
        answer_parts.append(self.formater.add_item("Tableaux de Karnough \hfill\\aRL{مخطط كارنوف}"))
        answer += "\n\\begin{itemize} % begin all karnaugh \n"        # begin karnaugh
        answer_parts.append(self.formater.open_itemize())
        answer =  "\n".join(answer_parts)
        for i, minterms in enumerate(funct_list):
            answer += "\\begin{minipage}{.5\\textwidth}\n"
            answer_parts.append(self.formater.open_minipage() )
            answer +="\\item La fonction  %s \\aRL{الدالة}\n\n"%output_names[i]
            answer_parts.append(self.formater.add_item("La fonction  %s \\aRL{الدالة}\n\n"%output_names[i]))            
            # ~ answer += self.bq.draw_map(minterms, latex=True, correct=True,dontcares=dont_care_list[i])
            simply_terms= self.bq.simplify_map(minterms, dont_care_list[i])
            mapy= self.formater.draw_map(minterms, dontcares=dont_care_list[i], correct = True,
                    variables = self.bq.variables,
                    simply_terms= simply_terms) 
            answer += mapy
            answer_parts.append(mapy)            
                              
            sop, pos = self.bq.simplify(minterms, dont_care_list[i])
            functions_forms_table[i]['simplified'] = self.formater.normalize_formula(sop)
            answer +="\n\n"
            # ~ answer += "\\begin{itemize}\n"
            answer += "\\textbf{La forme simplifiée \\aRL{الشكل المبسط}} \n\n %s = $%s$\n\n"%(output_names[i],self.formater.normalize_formula(sop))
            answer_parts.append("\\textbf{La forme simplifiée \\aRL{الشكل المبسط}} \n\n %s = $%s$\n\n"%(output_names[i],self.formater.normalize_formula(sop)))
            # ~ answer += "\\item La deuxième forme simplifiée \\aRL{الشكل المبسط الثاني} \n\n%s = $%s$\n"%(output_names[i], self.formater.normalize_formula(pos))
            # ~ answer += "\n\\end{itemize}\n"
            answer += "\n\\end{minipage}\n"
           
            answer_parts.append(self.formater.close_minipage())            

            
        answer += "\n\\end{itemize} %end all karnaugh\n"        # end all karnaugh
        answer_parts.append(self.formater.close_itemize())         
       
        answer =  "\n".join(answer_parts)       
        # display all simplified as a list
        answer += " Les formes simplifiées \n"
        answer_parts.append(" Les formes simplifiées \n") 
        answer += "\\begin{itemize}\n"
        answer_parts.append(self.formater.open_itemize()) 
        for i in range(len(functions_forms_table)):
            fname = functions_forms_table[i].get('fname',"")
            simplified = functions_forms_table[i].get('simplified',"")
            answer += "\\item %s = $%s$\n\n"%(fname, simplified)
            answer_parts.append(self.formater.add_item("%s = $%s$\n\n"%(fname, simplified)))             
        answer += "\n\\end{itemize}\n"
        answer_parts.append(self.formater.close_itemize())         
        
        answer += "\\item Logigrammes \\aRL{المخططات المنطقية }\\\\"  
        answer_parts.append(self.formater.add_item("Logigrammes \\aRL{المخططات المنطقية }\\\\"))         
        
        sop_list = []       
        for i, minterms in enumerate(funct_list):
            sop, pos = self.bq.simplify(minterms, dont_care_list[i])       
            sop_list.append(sop)     

        lggm = self.formater.draw_logigram_list(sop_list, function_namelist=output_names,
             variables = var_names)
        answer += lggm
        answer += self.formater.close_enumerate() 
        answer_parts.append(lggm) 
        answer_parts.append(self.formater.close_enumerate()) 
        
        answer =  "\n".join(answer_parts)  
        return question, arabic, data, answer 
        
        
        
               
    def question_exp(self,):
        

        question = u"Simplifier l'expression suivante par les proprietés algébreiques \n"
        arabic = u"بسط العبارة الآتية بالخواص الجبرية"
        sop_quest, minterms = self.bq.rand_exp(4)

        data = "S = $%s$\n"%self.formater.normalize_formula(sop_quest)        
        # answer
        sop_rep, _ = self.bq.simplify(minterms)

        # answer
        answer = "Simplifier l'expression suivante\n\n"
        answer += "S = $%s$\n\n"%self.formater.normalize_formula(sop_quest)
        answer += " = $%s$\n\n"%self.formater.normalize_formula(sop_rep)

        answer += "\nKarnough map\n"
        # ~ answer += self.bq.draw_map(minterms, latex=True, correct=True)
        simply_terms= self.bq.simplify_map(minterms)
        answer += self.formater.draw_map(minterms, correct = True,
                variables = self.bq.variables,
                simply_terms= simply_terms)        
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





def main(args):
    builder = test_builder()
    args ={"minterms":[1,2,3]}
    test = builder.get_test(4,repeat=1, args=args)
    print(test)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))