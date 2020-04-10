from tkinter import*
from tkinter import ttk
import random
import sqlite3
import time
from datetime import datetime
import tkinter.messagebox

def main():
    root=Tk()
    app=Window1(root)


class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Product Review Analysis for Genuine Rating")
        self.master.geometry('1350x750+0+0')
        self.master.configure(bg='powder blue')
        self.frame=Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.lblTitle=Label(self.frame, text='Product Review Analysis for Genuine Rating', font=('arial',50,'bold'),bg='powder blue',fg='black')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)

  #==========================================================================================================================================

        self.LoginFrame1=LabelFrame(self.frame, width=1350, height=600, font=('arial',20,'bold'),relief='ridge', bg='cadet blue',bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2=LabelFrame(self.frame, width=1000, height=600, font=('arial',20,'bold'),relief='ridge', bg='cadet blue',bd=20)
        self.LoginFrame2.grid(row=2, column=0)

  #================================================= Label & Entry===========================================================================

        self.lblUsername=Label(self.LoginFrame1, text= 'Username', font=('arial',20,'bold'), bd=22,bg='cadet blue' , fg='Cornsilk')
        self.lblUsername.grid( row=0, column=0)
        self.txtUsername=Entry(self.LoginFrame1, font=('arial',20,'bold'),textvariable=self.Username)
        self.txtUsername.grid( row=0, column=1, padx=119)

        self.lblPassword=Label(self.LoginFrame1, text= 'Password', font=('arial',20,'bold'),bd=22,bg='cadet blue' , fg='Cornsilk')
        self.lblPassword.grid( row=1, column=0)
        self.txtPassword=Entry(self.LoginFrame1, font=('arial',20,'bold'),show = "*", textvariable=self.Password)
        self.txtPassword.grid( row=1, column=1, columnspan=2, pady=30)
                                     
  #====================================================  Button==============================================================================
        self.btnLogin=Button(self.LoginFrame2, text='Login',width=17,font=('arial',20,'bold'),command=self.Login_System)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=8)

        self.btnReset=Button(self.LoginFrame2, text='Reset',width=17,font=('arial',20,'bold'),command=self.Reset)
        self.btnReset.grid(row=3,column=1,pady=20,padx=8)

        self.btnExit=Button(self.LoginFrame2, text='Exit',width=17,font=('arial',20,'bold'), command=self.iExit)
        self.btnExit.grid(row=3,column=2,pady=20,padx=8)

  #===========================================================================================================================================

    def Login_System(self):
        u=(self.Username.get())
        p=(self.Password.get())

        if(u==str(1234) and p==str(1234)):
            self.newWindow=Toplevel(self.master)
            self.app=Review(self.newWindow)
        else:
            tkinter.messagebox.askyesno("Login Systems", "Invalid login detail")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Login Systems", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command=self.new_window
            return   
       

    def new_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Library(self.newWindow)
 
    

