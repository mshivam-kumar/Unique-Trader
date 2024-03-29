from doctest import master
import sys
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.constants import *
from turtle import left
from tkcalendar import Calendar, DateEntry

from datetime import datetime
from numpy import mask_indices

import crypto_support
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import pandas_datareader as web
import datetime as dt
import mplfinance as mpf
import matplotlib.pyplot as plt





global_fig = None
toolbar = None
start=None
end=None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1100x600+148+40")
        # replacing tkinter symbol in topbar of window
        # top.wm_iconbitmap("C:/Users/shiva/Desktop/crypto analysis/crypto.ico")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Unique Trader - A step towards automation                                                                                                                                                                       made by: Shivam Kumar at DHS \u00a9")
        top.configure(background="#a97ec2")
        top.configure(highlightbackground="#a97ec2")
        top.configure(highlightcolor="black")

        self.top = top

        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.233, rely=0.153, relheight=0.773, relwidth=0.731)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        
        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.058, rely=-0.006, height=31, width=261)
        self.Label1.configure(activebackground="#cc75bf")
        self.Label1.configure(activeforeground="#9780c1")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#af7ac7")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 12")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Select The Dates For Visualization :''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.069, rely=0.050, height=21, width=71)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d89369")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Start Date :''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.069, rely=0.106, height=21, width=71)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d89369")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''End Date :''')

        

        self.Label11 = tk.Label(self.top)
        self.Label11.place(relx=0.031, rely=0.35, height=43, width=140)
        self.Label11.configure(activebackground="#cc75bf")
        self.Label11.configure(activeforeground="#9780c1")
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#af7ac7")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font="-family {Segoe UI} -size 12")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''For Other Coins \nEnter Input Below :''')

        self.Label21 = tk.Label(self.top)
        self.Label21.place(relx=0.017, rely=0.450, height=21, width=53)
        self.Label21.configure(anchor='w')
        self.Label21.configure(background="#d89369")
        self.Label21.configure(compound='left')
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(text='''Name :''')

        self.Label31 = tk.Label(self.top)
        self.Label31.place(relx=0.017, rely=0.50, height=21, width=53)
        self.Label31.configure(anchor='w')
        self.Label31.configure(background="#d89369")
        self.Label31.configure(compound='left')
        self.Label31.configure(disabledforeground="#a3a3a3")
        self.Label31.configure(foreground="#000000")
        self.Label31.configure(text='''Symbol :''')


        self.cNameEntry1 = tk.Entry(self.top)
        self.cNameEntry1.place(relx=0.07, rely=0.450, height=20, relwidth=0.080)
        self.cNameEntry1.configure(background="white")
        self.cNameEntry1.configure(cursor="fleur")
        self.cNameEntry1.configure(disabledforeground="#a3a3a3")
        self.cNameEntry1.configure(font="TkFixedFont")
        self.cNameEntry1.configure(foreground="#000000")
        self.cNameEntry1.configure(font=('Helvatical bold', 9))
        self.cNameEntry1.insert(0, "ex: BITCOIN")
        self.cNameEntry1.configure(state='disabled')
        focus_in = self.cNameEntry1.bind('<Button-1>', lambda x: self.on_focus_in(self.cNameEntry1))
        focus_out = self.cNameEntry1.bind(
        '<FocusOut>', lambda x: self.on_focus_out(self.cNameEntry1, 'ex: BITCOIN'))
        

        

        self.cKeyEntry1 = tk.Entry(self.top)
        self.cKeyEntry1.place(relx=0.07, rely=0.50, height=20, relwidth=0.080)
        self.cKeyEntry1.configure(background="white")
        self.cKeyEntry1.configure(cursor="fleur")
        self.cKeyEntry1.configure(disabledforeground="#a3a3a3")
        self.cKeyEntry1.configure(font="TkFixedFont")
        self.cKeyEntry1.configure(foreground="#000000")

        self.cKeyEntry1.insert(0, "ex: BTC")
        self.cKeyEntry1.configure(state='disabled')
        focus_in_key = self.cKeyEntry1.bind(
            '<Button-1>', lambda x: self.on_focus_in(self.cKeyEntry1))
        focus_out_key = self.cKeyEntry1.bind(
            '<FocusOut>', lambda x: self.on_focus_out(self.cKeyEntry1, 'ex: BTC'))

        # self.cKeyEntry1.configure(state=DISABLED)




        self.visualizeButton = tk.Button(self.top,command=self.visualizeAnyCrypto)
        self.visualizeButton.place(relx=0.026, rely=0.55, height=34, width=130)
        self.visualizeButton.configure(activebackground="#ececec")
        self.visualizeButton.configure(activeforeground="#000000")
        self.visualizeButton.configure(background="#d9d9d9")
        self.visualizeButton.configure(compound='left')
        self.visualizeButton.configure(disabledforeground="#a3a3a3")
        self.visualizeButton.configure(foreground="#000000")
        self.visualizeButton.configure(highlightbackground="#d9d9d9")
        self.visualizeButton.configure(highlightcolor="black")
        self.visualizeButton.configure(pady="0")
        self.visualizeButton.configure(text='''VISUALIZE''')



        self.Entry1 = DateEntry(crypto_support.root, width=16,
                                    bd=2, year=2020, month=2, day=15)
        # self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.173, rely=0.050, height=20, relwidth=0.097)
        self.Entry1.configure(background="white")
        self.Entry1.configure(cursor="fleur")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        # self.Entry1.configure(insertbackground="black")

        # self.Entry2 = tk.Entry(self.top)
        self.Entry2 = DateEntry(
            crypto_support.root, width=16, background="magenta3", foreground="white", bd=3)
        self.Entry2.place(relx=0.173, rely=0.106, height=20, relwidth=0.097)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        # self.Entry2.configure(insertbackground="black")

        # self.Button1 = tk.Button(self.top, command=self.bitcoin)
        self.Button1 = tk.Button(self.top, command=self.bitcoin)
        self.Button1.place(relx=0.405, rely=0.015, height=34, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''BITCOIN''')


        self.Button2 = tk.Button(self.top,command=self.etherium)
        self.Button2.place(relx=0.405, rely=0.09, height=34, width=87)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''ETHERIUM''')

        self.Button3 = tk.Button(self.top,command=self.loopring)
        self.Button3.place(relx=0.543, rely=0.015, height=34, width=77)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''LOOPRING''')

        self.Button4 = tk.Button(self.top,command=self.trx)
        self.Button4.place(relx=0.543, rely=0.09, height=34, width=77)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''TRX''')

        self.Button5 = tk.Button(self.top,command=self.polygon)
        self.Button5.place(relx=0.659, rely=0.015, height=34, width=67)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(compound='left')
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''POLYGON''')

        self.Button6 = tk.Button(self.top,command=self.cardano)
        self.Button6.place(relx=0.659, rely=0.09, height=34, width=67)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(compound='left')
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''CARDANO''')

        self.Button7 = tk.Button(self.top,command=self.dash)
        self.Button7.place(relx=0.763, rely=0.015, height=34, width=67)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(compound='left')
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''DASH''')

        self.Button8 = tk.Button(self.top,command=self.shib)
        self.Button8.place(relx=0.763, rely=0.09, height=34, width=67)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(compound='left')
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''SHIBA INU''')

        self.Button9 = tk.Button(self.top,command=self.doge)
        self.Button9.place(relx=0.867, rely=0.015, height=34, width=87)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(compound='left')
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''DOGE COIN''')

        self.Button10 = tk.Button(self.top,command=self.solana)
        self.Button10.place(relx=0.867, rely=0.09, height=34, width=87)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(compound='left')
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''SOLANA''')

        # self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        # top.configure(menu = self.menubar)

        

    def on_focus_in(self,entry):
        if entry.cget('state') == 'disabled':
            entry.configure(state='normal')
            entry.delete(0, 'end')


    def on_focus_out(self,entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(state='disabled')

    def visualizeAnyCrypto(self):
        self.start_end_date()
        global global_fig

        name=self.cNameEntry1.get().upper()+" price (USD)"
        if(name == "EX: BITCOIN price (USD)"):
            name=""
        key = self.cKeyEntry1.get().upper()+"-USD"
        if(key=="EX: BTC-USD"):
            key=""
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)
        try:
            data = web.DataReader(key, "yahoo", start, end)
            global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title=name, figratio=(20, 12))
            self.plot()
        except:
            messagebox.showinfo("showinfo", f" Error : '{key}' invalid coin symbol entered")



    def bitcoin(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)
        
        data = web.DataReader("BTC-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="BITCOIN price (USD)", figratio=(20, 12))
        self.plot()
        # fig, axlist = mpf.plot(ohlcv_datafra, figratio=(8, 5), returnfig=True)
    def doge(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)

        data = web.DataReader("DOGE-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="DOGE COIN price (USD)")
        self.plot()

    def etherium(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)

        data = web.DataReader("ETH-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="ETHERIUM price (USD)")
        self.plot()

    def dash(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)

        data = web.DataReader("DASH-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="DASH price (USD)")
        self.plot()

    def shib(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)

        data = web.DataReader("SHIB-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="SHIB INU price (USD)")
        self.plot()

    def solana(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)

        data = web.DataReader("SOL-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="SOLANA price (USD)")
        self.plot()

    def polygon(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)

        data = web.DataReader("MATIC-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="POLYGON price (USD)")
        self.plot()

    def cardano(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)

        data = web.DataReader("ADA-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="CARDANO price (USD)")
        self.plot()

    def trx(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)

        data = web.DataReader("TRX-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="TRX price (USD)")
        self.plot()

    def loopring(self):
        self.start_end_date()
        global global_fig
        global_fig = Figure(figsize=(8, 8),
                            dpi=100)

        data = web.DataReader("LRC-USD", "yahoo", start, end)
        global_fig, axlist = mpf.plot(data, type="candle", volume=True, returnfig=True,
                                      style="yahoo", title="LOOPRING price (USD)")
        self.plot()




    def start_end_date(self):
        global start
        global end
        start = self.Entry1.get()
        start = datetime.strptime(start, "%m/%d/%y")

        end = self.Entry2.get()
        end = datetime.strptime(end, "%m/%d/%y")


    def plot(self):
        # self.Canvas1.draw_idle()
        # self.Canvas1.delete()

        self.Canvas1.destroy()#deletes canvas

        self.Canvas1 = tk.Canvas(self.top)
        # self.Canvas1.place(relx=0.083, rely=0.153,
                        #    relheight=0.773, relwidth=0.851)
        self.Canvas1.place(relx=0.233, rely=0.153,
                           relheight=0.773, relwidth=0.741)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")


        plt.close(global_fig)
        # self.Canvas1.delete("all")
        global toolbar
        canvas = FigureCanvasTkAgg(global_fig, master=self.Canvas1)
        canvas.get_tk_widget().delete("all")

        # global_fig.canvas.draw_idle()
        global_fig.canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # for item in canvas.get_tk_widget().find_all():
        # canvas.get_tk_widget().delete(item)

        # placing the toolbar on the Tkinter window

        # creating the Matplotlib toolbar
        if toolbar is None:
            toolbar = NavigationToolbar2Tk(canvas, crypto_support.root)
            canvas.get_tk_widget().pack()
            toolbar.update()

        # toolbar = NavigationToolbar2Tk(canvas, self.Canvas1)



    # def main_coins_show(self):
    #     global global_fig
    #     self.start_end_date()
    #     currency = "USD"
    #     metric = "Close"

    #     crypto = ['BTC', 'ETH', 'LTC', 'XRP', 'DASH', 'SC']

    #     colnames = []

    #     first = True

    #     for ticker in crypto:
    #         data = web.DataReader(f"{ticker}-{currency}", "yahoo", start, end)
    #         if first:
    #             combined = data[[metric]].copy()
    #             colnames.append(ticker)
    #             combined.columns = colnames
    #             first = False
    #         else:
    #             combined = combined.join(data[metric])
    #             colnames.append(ticker)
    #             combined.columns = colnames

    #     plt.yscale('log')  # first show linear

    #     figure2 = plt.Figure(figsize=(10,9), dpi=100)
    #     ax2 = figure2.add_subplot(111)
    #     line2 = FigureCanvasTkAgg(figure2, self.Canvas1)
    #     ax2.set_title('Top Crypto Currency Coins')
    #     color=['r','g','b','c','m','y']
    #     i=0
    #     for ticker in crypto:
    #         # plt.plot(combined[ticker], label=ticker)
    #     # self.plot()

    #         line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #         mpf.plot(combined[ticker],type="canlde")
    #         # combined[ticker].plot(kind='line', legend=True, ax=ax2, color=color[i],marker='.', fontsize=14)
    #         i+=1

    #     # plt.legend(loc="upper right")

    #     toolbar = NavigationToolbar2Tk(line2, crypto_support.root)
    #     line2.get_tk_widget().pack()
    #     toolbar.update()

        # plt.legend(loc="upper right")
        # plt.show()



def start_up():
    crypto_support.main()

if __name__ == '__main__':
    crypto_support.main()





