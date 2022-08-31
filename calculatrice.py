
import tkinter as tk
import math
#definition des diiférents paramètres pris par les boutons couleurs ecriture
largeur=('black')
font_E=("Arial",12)
blanc="#E1E1E1"
default=("Arial",20)
  
off_white="#E1E1E1"
gris_clair="#E1E1E1"
color_label="#000000"
bleu="#00ffdd"
#initiliasatin de la class 
class calculator:
    def __init__ (self):
        self.ecran=tk.Tk()
        self.ecran.geometry("400x600")
        self.ecran.resizable(0,0)
        self.ecran.title("calculator")
        self.total_expression="0"
        self.current_expression="0"
        self.display_frame=self.create_display_frame()
        self.total_label,self.label=self.create_display_labels()
        self.digits ={7:(1,1),8:(1,2),9:(1,3),
                      4:(2,1),5:(2,2),6:(2,3),
                      1:(3,1),2:(3,2),3:(3,3),
                      0:(4,2),".":(4,1)}
        self.operations={"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}
        self.buttons_frame=self.create_buttons_frame()
 
        
        self.buttons_frame.rowconfigure(0,weight=0)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
#Cette fonction permet d'affichier les boutons
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_log10_button()
        self.create_ln_button()
        self.create_e_button()
        self.create_sin_button()
        self.create_tan_button()
        self.create_cos_button()
        self.create_bin_button()
        self.create_oct_button()
        self.create_hex_button()
        self.create_fact_button()
        
    
#cette fonction sert juste pour le design des diiférentes touches

    def create_display_labels(self):
        total_label=tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,bg=gris_clair,fg=color_label,padx=40,font=font_E)
        total_label.pack(expand=True,fill='both')
        label=tk.Label(self.display_frame,text=self.current_expression,anchor=tk.E,bg=gris_clair,fg=color_label,padx=40,font=largeur)
        label.pack(expand=True,fill='both')
        return total_label,label



    def create_display_frame(self):
       frame=tk.Frame(self.ecran,height=221,bg=gris_clair)
       frame.pack(expand=True,fill="both")
       return frame

    def add_to_expression(self,value):
        self.current_expression +=str(value)
        self.update_label()




    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.buttons_frame,text=str(digit),bg=blanc,fg=largeur,borderwidth=0,
            command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)


    def append_operator(self,operator):
        self.current_expression +=operator
        self.total_expression=self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()
        




    def create_operator_buttons(self):
        i=0
        for operator,symbol in self.operations.items():
            button=tk.Button(self.buttons_frame, text=symbol,bg=off_white,fg=color_label,font=default,borderwidth=0,
            command=lambda x=operator:self.append_operator(x))
            button.grid(row=i,column=4, sticky=tk.NSEW)
            i +=1

    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_label()
        self.update_total_label()



    def create_clear_button(self):
        button=tk.Button(self.buttons_frame, text="C",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.clear)
        button.grid(row=0,column=1,sticky=tk.NSEW)

    def Square(self):
        self.current_expression=str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button=tk.Button(self.buttons_frame, text="x\u00b2",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.Square)
        button.grid(row=0,column=2,sticky=tk.NSEW)


    def Sqrt(self):
        self.current_expression=math.cos(str(eval(f"{self.current_expression}**0.5 ")))
        self.update_label()

    def create_sqrt_button(self):
        button=tk.Button(self.buttons_frame, text="\u221ax",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.Sqrt)
        button.grid(row=0,column=3,sticky=tk.NSEW)

    def cosinus(self):
        self.current_expression=math.cos(math.radians(float(eval(f"{self.current_expression}"))))
        self.update_label()

    def cosinus(self):
        self.current_expression=math.cos(math.radians(float(eval(f"{self.current_expression}"))))
        self.update_label()

    def sinus(self):
        self.current_expression=math.sin(math.radians(float(eval(f"{self.current_expression}"))))
        self.update_label()

    def tangente(self):
        self.current_expression=math.tan(math.radians(float(eval(f"{self.current_expression}"))))
        self.update_label()

    def expo(self):
        self.current_expression=math.exp(float(eval(f"{self.current_expression}")))
        self.update_label()
 
    def logn(self):
        self.current_expression=math.log(float(eval(f"{self.current_expression}")))
        self.update_label()

    def logn10(self):
        self.current_expression=math.log(float(eval(f"{self.current_expression}")))
        self.update_label()

    def bbin(self):
        while True:
            n=int(self.current_expression)
            L=[]
            quot=1
            while quot !=0:
                rest=n%2
                L.append(str(rest))
                quot=n//2
                n=quot
            return("".join(reversed(L)))
        self.update_label()

    def hhex(self):
        while True:
            n=int(self.current_expression)
            L=[]
            quot=1
            while quot !=0:
                rest=n%16
                if 10<=rest<=15:
                    rest=chr(65+(rest%10))
                    L.append(rest)
                else:
                    L.append(str(rest))
                quot=n//16
                n=quot
            return("".join(reversed(L)))
        self.update_label()


    def ooct(self):
        while True:
            n=int(self.current_expression)
            L=[]
            quot=1
            while quot !=0:
                rest=n%8
                L.append(str(rest))
                quot=n//8
                n=quot
            return("".join(reversed(L)))
        self.update_label()

    def ffact(self):
        f=1
        n=int(self.current_expression)
        i=1
        while(i<=n):
            f=f*i
            i=i+1
        return (f)
      



    def bin(self):
       self.current_expression=self.bbin()
       self.update_label()

    def oct(self):
       self.current_expression=self.ooct()
       self.update_label()

    def hex(self):
       self.current_expression=self.hhex()
       self.update_label()

    def fact(self):
        self.current_expression=self.ffact()
        self.update_label()


    


    def create_cos_button(self):
        button=tk.Button(self.buttons_frame, text="cos",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.cosinus)
        button.grid(row=0,column=0,sticky=tk.NSEW)

   

    def create_sin_button(self):
        button=tk.Button(self.buttons_frame, text="sin",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.sinus)
        button.grid(row=1,column=0,sticky=tk.NSEW)
    
    


    def create_tan_button(self):
        button=tk.Button(self.buttons_frame, text="tan",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.tangente)
        button.grid(row=2,column=0,sticky=tk.NSEW)


    def create_ln_button(self):
        button=tk.Button(self.buttons_frame, text="ln",bg=off_white,fg=color_label,font=default,borderwidth=0,padx=20,
        command=self.logn)
        button.grid(row=0,column=6,rowspan=5,sticky=tk.NSEW)

    def create_fact_button(self):
        button=tk.Button(self.buttons_frame, text="n!",bg=off_white,fg=color_label,font=default,borderwidth=0,padx=20,
        command=self.fact)
        button.grid(row=0,column=4,columnspan=2,sticky=tk.NSEW)

   

    def create_e_button(self):
        button=tk.Button(self.buttons_frame, text="e",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.expo)
        button.grid(row=4,column=0,sticky=tk.NSEW)


    def create_log10_button(self):
        button=tk.Button(self.buttons_frame, text="log",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.logn10)
        button.grid(row=3,column=0,sticky=tk.NSEW)

    def create_hex_button(self):
        button=tk.Button(self.buttons_frame, text="hex",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.hex)
        button.grid(row=2,column=5,sticky=tk.NSEW)
    
    def create_oct_button(self):
        button=tk.Button(self.buttons_frame, text="oct",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.oct)
        button.grid(row=1,column=5,sticky=tk.NSEW)
    
    
    def create_bin_button(self):
        button=tk.Button(self.buttons_frame, text="bin",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.bin)
        button.grid(row=3,column=5,sticky=tk.NSEW)
    
  




    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression= str(eval(self.total_expression))
            self.total_expression=""
        except Exception as e:
            self.current_expression="Error"
        finally:
            self.update_label()
     


    def create_equals_button(self):
        button=tk.Button(self.buttons_frame, text="=",bg=off_white,fg=color_label,font=default,borderwidth=0,
        command=self.evaluate)
        button.grid(row=4,column=3,columnspan=4,sticky=tk.NSEW)




    def create_buttons_frame(self):
        frame=tk.Frame(self.ecran)
        frame.pack(expand=True,fill="both")
        return frame


    def update_total_label(self):
        expression=self.total_expression
        for operator,symbol in self.operations.items():
            expression=expression.replace(operator,f'{symbol}')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

        



    def run(self):
        self.ecran.mainloop()


if __name__ =="__main__":
    calc=calculator()
    calc.run()