class Review:
    
    
    def __init__(self,master):
        self.master=master
        self.master.title("Product Review Analysis for Genuine Rating")
        self.master.geometry('1350x750+0+0')
        self.master.configure(bg='cadet blue')

        MType=StringVar()
        Ref=StringVar()
        Title=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Address1=StringVar()
        Address2=StringVar()
        Pincode=StringVar()
        MobileNo=StringVar()
        ProductName=StringVar()
        Cost=StringVar()
        CompanyName=StringVar()
        Rsize=StringVar()
        Feature=StringVar()
        DateOfManufacture=StringVar()
        DateOfReview=StringVar()
        KindOfReview=StringVar()
        WriteReview=StringVar()
        Rate=StringVar()


        def iReset2():
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            MobileNo.set("")
            Pincode.set("")
            ProductName.set("")
            Cost.set("")
            CompanyName.set("")
            Rsize.set("")
            Feature.set("")
            DateOfManufacture.set("")
            DateOfReview.set("")
            WriteReview.set("")
            Rate.set("")
            self.txtFrameDetail.delete("1.0",END)
            self.txtDisplayR.delete("1.0",END)
                

        def iDelete():
            iReset2()
            self.txtDisplayR.delete("1.0",END)

        def iEliminate():
            msg=tkinter.messagebox.askyesno("Product Review Analysis for Genuine Rating ", "Confirm if you want to exit")
            if msg=="True":
               master.quit()
                                

        def iDisplayData():
            self.txtFrameDetail.insert(END,MType.get()+"\t"+Ref.get()+"\t"+Title.get()+"\t"+Firstname.get()+
                                       "\t"+ Surname.get()+"\t"+Address1.get()+"\t"+Address2.get()+"\t"+"\t"+MobileNo.get()+"\t"+CompanyName.get()+"\t"+ProductName.get()
                                       +"\t"+WriteReview.get()+"\t "+Rate.get()+ "\n")

        def iReceipt():
            self.txtDisplayR.delete("1.0",END)
            self.txtDisplayR.insert(END, "Member Type: \t\t" + MType.get() + "\n")
            self.txtDisplayR.insert(END, "Ref No : \t\t" + Ref.get() + "\n")
            self.txtDisplayR.insert(END, "Title: \t\t" + Title.get() + "\n")
            self.txtDisplayR.insert(END, "First Name: \t\t" + Firstname.get() + "\n")
            self.txtDisplayR.insert(END, "Surname: \t\t" + Surname.get() + "\n")
            self.txtDisplayR.insert(END, "City : \t\t" + Address1.get() + "\n")
            self.txtDisplayR.insert(END, "State : \t\t" + Address2.get() + "\n")
            self.txtDisplayR.insert(END, "Mobile No: \t\t" + MobileNo.get() + "\n")
            self.txtDisplayR.insert(END, "Pincode : \t\t" + Pincode.get() + "\n")
            self.txtDisplayR.insert(END, "Review: \t\t" + WriteReview.get() + "\n")
            self.txtDisplayR.insert(END, "Rating (Out of 5): \t\t" + Rate.get() + "\n")
            self.txtDisplayR.insert(END, "Cost: \t\t" + Cost.get() + "\n")
            self.txtDisplayR.insert(END, "Storage Capacity: \t\t" + Rsize.get() + "\n")
            self.txtDisplayR.insert(END, "Feature: \t\t" +Feature.get() + "\n")
            self.txtDisplayR.insert(END, "Date of Review: \t\t" + DateOfReview.get() + "\n")
            self.txtDisplayR.insert(END, "Date of Manufacture: \t\t" + DateOfManufacture.get() + "\n")
            self.txtDisplayR.insert(END, "Rating/Feedback of Product : \t\t" + Rate.get() + "\n")
            self.txtDisplayR.insert(END, "Cost: \t\t" + Cost.get() + "\n")

    
        MainFrame=Frame(self.master)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle=Label(TitleFrame, width=40 , font=("arial", 30 , "bold"),text="\t Product Review Analysis for Genuine Rating \t", padx=15)
        self.lblTitle.grid()

        ButtonFrame=Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail=Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame , bd=10, width=800, height=300, padx=20, relief=RIDGE, font=("arial",12,"bold"), text="Product Review Analysis for Genuine Rating Info:",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame , bd=10, width=450, height=300, padx=20, relief=RIDGE, font=("arial",12,"bold"), text="Review Detail:",)
        DataFrameRIGHT.pack(side=RIGHT)

        #========================= Widgets=====================================#
        self.lblMemberType = Label(DataFrameLEFT, font=("arial", 12, "bold"), text ="Type Of Review:", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, state="readonly",textvariable=MType, font=("arial", 12, "bold"), width=23)
        self.cboMemberType['value']=('', 'Client', 'Member', 'Admin')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Product Name :",padx=2,pady=2)
        self.lblTitle.grid(row=0,column=2,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=ProductName,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','Mobile','Laptop')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=0,column=3)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Unique ID:",padx=2,pady=2)
        self.lblTitle.grid(row=1,column=0,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Ref,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','11111','22222','33333','44444','55555')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=1,column=1)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Name of the Company:",padx=2,pady=2)
        self.lblTitle.grid(row=1,column=2,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=CompanyName,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','Oppo','Samsung','Nokia','Redmi','Apple','Asus','HP','HCL','Acer','Dell')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=1,column=3)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Title:",padx=2,pady=2)
        self.lblTitle.grid(row=2,column=0,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Title,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=('', 'Mr.', 'Miss.', 'Mrs.', 'Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2,column=1)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Price (INR):",padx=2,pady=2)
        self.lblTitle.grid(row=2,column=2,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Cost,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','Rs 10,000','Rs 20,000','Rs 25,000', 'Rs 40,000', 'Rs 30,000' )
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2,column=3)




        self.lblFirstName = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="First Name:", padx=2,pady=2)
        self.lblFirstName.grid(row=3,column=0,sticky=W)
        self.txtFirstName=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Firstname)
        self.txtFirstName.grid(row=3,column=1)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Date Of Manufature:",padx=2,pady=2)
        self.lblTitle.grid(row=3,column=2,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=DateOfManufacture,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','10th January 2010','20th April 2012', '15th June 2014', '5th October 2015' )
        self.cboTitle.current(0)
        self.cboTitle.grid(row=3,column=3)

        self.lblSurname = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Last Name:", padx=2,pady=2)
        self.lblSurname.grid(row=4,column=0,sticky=W)
        self.txtSurname=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Surname)
        self.txtSurname.grid(row=4,column=1)
        
        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Date of Review :",padx=2,pady=2)
        self.lblTitle.grid(row=4,column=2,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=DateOfReview,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','10th April 2020','20th April 2020', '15th June 2020', '5th October 2020' )
        self.cboTitle.current(0)
        self.cboTitle.grid(row=4,column=3)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="City :",padx=2,pady=2)
        self.lblTitle.grid(row=5,column=0,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Address1,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','Bhopal','Kolkata', 'Jalandhar', 'Bangalore', 'Chennai' )
        self.cboTitle.current(0)
        self.cboTitle.grid(row=5,column=1)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Storage Capacity (in GB/TB):",padx=2,pady=2)
        self.lblTitle.grid(row=5,column=2,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Rsize,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','2GB','4GB', '8GB', '1TB','2TB' )
        self.cboTitle.current(0)
        self.cboTitle.grid(row=5,column=3)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="State :",padx=2,pady=2)
        self.lblTitle.grid(row=6,column=0,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Address2,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','Madhya Pradesh','West Bengal', 'Punjab', 'Karnataka', 'Tamil Nadu' )
        self.cboTitle.current(0)
        self.cboTitle.grid(row=6,column=1)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Unique/Special Feature:",padx=2,pady=2)
        self.lblTitle.grid(row=6,column=2,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Feature,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','High Pixel Camera','Good Processor', 'Light in Weight', 'Flexible','Portable' )
        self.cboTitle.current(0)
        self.cboTitle.grid(row=6,column=3)
        


        self.lblPostCode=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Mobile Number :", padx=2,pady=2)
        self.lblPostCode.grid(row=7,column=0,sticky=W)
        self.txtPostCode=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=MobileNo)
        self.txtPostCode.grid(row=7,column=1)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Write a Review about The Product :",padx=2,pady=2)
        self.lblTitle.grid(row=7,column=2,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=WriteReview,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','Good','Average','Bad')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=7,column=3)

        self.lblSellingPrice=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Pin Code :", padx=2,pady=2)
        self.lblSellingPrice.grid(row=8,column=0,sticky=W)
        self.txtSellingPrice=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Pincode)
        self.txtSellingPrice.grid(row=8,column=1)
        
        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Rate The Product (Out of 5 Stars) :",padx=2,pady=2)
        self.lblTitle.grid(row=8,column=2,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Rate,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=(' ','*','**','***','****','*****')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=8,column=3)

        
        #=========================Widgets=============================================================================#
        self.txtDisplayR=Text(DataFrameRIGHT, font=("arial", 12, "bold"),width=32, height=13, padx=8,pady=20)
        self.txtDisplayR.grid(row=0, column=2)


        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        

        ListOfProducts = ['Smart Phone, Samsung','Smart Phone, Oppo','Smart Phone, Nokia','Smart Phone, Apple ', 'Smart Phone, Redmi','Laptop, HP','Laptop, Dell',
                       'Laptop, Asus','Laptop, Acer','Laptop, HCL']



        def SelectedProduct(evt):
            value=str(productList.get(ListOfProducts.curselection()))
            w=value
          
            
            conn=sqlite3.connect('Review.db')
            c=conn.cursor()        
            c.execute('''SELECT * FROM ReviewDb WHERE Book_Title =?''' ,(w,))
            for row in c.fetchall():
                CompanyName.set(row[0])
                ProductName.set(row[1])
                Cost.set(row[2])
                Feature.set(row[3])
                WriteReview.set(row[4])
                Rate.set(14)
                
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateOfManufacture.set(d1)
                DateOfReview.set(d3)
                DateOfManufacture.set("No")
                
             

        productlist= Listbox(DataFrameRIGHT, width=20,height=12,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        productlist.bind('<<ListboxSelect>>',SelectedProduct)
        productlist.grid(row=0, column=0,padx=8)
        scrollbar.config(command=productlist.yview)

        
        for items in ListOfProducts:
            productlist.insert(END,items)

        #=========================Labels==============================================================================#
        self.lblLabel=Label(FrameDetail, font=("arial",10,'bold'), pady=8,
        text="Member Type  Reference No.  Title  First Name Last Name  City  State  Company Name  Product Name  Cost  Review  Rating  Date Of Manufacture  Date of Review",)
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
        self.txtFrameDetail.grid(row=1,column=0)
        
        #=========================Buttons=============================================================================#        
        self.btnDisplayData=Button(ButtonFrame, text='Display Review', font=('arial',12,'bold'),width=20, bd=4,command=iDisplayData)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnDelete=Button(ButtonFrame, text='Delete Review', font=('arial',12,'bold'),width=20, bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=2)

        self.btnReset1=Button(ButtonFrame, text='Reset', font=('arial',12,'bold'),width=20, bd=4, command=iReset2)
        self.btnReset1.grid(row=0,column=3)

        self.btnExit1=Button(ButtonFrame, text='Exit', font=('arial',12,'bold'),width=20, bd=4, command=iEliminate)
        self.btnExit1.grid(row=0,column=4)

        self.btnSubmit=Button(ButtonFrame, text='Submit Review', font=('arial',12,'bold'),width=20, bd=4, command=iReceipt)
        self.btnSubmit.grid(row=0,column=0)



           
        #======================Frames==========================================#
        
        
        
if __name__=="__main__":
    main()

    

