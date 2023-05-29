from tkinter import *
from tkinter import messagebox, ttk
import tempfile
import random
from time import strftime
from PIL import ImageTk, Image
import os



class Supermarche:
    def __init__(self, root):
        self.root = root
        self.root.title("MARKET TOULE")
        self.root.geometry("1100x1000")

        title = Label(self.root, text="__SUPER-MARCHE-CKDO__", font=(",",45), bg="white", fg="#21AD4D")
        title.pack(side=TOP, fill=X)

        self.c_nom = StringVar() #chaine de caractère
        self.c_phon = StringVar()
        self.n_factu = StringVar()
        z = random.randint(1000,9999)
        self.n_factu.set(z)
        self.c_email = StringVar()
        self.rech_factu = StringVar()
        self.produit = StringVar()
        self.prix = IntVar() # entier
        self.qte = IntVar()
        self.totalbrute = StringVar()
        self.taxe = StringVar()
        self.totalnet = StringVar()

        ##liste categorie

        self.list_categorie = ["Selection","Vetement","Style de vie","telephone"]

        self.list_souscategorieVetement = ["pantelon","T-shirt","Shirt"]

#souscategorievetement
        self.pantelon = ["levis","mufti","Skyar"]
        self.price_levis = 5000
        self.price_mufti = 1000
        self.price_skybar = 3000

        self.t_shirt = ["polo","Roadster","jack&jones"]
        self.price_polo = 5000
        self.price_roadster = 2500
        self.price_jack_jones = 3000


        self.shirt = ["peter England","Louis philipe","hugoBoss"]
        self.price_peter = 5900
        self.price_Louis = 6500
        self.price_Boss = 8500






