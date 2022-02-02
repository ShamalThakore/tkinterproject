import os
import random
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import tempfile

class RAIGADBAZARManagement:
    def __init__(self,root):
        self.root=root
        self.root.title("RAIGAD BAZAR MANAGEMENT SYSTEM")
        self.root.geometry("1300x700+0+0")

#_____________________________ images___________________________________________

    #------------------image1------------------------------------
        img1=Image.open("C:/Users/shamal/Desktop/images (2).jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_img=Label(self.root,image=self.photoimg1)
        lbl_img.place(x=0,y=0,width=320,height=100)

    #-------------------image2----------------------------------

        img2 = Image.open("C:/Users/shamal/Desktop/images (1).jfif")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img = Label(self.root, image=self.photoimg2)
        lbl_img.place(x=320, y=0, width=320, height=100)

    #---------------------image3--------------------------------
        img3 = Image.open("C:/Users/shamal/Desktop/images.jfif")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img = Label(self.root, image=self.photoimg3)
        lbl_img.place(x=640, y=0, width=330, height=100)

    #---------------------image4-----------------------------------
        img4 = Image.open("C:/Users/shamal/Desktop/image.jpg")
        img4 = img4.resize((500, 130), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbl_img = Label(self.root, image=self.photoimg4)
        lbl_img.place(x=950, y=0, width=350, height=100)

#------------------------------------Heding label----------------------------------------------------------


        lbl_title=Label(self.root,text="RAIGAD BAZAR MANAGEMENT SYSTEM",
                        bg="white",fg="red",font=("times new roman",30,"bold"))
        lbl_title.place(x=0,y=100,width=1280,height=45)

#--------------------------------------- DATAFRAME --------------------------------------------------------------
        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=150, width=1280, height=500)

        # _------------------------------variablea-----------------------------------------------------------------

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        z = random.randint(1000, 9999)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.quality = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()

        #___________________----------------customer frame:-------------------_____________________________________________

        Cust_Frame=LabelFrame(Main_Frame, text = "Customer", font = ("times new roman", 15, "bold"),bg="white", fg="red")
        Cust_Frame.place(x=10, y=5, width=300, height=126)

        self.lblCustName=Label(Cust_Frame,text="Customer Name  :",font=("times new roman",11,"bold"),bg="white")
        self.lblCustName.grid(row=0,column=0,sticky=W,padx=3,pady=1)

        self.txtCustName=ttk.Entry(Cust_Frame, textvariable=self.c_name , font = ("times new roman", 11, "bold"),width=19)
        self.txtCustName.grid(row=0,column=1, sticky=W,padx=3,pady=1)

        self.lbl_mob = Label(Cust_Frame, text="Mobile No :", font=("times new roman", 11, "bold"), bg="white")
        self.lbl_mob.grid(row=1, column=0, sticky=W, padx=3, pady=1)

        self.entry_mob= ttk.Entry(Cust_Frame, textvariable=self.c_phone, font=("times new roman", 11, "bold"), width=19)
        self.entry_mob.grid(row=1, column=1, sticky=W,padx=3,pady=1)

        self.lblEmail = Label(Cust_Frame, text="Email :", font=("times new roman", 11, "bold"), bg="white")
        self.lblEmail.grid(row=2, column=0, sticky=W, padx=3, pady=1)

        self.txtEmail = ttk.Entry(Cust_Frame, textvariable=self.c_email,font=("times new roman", 11, "bold"), width=19)
        self.txtEmail.grid(row=2, column=1, sticky=W, padx=3, pady=1)

# ___________________________________________________________________________________________________________________________________________________________
        # __________________-------------Product Categories list------------------____________________________

        self.Category = ["Select Option", "Grocery", "Clothing", "LifeStyle"]

        # SubCategory Grocery list

        self.SubCatGrocery= ["Rice", "Dal/Beans", "Vegitables/Fruits","Dairy","DryFruits","Sauces/Oil"]

        # Rice
        self.Rice = ["Basmathi Rice", "Ponni Rice", "Brown Rice", "Idli/Dosa Rice", "Nadu Rice"]
        self.price_Basmathi = 450
        self.price_Ponni = 400
        self.price_Brown = 350
        self.price_Idli = 440
        self.price_Nadu = 250

        # Dal/Beans
        self.Dal_Beans = ["Arhar/Tur Dal", "Moong Dal", "Masoor Dal", "Urad Dal", "Channa Dal"]
        self.price_Arhar = 50
        self.price_Moong = 90
        self.price_Masoor = 50
        self.price_Urad = 45
        self.price_Channa= 25

        # Vegitables/Fruits
        self.Vegitables_Fruits = ["Apple", "Tomato", "Capsicum", "Carrot", "Mango"]
        self.price_Apple = 50
        self.price_Tomato = 20
        self.price_Capsicum = 35
        self.price_Carrot = 40
        self.price_Mango= 25

        # Dairy
        self.Dairy = ["Milk", "Paneer", "Butter", "Cheese", "Cream"]
        self.price_Milk= 50
        self.price_Paneer = 20
        self.price_Butter = 35
        self.price_Cheese = 40
        self.price_Cream = 25

        # DryFruits
        self.DryFruits = ["Almonds", "Cashew", "Pistachio", "Walnuts", "Raisins"]
        self.price_Almonds = 50
        self.price_Cashew = 20
        self.price_Pistachio = 35
        self.price_Walnuts = 40
        self.price_Raisins = 25

        # Sauces/Oil
        self.Sauces_Oil = ["BBQ Sauce", "Oil", "Vinegar","Salad Dressing", "Maple Syrup"]
        self.price_BBQ_Sauce= 50
        self.price_Oil = 20
        self.price_Vinegar = 35
        self.price_Salad_Dressing = 40
        self.price_Maple_Syrup = 25



#----------------------------------- SubCategory Clothiog---------------------------------------------------

        self.SubCatClothing = ["Pant", "T-Shirt", "Shirt"]
    # pant
        self.pant = ["Levis", "Mufti", "Spykar"]
        self.price_levis = 5000
        self.price_mufti = 5550
        self.price_spykar = 6000


    # T-shirt
        self.T_Shirt=["Polo","Roadster","Jack&Jones"]
        self.price_polo=1500
        self.price_roadster=2000
        self.price_jackjones=2500

        self.Shirt=["Peter England","Louis Phillipe","Park Avenue"]
        self.price_Peter=2100
        self.price_Louis=3200
        self.price_Park=4500

    # SubCatLifeStyle___________________

        self.SubCatLifeStyle = ["Bath Soap", "Face Creame", "Hair Oil"]
        self.Bath_Soap = ["LifeBuy", "Lux", "Santoor", "Pear"]
        self.price_life = 5000
        self.price_lux = 5550
        self.price_santoor = 6000
        self.price_Pear = 6000

        self.Face_Creame=["Fair&Lovely","Ponds","Olay","Garnier"]
        self.price_fair=20
        self.price_ponds=20
        self.price_olay=20
        self.price_garnier=25

        self.Hair_Oil=["Parachute","Jashmin","Bajaj"]
        self.price_para=25
        self.price_jashmin=22
        self.price_bajaj=30


#________________________________------- Product lable Frame--------___________________________________________________

        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("times new roman", 15, "bold"), bg="white", fg="red")
        Product_Frame.place(x=320, y=5, width=542, height=126)

        # Category___
        self.lblCategory = Label(Product_Frame, text="Select Categories :", font=("times new roman", 12, "bold"), bg="white")
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=3, pady=1)

        self.Combo_Category=ttk.Combobox(Product_Frame, value=self.Category ,font=("times new roman", 13, "bold"),width= 15)
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=3, pady=1)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        # SubCategory_________
        self.lblSubCategory = Label(Product_Frame, text="SubCategories :", font=("times new roman", 12, "bold"),bg="white")
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=3, pady=1)

        self.ComboSubCategory = ttk.Combobox(Product_Frame,value=[""], font=("times new roman", 13, "bold"), width=15)
        self.ComboSubCategory.grid(row=1, column=1, sticky=W, padx=3, pady=1)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product Name________
        self.lblProduct = Label(Product_Frame, text="Product Name :", font=("times new roman", 12, "bold"),bg="white")
        self.lblProduct.grid(row=2, column=0, sticky=W, padx=3, pady=1)

        self.ComboProduct = ttk.Combobox(Product_Frame, textvariable=self.product,font=("times new roman", 13, "bold"), width=15)
        self.ComboProduct.grid(row=2, column=1, sticky=W, padx=3, pady=1)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        # Price
        self.lblPrice = Label(Product_Frame, text="Price :", font=("times new roman", 12, "bold"), bg="white")
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=3, pady=1)

        self.ComboPrice = ttk.Combobox(Product_Frame, textvariable=self.prices,font=("times new roman", 13, "bold"), width=15)
        self.ComboPrice.grid(row=0, column=3, sticky=W, padx=3, pady=1)

        # Quality
        self.lblQuality= Label(Product_Frame, text="Quality :", font=("times new roman", 12, "bold"), bg="white")
        self.lblQuality.grid(row=1, column=2, sticky=W, padx=3, pady=1)

        self.ComboQuality = ttk.Entry(Product_Frame,textvariable=self.quality, font=("times new roman", 13, "bold"), width=17)
        self.ComboQuality.grid(row=1, column=3, sticky=W, padx=3, pady=1)