#souscategorie style de vie
        self.list_souscategoriestyle = ["Bath Soap","Creme","huile cheveux"]

        self.Bath_soap = ["livebuy","lux","Santoor","pearl"]
        self.price_livebuy = 5000
        self.price_lux = 1000
        self.price_santoor = 3000
        self.price_pearl = 3000

        self.t_creme = ["faire&lovely","ponds","olay","Garnier"]
        self.price_fair = 1500
        self.price_pond = 1420
        self.price_olay = 4530
        self.price_garnier = 1250


        self.huile = ["parachute","jasmin","Bajaj"]
        self.price_parachute = 1450
        self.price_jasmin = 2300
        self.price_Bajaj = 1500

        #souscatagorie telephone

        self.list_souscategorietel = ["Iphone","Samsung","Huawei","Techno"]

        self.iphone = ["IphoneX ","Iphone11 ","Iphonemax"]
        self.price_iphone_x = 65000
        self.price_iphone_11 = 111000
        self.price_iphone_max = 1113000

        self.samsung = ["A10","S10","A80"]
        self.price_A10 = 120000
        self.price_S10 = 112500
        self.price_A80 = 123000


        self.huawei = ["huawei y95","huawei p8"," huawei Mate"]
        self.price_y95 = 89900
        self.price_p8 = 116500
        self.price_mate = 118500



        self.techno = ["techno cam11","techno cam 12 ","techno cam13"]
        self.price_com11 = 115900
        self.price_com12 = 116500
        self.price_com13 = 228500

        Main_Frame = Frame(self.root, bd=2 , relief=GROOVE,bg='white')
        Main_Frame.place(x=10 ,y=50,width=1890,height=920)

        client_Frame = LabelFrame(self.root, text="client", font=("times new roman",10),bg="white")
        client_Frame.place(x=20 ,y=65 ,width=250 ,height=150)
        self.lbl_contact = Label(client_Frame,text='contact',font=("times new roman",10,"bold"),bg="white")
        self.lbl_contact.grid(row=0,column=0,sticky=W,padx=5 ,pady=5)
        self.lbl_nomclient = Label(client_Frame, text='nom du client', font=("times new roman", 10, "bold"), bg="white")
        self.lbl_nomclient.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.lbl_email = Label(client_Frame, text='email', font=("times new roman", 10, "bold"), bg="white")
        self.lbl_email.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txt_contat = ttk.Entry(client_Frame, textvariable=self.c_phon, font=("times new roman",10))
        self.txt_contat.grid(row=0 , column=1 , sticky=W,padx=5,pady=2 )
        self.txt_nomclient = ttk.Entry(client_Frame, textvariable=self.c_nom, font=("times new roman",10))
        self.txt_nomclient.grid(row=1 , column=1 , sticky=W,padx=5,pady=2 )
        self.txt_email = ttk.Entry(client_Frame ,textvariable=self.c_email, font=("times new roman",10))
        self.txt_email.grid(row=2 , column=1 , sticky=W,padx=5,pady=2 )


        produit_frame = LabelFrame(Main_Frame, text="PRODUIT", font=("times new roman",10),bg="white")
        produit_frame.place(x=270,y=10 ,width=570 ,height=150)
        self.lbl_categori = Label(produit_frame,text='Selectioner Categorie',font=("times new roman",10,"bold"),bg="white")
        self.lbl_categori.grid(row=0,column=0,sticky=W,padx=5 ,pady=5)
        self.lbl_souscategori= Label(produit_frame,text='Sous categorie',font=("times new roman",10,"bold"),bg="white")
        self.lbl_souscategori.grid(row=1,column=0,sticky=W,padx=5 ,pady=5)
        self.lbl_nomproduit = Label(produit_frame,text='Nom du produit',font=("times new roman",10,"bold"),bg="white")
        self.lbl_nomproduit.grid(row=2,column=0,sticky=W,padx=5 ,pady=5)
        self.lbl_prix= Label(produit_frame,text='Prix',font=("times new roman",10,"bold"),bg="white")
        self.lbl_prix.grid(row=0,column=2,sticky=W,padx=5 ,pady=5)
        self.lbl_qte = Label(produit_frame,text='Quantité',font=("times new roman",10,"bold"),bg="white")
        self.lbl_qte.grid(row=1,column=2,sticky=W,padx=2 ,pady=5)
        self.txt_categorie = ttk.Combobox(produit_frame,font=("times new roman",10) ,values=self.list_categorie ,width=20,state="readonly")
        self.txt_categorie.grid(row=0 ,column=1,sticky=W,padx=2,pady=2)
        self.txt_categorie.current(0)
        self.txt_categorie.bind("<<ComboboxSelected>>",self.fonctionCategorie)
        self.txt_souscategorie = ttk.Combobox(produit_frame,font=("times new roman",10) ,values=[""],width=24,state="readonly")
        self.txt_souscategorie.grid(row=1 , column=1,sticky=W,padx=5,pady=2)
        self.txt_souscategorie.current(0)
        self.txt_souscategorie.bind("<<ComboboxSelected>>",self.fonctionsouscategorie)
        self.txt_nomproduit = ttk.Combobox(produit_frame,font=("times new roman",10), textvariable=self.produit  ,width=21,state="readonly")
        self.txt_nomproduit.grid(row=2 , column=1,sticky=W,padx=5,pady=2)
        self.txt_nomproduit.bind("<<ComboboxSelected>>",self.fonctionomproduit)
        self.txt_prix = ttk.Combobox(produit_frame,font=("times new roman",10), textvariable=self.prix ,width=20,state="readonly")
        self.txt_prix.grid(row=0 , column=3,sticky=W,padx=5,pady=2)
        self.txt_qte = ttk.Combobox(produit_frame,font=("times new roman",10), textvariable=self.qte  ,width=20,state="readonly")
        self.txt_qte.grid(row=1 , column=3,sticky=W,padx=5,pady=2)
#recherche
        recher_Frame = Frame(Main_Frame,bd=2,bg="white")
        recher_Frame.place(x=850 , y=10 ,width=300 , height=100)
#facture
        Facture_lbl = LabelFrame(Main_Frame,text="facture",font=("times new roman ",12,"bold"),bg="yellow")
        Facture_lbl.place(x=400,y=170,width=600,height=350)
        scroll_y = Scrollbar(Facture_lbl,orient=VERTICAL)
        self.textarea = Text(Facture_lbl,font=("times new roman",15,"bold"),bg="white",fg="blue")
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        self.lbl_recherche = Label(recher_Frame,text="N Facture", font=("times new roman",10,"bold"),bg="white" )
        self.lbl_recherche.grid(row=0,column=0,sticky=W, padx=5,pady=2)

        self.txt_recherche = ttk.Entry(recher_Frame,textvariable=self.rech_factu,font=("times new roman",10),width=13)
        self.txt_recherche.grid(row=2,column=0,sticky=W, padx=5,pady=2)

        self.btn_recherche = Button(recher_Frame, text="Recherche", command=self.rechercher, height=0, font=("times new roman", 12, "bold"), bg="#9CE2B2")
        self.btn_recherche.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        #enbas
        enbas_Frame = LabelFrame(Main_Frame,text="NET",font=("times new ",10,"bold"),bg="white")
        enbas_Frame.place(x=5,y=540,width=1000,height=100)
        self.lbl_totalbruite = Label(enbas_Frame,text="Total Brute",font=("times new romamn",10,"bold"),bg="white" )
        self.lbl_totalbruite.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.lbl_taxe = Label(enbas_Frame,text="Taxe",font=("times new roman",10,"bold"),bg="white")
        self.lbl_taxe.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.lbl_total = Label(enbas_Frame, text="Total Net", font=("times new roman", 10, "bold"), bg="white")
        self.lbl_total.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.lbl_total = Label(enbas_Frame, text="Total Net", font=("times new roman", 10, "bold"), bg="white")
        self.lbl_total.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.txt_totalbrute= ttk.Entry(enbas_Frame, textvariable=self.totalbrute, font=("times new roman", 10), width=15,state="readonly" )
        self.txt_totalbrute.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.txt_taxe = ttk.Entry(enbas_Frame, textvariable=self.taxe, font=("times new roman", 10),width=15, state="readonly")
        self.txt_taxe.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.txt_totalnet = ttk.Entry(enbas_Frame, textvariable=self.totalnet, font=("times new roman", 10), width=15,state="readonly")
        self.txt_totalnet.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        #image
        self.imge = ImageTk.PhotoImage(Image.open("C:/Users/DR_ANTOINE/Desktop/Gestion magasin/image/cc.jpg"))
        self.lbl_image = Label(image=self.imge)
        self.lbl_image.place(x=60,y=220,width=320,height=360)
        #bouton
        Btn_frame = Frame(enbas_Frame,bd=2, bg="white")
        Btn_frame.place(x=200,y=0)

        self.ajoutePanier =Button(Btn_frame,text="Ajouter panier ",height=3,  command= self.ajouter ,  font=("times new roman",8,"bold"),bg="#9CE2B2",width=15, cursor="hand2")
        self.ajoutePanier.grid(row=0,column=0)
        self.generer = Button(Btn_frame, text="Generé ", height=3, command=self.genererFacture,  font=("times new roman", 8, "bold"), bg="#9CE2B2", width=10, cursor="hand2")
        self.generer.grid(row=0, column=1)
        self.save = Button(Btn_frame, text=" sauvegarder Facture ", command=self.sauvegarder ,  height=3, font=("times new roman", 8, "bold"),bg="#9CE2B2", width=20, cursor="hand2")
        self.save.grid(row=0, column=2)
        self.imprime = Button(Btn_frame, text="imprimer ", command=self.imprimer, height=3, font=("times new roman", 8, "bold"), bg="#9CE2B2", width=15, cursor="hand2")
        self.imprime.grid(row=0, column=3)
        self.reini = Button(Btn_frame, text=" Renitialisé ", height=3, command=self.rein , font=("times new roman", 8, "bold"),bg="#9CE2B2", width=15, cursor="hand2")
        self.reini.grid(row=0, column=4)
        self.quite = Button(Btn_frame, text=" quitter ", height=3, font=("times new roman", 8, "bold"), bg="#9CE2B2",width=20, cursor="hand2")
        self.quite.grid(row=0, column=4)
        self.Bienvenu()
        self.l=[]

    def imprimer(self):
        fichier = tempfile.mktemp(".txt")
        open(fichier,"w").write(self.textarea.get("1.0",END))
        os.startfile(fichier,"print")

    def rein(self):
        self.textarea.delete(1.0, END)
        self.c_nom.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.n_factu.set(str(x))
        self.rech_factu.set("")
        self.produit.set("")
        self.prix.set(0)
        self.qte.set(0)
        self.l=[0]
        self.totalbrute.set("")
        self.taxe.set("")
        self.totalnet.set("")
        self.Bienvenu()
        ####Fonctions


    def Bienvenu(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END, "\t Bienvenu chez super Marché de MARKET TOULE")
        self.textarea.insert(END, f"\n\nNuméro Facture : {self.n_factu.get()}")
        self.textarea.insert(END, f"\n\nNom Client : {self.c_nom.get()}")
        self.textarea.insert(END, f"\n\nTéléphone : {self.c_phon.get()}")
        self.textarea.insert(END, f"\n\nEmail : {self.c_email.get()}")
        self.textarea.insert(END, "\n*******************************************************")
        self.textarea.insert(END, f"\nProduits\t\tQTE\t\tPrix")
        self.textarea.insert(END, "\n********************************************************")


    def rechercher(self):
        touver = "non"
        for i in os.listdir("C:/Users/DR_ANTOINE/Desktop/Gestion/magasin/facture/"):
            if i.split(".")[0]==self.rech_factu.get():
                f1 = open(f"C:/Users/DR_ANTOINE/Desktop/Gestion/ magasin/facture/{i}","r")
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                    f1.close()
                    trouver ="oui"
                if trouver=="non":
                    messagebox.showerror("erreur","la facture n'existe pas")

    def genererFacture(self):
        if self.produit.get()=="":
            messagebox.showerror("erreur","ajouter d'abor un produit")
        else:
            text= self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.Bienvenu()
            text = self.textarea.insert(END,text)
            self.textarea.insert(END,"\n******************************************************************")
            self.textarea.insert(END, f"\nTotal Bruite : \t\t\t{self.totalbrute.get()}")
            self.textarea.insert(END, f"\ntaxe : \t\t\t{self.totalbrute.get()}")
            self.textarea.insert((END,f"\nTotal Net : \t\t\t {self.totalnet.get()}"))


    def imprimer(self):
        fichier=tempfile.mktemp(".txt")
        open(fichier,"w").write(self.textarea.get("1.0",END))
        os.startfile(fichier,"print")

    def sauvegarder(self):
        op=messagebox.askyesno("sauvegarder ","Voulez vous sauvegarder la facture?")
        if op==True:
            self.donneFacture=self.textarea.get(1.0,END)
            f1=open("C:/Users/DR_ANTOINE/Desktop/Gestion magasin/facture/"+str(self.n_factu.get())+".txt","w")
            f1.write(self.donneFacture)
            messagebox.showinfo("sauvegarder",f"La facture numéro {self.n_factu.get()} a été enregistré  avec succès ")
            f1.close()


    def ajouter(self):
        self.n = self.prix.get()
        self.m = self.qte.get() * self.n
        self.l.append(self.m)
        if self.produit.get()=="":
            messagebox.showerror("erreur","Selectionnez un produit")
        else:
            self.textarea.insert(END,f"\n{self.produit.get()}\t\t\t{self.qte.get()}\t\t\t{self.m}")
            self.totalbrute.set(str("Rs.%.2f"%(sum(self.l))))
            self.taxe.set(str("Rs.%.2f"%((((sum(self.l))-(self.prix.get()))*1)/100)))
            self.totalnet.set(str("Rs.%.2f"%(((sum(self.l)) + ((((sum(self.l)) - (self.prix.get())) *   1 )/100)))))

    def fonctionCategorie(self,even=""):
        if   self.txt_categorie.get()=="Vetement":
             self.txt_souscategorie.config(values=self.list_souscategorieVetement)
             self.txt_souscategorie.current(0)

        if  self.txt_categorie.get() == "Style de vie":
            self.txt_souscategorie.config(values=self.list_souscategoriestyle)
            self.txt_souscategorie.current(0)

        if  self.txt_categorie.get() == "telephone":
            self.txt_souscategorie.config(values=self.list_souscategorietel)
            self.txt_souscategorie.current(0)

    ########fonction
    def fonctionsouscategorie(self, even=""):
        #vetement
        if  self.txt_souscategorie.get =="pantelon":
            self.txt_nomproduit.config(values=self.pantelon)
            self.txt_nomproduit.current(0)

        if  self.txt_souscategorie.get() == "T-shirt":
            self.txt_nomproduit.config(values=self.t_shirt)
            self.txt_nomproduit.current(0)

        if  self.txt_souscategorie.get() == "Shirt":
            self.txt_nomproduit.config(values=self.shirt)
            self.txt_nomproduit.current(0)

        # Style de vie

        if  self.txt_souscategorie.get == "Bath Soap":
            self.txt_nomproduit.config(values=self.Bath_soap)
            self.txt_nomproduit.current(0)

        if  self.txt_souscategorie.get == "Creme":
            self.txt_nomproduit.config(values=self.t_creme)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get == "huile cheveuxx":
            self.txt_nomproduit.config(values=self.huile)
            self.txt_nomproduit.current(0)

        # telephone
        if self.txt_souscategorie.get=="iphone":
            self.txt_nomproduit.config(values=self.iphone)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get=="Samsung":
            self.txt_nomproduit.config(values=self.samsung)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get=="Huawei":
            self.txt_nomproduit.config(values=self.huawei)
            self.txt_nomproduit.current(0)


        if self.txt_souscategorie.get=="Techno":
            self.txt_nomproduit.config(values=self.techno)
            self.txt_nomproduit.current(0)

    def fonctionomproduit(self, event=""):

        if self.txt_nomproduit.get()=="levis":
            self.txt_prix.config(values=self.price_levis)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="mufti":
            self.txt_prix.config(values=self.price_mufti)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Skyar":
            self.txt_prix.config(values=self.price_skybar)
            self.txt_prix.current(0)
            self.qte.set(1)



        if self.txt_nomproduit.get() == "polo":
            self.txt_prix.config(values=self.price_polo)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Roadster":
            self.txt_prix.config(values=self.price_roadster)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get() == "jack&jones":
            self.txt_prix.config(values=self.price_jack_jones)
            self.txt_prix.current(0)
            self.qte.set(1)



        if  self.txt_nomproduit.get() == "peter England":
            self.txt_prix.config(values=self.price_peter)
            self.txt_prix.current(0)
            self.qte.set(1)


        if  self.txt_nomproduit.get() == "Louis philipe":
            self.txt_prix.config(values=self.price_Louis)
            self.txt_prix.current(0)
            self.qte.set(1)


        if  self.txt_nomproduit.get() == "hugoBoss":
            self.txt_prix.config(values=self.price_Boss)
            self.txt_prix.current(0)
            self.qte.set(1)



        if  self.txt_nomproduit.get() == "livebuy":
            self.txt_prix.config(values=self.price_livebuy)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "lux":
            self.txt_prix.config(values=self.price_lux)
            self.txt_prix.current(0)
            self.qte.set(1)


        if  self.txt_nomproduit.get() == "Santoor":
            self.txt_prix.config(values=self.price_santoor)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "Pearl":
            self.txt_prix.config(values=self.price_pearl)
            self.txt_prix.current(0)
            self.qte.set(1)


        if  self.txt_nomproduit.get() == "Garnier":
            self.txt_prix.config(values=self.price_garnier)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "faire&lovely":
            self.txt_prix.config(values=self.price_fair)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "ponds":
            self.txt_prix.config(values=self.price_pond)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "olay":
            self.txt_prix.config(values=self.price_olay)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "parachute":
            self.txt_prix.config(values=self.price_parachute)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "jasmin":
            self.txt_prix.config(values=self.price_jasmin)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "Bajaj":
            self.txt_prix.config(values=self.price_Bajaj)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "IphoneX ":
            self.txt_prix.config(values=self.price_iphone_x)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() =="Iphone11":
            self.txt_prix.config(values=self.price_iphone_11)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "Iphonemax ":
            self.txt_nomproduit.config(values=self.price_iphone_max)
            self.txt_nomproduit.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "A10":
            self.txt_prix.config(values=self.price_A10)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "S10":
            self.txt_prix.config(values=self.price_S10)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() == "A80 ":
            self.txt_prix.config(values=self.price_A80)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() =="huawei y95":
            self.txt_prix.config(values=self.price_y95)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get()=="huawei p8":
            self.txt_prix.config(values=self.price_p8)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get() =="huawei Mate":
            self.txt_prixt.config(values=self.price_mate)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get()=="techno cam11":
            self.txt_prix.config(values=self.price_com11)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() =="techno cam 12 ":
            self.txt_prix.config(values=self.price_com12)
            self.txt_prix.current(0)
            self.qte.set(1)

        if  self.txt_nomproduit.get() =="techno cam13":
            self.txt_prix.config(values=self.price_com13)
            self.txt_prix.current(0)
            self.qte.set(1)


if __name__ == "__main__":
    root = Tk()
    obj = Supermarche(root)
    root.mainloop()