#__________________________-----------Middle Photos--------------_________________________________________________
# Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=134,width=850,height=300)

    # images___________
        img5 = Image.open("C:/Users/shamal/Desktop/dryfruits.jpg")
        img5 = img5.resize((500, 130), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbl_img = Label(MiddleFrame, image=self.photoimg5)
        lbl_img.place(x=-9, y=-100, width=280, height=300)

        # image 6________
        img6 = Image.open("C:/Users/shamal/Desktop/veggie.jpg")
        img6 = img6.resize((500, 130), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lbl_img = Label(MiddleFrame, image=self.photoimg6)
        lbl_img.place(x=-9, y=80, width=280, height=170)

        # image 7________
        img7 = Image.open("C:/Users/shamal/Desktop/o.jpg")
        img7 = img7.resize((500, 130), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        lbl_img = Label(MiddleFrame, image=self.photoimg7)
        lbl_img.place(x=280, y=80, width=279, height=170)

        # image 8________
        img8 = Image.open("C:/Users/shamal/Desktop/download (1).jfif")
        img8 = img8.resize((500, 130), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        lbl_img = Label(MiddleFrame, image=self.photoimg8)
        lbl_img.place(x=280, y=-70, width=279, height=170)

        # image 9________
        img9 = Image.open("C:/Users/shamal/Desktop/r.jpeg")
        img9 = img9.resize((500, 130), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        lbl_img = Label(MiddleFrame, image=self.photoimg9)
        lbl_img.place(x=570, y=80, width=279, height=170)

        # image 10________
        img10 = Image.open("C:/Users/shamal/Desktop/f.jpg")
        img10 = img10.resize((500, 130), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        lbl_img = Label(MiddleFrame, image=self.photoimg10)
        lbl_img.place(x=570, y=-70, width=279, height=170)


#------------------------------------ Right Frame Bill Aria-------------------------------------------------------

        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Aria",font=("times new roman", 15, "bold"), bg="white",fg="red")
        RightLabelFrame.place(x=870, y=35, width=400, height=335)

        # Search
        Search_Frame = Frame(Main_Frame, bd=2, bg="white")
        Search_Frame.place(x=870, y=1,width=400,height=40)

        self.lblBill = Label(Search_Frame, text="Bill Number", font=("times new roman", 12, "bold"), fg="white", bg="red")
        self.lblBill.grid(row=0, column=0, sticky=W, padx=3, pady=1)

        self.txt_Entry_Search= ttk.Entry(Search_Frame,font=("times new roman", 12, "bold"),width=23)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W)

        self.BtnSearch=Button(Search_Frame, command=self.find_bill, text="Search", font=("times new roman", 11, "bold"), fg="white",width=11, cursor="hand2",bg="red")
        self.BtnSearch.grid(row=0, column=4)

          # Scrollbar____________________-------------------------------------------------------------------
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

#     # Bill Counter label Frame___________________________________________________

        Bottom_Frame= LabelFrame(Main_Frame, text="Bill Counter", font=("times new roman", 15, "bold"), bg="white",fg="red")
        Bottom_Frame.place(x=0, y=371, width=1265, height=115)

         # Sub Total
        self.lblSubTotal = Label(Bottom_Frame, text="Sub Total :", font=("times new roman", 12, "bold"), bg="white")
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=3, pady=1)

        self.EntySubTotal = ttk.Entry(Bottom_Frame,textvariable=self.sub_total, font=("times new roman", 11, "bold"), width=17)
        self.EntySubTotal.grid(row=0, column=1, sticky=W, padx=3, pady=1)

#         # Gov. Tax
        self.lbl_tax = Label(Bottom_Frame, text="Gov. Tax :", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=3, pady=1)

        self.txt_tax = ttk.Entry(Bottom_Frame, textvariable=self.tax_input , font=("times new roman", 11, "bold"), width=17)
        self.txt_tax.grid(row=1, column=1, sticky=W, padx=3, pady=1)

         # Amount Total
        self.lblAmountTotal = Label(Bottom_Frame, text="Total :", font=("times new roman", 12, "bold"), bg="white")
        self.lblAmountTotal.grid(row=2, column=0, sticky=W, padx=3, pady=1)

        self.txtAmountTotal = ttk.Entry(Bottom_Frame, textvariable=self.total, font=("times new roman", 11, "bold"), width=17)
        self.txtAmountTotal.grid(row=2, column=1, sticky=W, padx=3, pady=1)

    # Button Frame_______________-
        Btn_Frame = Frame(Bottom_Frame, bd=2, bg="white")
        Btn_Frame.place(x=320, y=0)

        self.BtnAddToCart = Button(Btn_Frame, command=self.AddItem,  height=2,text="Add To Cart", font=("times new roman", 14, "bold"),
                           bg="orangered", fg="white", width=13, cursor="hand2")
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btngenerate_bill = Button(Btn_Frame, command=self.gen_bill,  height=2, text="Generate Bill", font=("times new roman", 14, "bold"),
                               bg="orangered", fg="white", width=13, cursor="hand2")
        self.Btngenerate_bill.grid(row=0, column=1)

        self.BtnSave = Button(Btn_Frame, command=self.save_bill, height=2, text="Save", font=("times new roman", 14, "bold"), bg="orangered",
                      fg="white", width=13, cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint = Button(Btn_Frame,command=self.print,  height=2, text="Print Bill", font=("times new roman", 14, "bold"), bg="orangered",
                       fg="white", width=13, cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(Btn_Frame, command=self.clear,  height=2, text="Clear", font=("times new roman", 14, "bold"), bg="orangered",
                       fg="white", width=13, cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(Btn_Frame, command=self.root.destroy, height=2, text="Exit", font=("times new roman", 14, "bold"),
                      bg="orangered", fg="white", width=13, cursor="hand2")
        self.BtnExit.grid(row=0, column=5)

#_____________________________--------------------------------------------------------------------------------
        self.welcome()

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome Raigad Bazar")
        self.textarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number: {self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email: {self.c_email.get()}")

        self.textarea.insert(END, "\n=========================================")
        self.textarea.insert(END,f"\n Products\t\t\tQuantity\t\tPrice")
        self.textarea.insert(END, "\n=========================================\n")
#________________________________________________________________________________________________________

    # Add to Cart
        self.l = []

    def AddItem(self):
        Tax = 1
        self.n = self.prices.get()
        self.m = self.quality.get() * self.n
        self.l.append(self.m)
        if self.product.get() == "":
            messagebox.showerror("Error", "Plaease Select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.quality.get()}\t\t{self.m}")
            self.sub_total.set(str("Rs.%.2f" % (sum(self.l))))
            self.tax_input.set(str("Rs.%.2f" % ((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))
            self.total.set(
                str("Rs.%.2f" % (((sum(self.l)) + ((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))))

 #  Gen bill

    def gen_bill(self):
        if self.product.get() == "":
            messagebox.showerror("Error", "Plaease Add To Cart Product")
        else:
            text = self.textarea.get(10.0, (10.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(END, "\n=========================================")
            self.textarea.insert(END, f"\n Sub Amount:\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Amount:\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount:\t\t{self.total.get()}")
            self.textarea.insert(END, "\n=========================================")

# Save bill

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("bill/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            op = messagebox.showinfo("Saved", f"Bill No:{self.bill_no.get()} Save Successfully")
            f1.close()

# print Bill

    def print(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp(".txt")
        open(filename,"w").write(q)
        os.startfile(filename,"print")

# Search
    def find_bill(self):
        found = "no"
        for i in os.listdir("bill/"):
              if i.split('_')[0] == self.search_bill.get():
                   f1 = open(f"bill/{i}", "r")
                   self.textarea.delete(1.0, END)
                   for d in f1:
                         self.textarea.insert(END, d)
                   f1.close()
                   found = "yes"
              if found == "no":
                   messagebox.showerror("Error", "Invalid Bill No.")


# Clear Bill

    def clear(self):
        self.textarea.delete(1.0, END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.quality.set(0)
        self.l = [0]
        self.welcome()

    #===============================================================================================================
       #_________________---------------combo box---------------------- ______________________

    def Categories(self,event=""):
        if self.Combo_Category.get()=="Grocery":
           self.ComboSubCategory.config(value=self.SubCatGrocery)
           self.ComboSubCategory.currrent(0)

        if self.Combo_Category.get() == "Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.currrent(0)

        if self.Combo_Category.get() == "LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.currrent(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Rice":
            self.ComboProduct.config(value=self.Rice)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Dal/Beans":
            self.ComboProduct.config(value=self.Dal_Beans)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Vegitables/Fruits":
            self.ComboProduct.config(value=self.Vegitables_Fruits)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Dairy":
            self.ComboProduct.config(value=self.Dairy)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "DryFruits":
            self.ComboProduct.config(value=self.DryFruits)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Sauces/Oil":
            self.ComboProduct.config(value=self.Sauces_Oil)
            self.ComboProduct.current(0)

#_-------------Clothing _--------------------

        if self.ComboSubCategory.get() == "Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "T-Shirt":
            self.ComboProduct.config(value=self.T_Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)

#_------------LifeStyle--------------

        if self.ComboSubCategory.get() == "Bath Soap":
            self.ComboProduct.config(value=self.Bath_Soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Face Creame":
            self.ComboProduct.config(value=self.Face_Creame)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Hair Oil":
            self.ComboProduct.config(value=self.Hair_Oil)
            self.ComboProduct.current(0)

#-----------Price_____________________________________________________

    def price(self,event=""):
        # Rice
        if self.ComboProduct.get() == "Basmathi Rice":
            self.ComboPrice.config(value=self.price_Basmathi)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Ponni Rice":
            self.ComboPrice.config(value=self.price_Ponni)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Brown Rice":
            self.ComboPrice.config(value=self.price_Brown)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Idli/Dosa Rice":
            self.ComboPrice.config(value=self.price_Idli)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Nadu Rice":
            self.ComboPrice.config(value=self.price_Nadu)
            self.ComboPrice.current(0)
            self.quality.set(1)

        # Dal/Beans
        if self.ComboProduct.get() == "Arhar/Tur Dal":
            self.ComboPrice.config(value=self.price_Arhar)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Moong Dal":
            self.ComboPrice.config(value=self.price_Moong)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Masoor Dal":
            self.ComboPrice.config(value=self.price_Masoor)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Urad Dal":
            self.ComboPrice.config(value=self.price_Urad)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Channa Dal":
            self.ComboPrice.config(value=self.price_Channa)
            self.ComboPrice.current(0)
            self.quality.set(1)

        # Vegitables/Fruits
        if self.ComboProduct.get() == "Apple":
            self.ComboPrice.config(value=self.price_Apple)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Tomato":
            self.ComboPrice.config(value=self.price_Tomato)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Capsicum":
            self.ComboPrice.config(value=self.price_Capsicum)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Carrot":
            self.ComboPrice.config(value=self.price_Carrot)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Mango":
            self.ComboPrice.config(value=self.price_Mango)
            self.ComboPrice.current(0)
            self.quality.set(1)

        # Dairy
        if self.ComboProduct.get() == "Milk":
            self.ComboPrice.config(value=self.price_Milk)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Paneer":
            self.ComboPrice.config(value=self.price_Paneer)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Butter":
            self.ComboPrice.config(value=self.price_Butter)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Cheese":
            self.ComboPrice.config(value=self.price_Cheese)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Channa Cream":
            self.ComboPrice.config(value=self.price_Cream)
            self.ComboPrice.current(0)
            self.quality.set(1)

        # DryFruits
        if self.ComboProduct.get() == "Almonds":
            self.ComboPrice.config(value=self.price_Almonds)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Cashew":
            self.ComboPrice.config(value=self.price_Cashew)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Pistachio":
            self.ComboPrice.config(value=self.price_Pistachio)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Walnuts":
            self.ComboPrice.config(value=self.price_Walnuts)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Raisins":
            self.ComboPrice.config(value=self.price_Raisins)
            self.ComboPrice.current(0)
            self.quality.set(1)

        # Sauces/oil
        if self.ComboProduct.get() == "BBQ Sauce":
            self.ComboPrice.config(value=self.price_BBQ_Sauce)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Oil":
            self.ComboPrice.config(value=self.price_Oil)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Vinegar":
            self.ComboPrice.config(value=self.price_Vinegar)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Salad Dressing":
            self.ComboPrice.config(value=self.price_Salad_Dressing)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get() == "Maple Syrup":
            self.ComboPrice.config(value=self.price_Maple_Syrup)
            self.ComboPrice.current(0)
            self.quality.set(1)

        # Pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_spykar)
            self.ComboPrice.current(0)
            self.quality.set(1)

   # T-Shirt ___________________________________

        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_roadster)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_jackjones)
            self.ComboPrice.current(0)
            self.quality.set(1)

    # Shirt____________----

        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.quality.set(1)

    # LifeStyle
        if self.ComboProduct.get() == "LifeBuy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Pear":
            self.ComboPrice.config(value=self.price_Pear)
            self.ComboPrice.current(0)
            self.quality.set(1)

    # Face Creame
        if self.ComboProduct.get()=="Fair&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.quality.set(1)

    # Hair Oil
        if self.ComboProduct.get() == "Parachute":
            self.ComboPrice.config(value=self.para)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Jashmin":
            self.ComboPrice.config(value=self.price_jashmin)
            self.ComboPrice.current(0)
            self.quality.set(1)

        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.quality.set(1)

if __name__=="__main__":
    root=Tk()
    obj=RAIGADBAZARManagement(root)
    root.mainloop()
