from ast import Str
from cProfile import label
from calendar import c
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import sqlite3
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkinter import colorchooser
from configparser import ConfigParser
import tkinter as tk
import tkinter
from tkinter.ttk import Treeview
import json
from tokenize import String
#from typing_extensions import Self
import zipfile
from zipfile import ZipFile
#from django.forms import Input
import requests
import os
import pandas as pd
import re
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
import urllib.request
import io
from io import BytesIO
import functools
import operator
import shutil
import urllib.request as request
from contextlib import closing
from zipfile import ZipFile
import os
import sqlite3
import pandas as pd
from ttkwidgets.autocomplete import AutocompleteCombobox
from requests.structures import CaseInsensitiveDict
# # def Priceupdate():
# 	DLurl = 'https://www.pencarrie.com/api/public/v1/export/products.zip'
# 	o_file = 'products.zip' 
# 	userid = 'john.g@mpcembroidery.co.uk'
# 	password = 'Hapu12345!'
# 	s=requests.Session()
# 	cookies=s.cookies
# 	headers = {'User-Agent': 'Mozilla/5.0'}
# 	s.get(DLurl)

# 	soup = BeautifulSoup(s.get(DLurl).text, features="lxml")
# 	csrfToken = soup.find('meta', attrs={'name': 'csrf-token'})
	
# 	authenticity_token = csrfToken.get('content')	
# 	print(authenticity_token)
# 	payload = {
# 			'email': userid,
# 			'password': password,
# 			'_token': authenticity_token
# 			}


# 	headers = CaseInsensitiveDict()
# 	headers['User-Agent'] = 'Mozilla/5.0'
# 	headers["Accept"] = "application/json"
# 	headers["Authorization"] = "Bearer	eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDQ5N2Q4MzQ1OTQzYzUwNDhkNzVlY2NkMjU0YWMzYjIwYmIwNzYwOGU4YWI5ZmIyODExMjBkZDBjODU3ZGViNGFjZTY3MGU0YjQwZmMwOGMiLCJpYXQiOjE2NTc5NzcyOTEuMjUzMjU4LCJuYmYiOjE2NTc5NzcyOTEuMjUzMjYxLCJleHAiOjE2ODk1MTMyOTEuMjQ5MjIyLCJzdWIiOiI0MTY2Iiwic2NvcGVzIjpbXX0.MsI4xhdTWSXpOA2xVwmSNgEFrJR86ZXlopb7_X1P6Oq9EJsCQ9fYiaL1_7dKHG13jTmvzxeIELdwN4M1iWltM89ci6Wtx9p9B-tlLuuFCaQNeRzauo7OSjBnp1QuhRsSnY8RanE_NVcKNCXaHcLlcJPqN2GNQxpH35M_PS1ZGzIZVL5RhblbYozxMOQxE5siZMU0CZgpRZGcpZr_7yNHAAzZEojyH9_MdgouOLFnhArclegL9RgBAA-7bp20prv-0yeCqpC7vzSCRPgtIZE87vdQ_rqjehSwOwBq7vq0leQJTwnsicYquUtbe3DRFztJg9iLE_OLS8MraxlWUDVqbbsYgMhsynwjisBBXhpwGY3Sv4tEbOb8tTkOwIJGKZCcQqh3tmtzKQ1k2p6DZVxzpCCHHefYY4Bl2ut88npXUHpTYxDFVC-dwVpR_vaArw6bOYRxuZRECHMEs_Zmnf3X_H47d0X5fzwCAaHrVJJKJG38uzzFuVUYjzBA2vvJ-nzvZlDNVmObawo4owxgP4XWGtrbzSc9dABXLcAzh3M6Y7rGbTt1Nka35oicqyMjkQ6rNTJFq8nYk7I1ZHUdqZf1dBU4q9jqiydw9UJ6J2r8kbJQY47K0dMbGXHch8xo39FQuZch6TPti1RJsdEIMgqDZf0X_QOGT_et3aVGG7wju8E"
# 	r = requests.get(DLurl, data = payload, headers=headers)
# 	with open(o_file, 'wb') as f:
# 		for chunk in r.iter_content(chunk_size=1024):
# 			if chunk:
# 				f.write(chunk)
# 				f.flush()

# 	# DLurl = 'https://www.pencarrie.com/api/public/v1/export/products.zip'

# 	# o_file = 'products.zip' 
# 	# userid = 'john.g@mpcembroidery.co.uk'
# 	# password = 'Hapu12345!'

# 	# s=requests.Session()
# 	# cookies=s.cookies
# 	# headers = {'User-Agent': 'Mozilla/5.0'}

# 	# s.get(DLurl)

# 	# soup = BeautifulSoup(s.get(DLurl).text, features="lxml")
# 	# #csrfToken = soup.find('meta', attrs={'name': 'csrf-token'})
# 	# authenticity_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDQ5N2Q4MzQ1OTQzYzUwNDhkNzVlY2NkMjU0YWMzYjIwYmIwNzYwOGU4YWI5ZmIyODExMjBkZDBjODU3ZGViNGFjZTY3MGU0YjQwZmMwOGMiLCJpYXQiOjE2NTc5NzcyOTEuMjUzMjU4LCJuYmYiOjE2NTc5NzcyOTEuMjUzMjYxLCJleHAiOjE2ODk1MTMyOTEuMjQ5MjIyLCJzdWIiOiI0MTY2Iiwic2NvcGVzIjpbXX0.MsI4xhdTWSXpOA2xVwmSNgEFrJR86ZXlopb7_X1P6Oq9EJsCQ9fYiaL1_7dKHG13jTmvzxeIELdwN4M1iWltM89ci6Wtx9p9B-tlLuuFCaQNeRzauo7OSjBnp1QuhRsSnY8RanE_NVcKNCXaHcLlcJPqN2GNQxpH35M_PS1ZGzIZVL5RhblbYozxMOQxE5siZMU0CZgpRZGcpZr_7yNHAAzZEojyH9_MdgouOLFnhArclegL9RgBAA-7bp20prv-0yeCqpC7vzSCRPgtIZE87vdQ_rqjehSwOwBq7vq0leQJTwnsicYquUtbe3DRFztJg9iLE_OLS8MraxlWUDVqbbsYgMhsynwjisBBXhpwGY3Sv4tEbOb8tTkOwIJGKZCcQqh3tmtzKQ1k2p6DZVxzpCCHHefYY4Bl2ut88npXUHpTYxDFVC-dwVpR_vaArw6bOYRxuZRECHMEs_Zmnf3X_H47d0X5fzwCAaHrVJJKJG38uzzFuVUYjzBA2vvJ-nzvZlDNVmObawo4owxgP4XWGtrbzSc9dABXLcAzh3M6Y7rGbTt1Nka35oicqyMjkQ6rNTJFq8nYk7I1ZHUdqZf1dBU4q9jqiydw9UJ6J2r8kbJQY47K0dMbGXHch8xo39FQuZch6TPti1RJsdEIMgqDZf0X_QOGT_et3aVGG7wju8E'
# 	# payload = {
# 	# 		'email': userid,
# 	# 		'password': password
# 	# 		}
# 	# headers = {"Authorization": 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDQ5N2Q4MzQ1OTQzYzUwNDhkNzVlY2NkMjU0YWMzYjIwYmIwNzYwOGU4YWI5ZmIyODExMjBkZDBjODU3ZGViNGFjZTY3MGU0YjQwZmMwOGMiLCJpYXQiOjE2NTc5NzcyOTEuMjUzMjU4LCJuYmYiOjE2NTc5NzcyOTEuMjUzMjYxLCJleHAiOjE2ODk1MTMyOTEuMjQ5MjIyLCJzdWIiOiI0MTY2Iiwic2NvcGVzIjpbXX0.MsI4xhdTWSXpOA2xVwmSNgEFrJR86ZXlopb7_X1P6Oq9EJsCQ9fYiaL1_7dKHG13jTmvzxeIELdwN4M1iWltM89ci6Wtx9p9B-tlLuuFCaQNeRzauo7OSjBnp1QuhRsSnY8RanE_NVcKNCXaHcLlcJPqN2GNQxpH35M_PS1ZGzIZVL5RhblbYozxMOQxE5siZMU0CZgpRZGcpZr_7yNHAAzZEojyH9_MdgouOLFnhArclegL9RgBAA-7bp20prv-0yeCqpC7vzSCRPgtIZE87vdQ_rqjehSwOwBq7vq0leQJTwnsicYquUtbe3DRFztJg9iLE_OLS8MraxlWUDVqbbsYgMhsynwjisBBXhpwGY3Sv4tEbOb8tTkOwIJGKZCcQqh3tmtzKQ1k2p6DZVxzpCCHHefYY4Bl2ut88npXUHpTYxDFVC-dwVpR_vaArw6bOYRxuZRECHMEs_Zmnf3X_H47d0X5fzwCAaHrVJJKJG38uzzFuVUYjzBA2vvJ-nzvZlDNVmObawo4owxgP4XWGtrbzSc9dABXLcAzh3M6Y7rGbTt1Nka35oicqyMjkQ6rNTJFq8nYk7I1ZHUdqZf1dBU4q9jqiydw9UJ6J2r8kbJQY47K0dMbGXHch8xo39FQuZch6TPti1RJsdEIMgqDZf0X_QOGT_et3aVGG7wju8E'}

# 	# s.post(DLurl, data=payload, cookies=cookies, headers=headers )
# 	# r = s.get(DLurl)
# 	# with open(o_file, 'wb') as f:
# 	# 	for chunk in r.iter_content(chunk_size=1024):
# 	# 		if chunk:
# 	# 			f.write(chunk)
# 	# 			f.flush()

# 	# Create a ZipFile Object and load sample.zip in it
# 	with ZipFile('products.zip', 'r') as zipObj:
# 	# Extract all the contents of zip file in current directory
# 		zipObj.extractall()

# 	mydbfile="productdata.db"
# 	mycsvfile="PencarriePrices.csv"

# 	## If file exists, delete it ##
# 	if os.path.isfile(mycsvfile):
# 		os.remove(mycsvfile)

# 	os.rename("products.csv", "PencarriePrices.csv")

# 	if os.path.isfile(mydbfile):
# 		os.remove(mydbfile)

# 	conn = sqlite3.connect('productdata.db')
# 	c = conn.cursor()

# 	conn.commit()


def Priceupdate():
	URL = 'https://www.pencarrie.com/login'
	DLurl = 'https://www.pencarrie.com/export/products.zip'
	#payload = {'email':'john.g@mpcembroidery.co.uk','password':'Hapu12345!','redirect':'/'}
	o_file = 'products.zip' 
	userid = 'john.g@mpcembroidery.co.uk'
	password = 'Hapu12345!'


	s=requests.Session()
	cookies=s.cookies
	headers = {'User-Agent': 'Mozilla/5.0'}

	s.get(URL)

	soup = BeautifulSoup(s.get(URL).text, features="lxml")
	csrfToken = soup.find('meta', attrs={'name': 'csrf-token'})
	authenticity_token = csrfToken.get('content')
	payload = {
			'email': userid,
			'password': password,
			'_token': authenticity_token
			}
			
	s.post(URL, data=payload, cookies=cookies, headers=headers)
	r = s.get(DLurl)
	with open(o_file, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
				f.flush()

	# Create a ZipFile Object and load sample.zip in it
	with ZipFile('products.zip', 'r') as zipObj:
	# Extract all the contents of zip file in current directory
		zipObj.extractall()

	mydbfile="productdata.db"
	mycsvfile="PencarriePrices.csv"

	## If file exists, delete it ##
	if os.path.isfile(mycsvfile):
		os.remove(mycsvfile)

	os.rename("products.csv", "PencarriePrices.csv")

	if os.path.isfile(mydbfile):
		os.remove(mydbfile)

	conn = sqlite3.connect('productdata.db')
	c = conn.cursor()

	conn.commit()
	
def updateDatabase():
	df = pd.read_csv('PencarriePrices.csv',low_memory=False)
	# strip whitespace from headers
	df.columns = df.columns.str.strip()

	con = sqlite3.connect("productdata.db")
	# drop data into database
	df.to_sql("Pencarrie", con)

	with sqlite3.connect('productdata.db') as db:
		curr = db.cursor()
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Style Code` to `Style_Code`;")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Supplier Code` to `Supplier_Code`;")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Type` to `product_catergory`;")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Carton List Price` to `Carton_Price`;")
		curr.execute("ALTER TABLE Pencarrie ADD COLUMN `our_discounted_price` TEXT;")
		curr.execute("UPDATE Pencarrie SET our_discounted_price = 'Unavailable ATM';")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Body` to `Description_Body`;")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Front Image` to `image1`;")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Back Image` to `image2`;")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Side Image` to `image3`;")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `VAT Rate` to `VAT_Rate`;")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Colourway Name` to `Colourway_Name`;")
		curr.execute("ALTER TABLE Pencarrie RENAME COLUMN `Commodity Code` to `Commodity_Code`;")
		curr.execute("ALTER TABLE Pencarrie ADD COLUMN Supplier TEXT;")
		curr.execute("UPDATE Pencarrie SET Supplier = 'Pencarrie';")
		curr.execute("ALTER TABLE Pencarrie ADD COLUMN CodeColour TEXT;")
		curr.execute("UPDATE Pencarrie SET CodeColour = `Style_Code` || ' ' || `Colourway_Name`;")
		db.commit()



	con.close()
	
def BTCPriceupdate():
	o_file = 'ProductExport_mpc0001.zip' 

	with closing(request.urlopen('ftp://mpc0001:T5smB<+uMCyr@ftpdata.btcactivewear.co.uk/ProductExport_mpc0001.zip')) as r:    
		with open(o_file, 'wb') as f:
			shutil.copyfileobj(r, f)
        
		with ZipFile('ProductExport_mpc0001.zip', 'r') as zipObj:
   			# Extract all the contents of zip file in current directory
			zipObj.extractall()

			mycsvfile="BTCPrices.xlsx"

			## If file exists, delete it ##
			if os.path.isfile(mycsvfile):
				os.remove(mycsvfile)

			os.rename("ProductExport_mpc0001.xlsx", "BTCPrices.xlsx")

			conn = sqlite3.connect('productdata.db')
			c = conn.cursor()

			conn.commit()
			# load data
			df = pd.read_excel('BTCPrices.xlsx')
			# strip whitespace from headers
			df.columns = df.columns.str.strip()

			con = sqlite3.connect("productdata.db")
			# drop data into database
			df.to_sql("BTC", con)
				
			con.close()
			with sqlite3.connect('productdata.db') as db:
				curr = db.cursor()
				curr.execute("ALTER TABLE BTC RENAME COLUMN `Style Code` to `Supplier_Code`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN SPC to `Style_Code`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN Description to `Title`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `Colour Name` to `Colourway_Name`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `BTC Price` to `Carton List Price`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `Carton List Price` to `Carton_Price`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `Department` to `product_catergory`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `Customer Discounted Price` to `our_discounted_price`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `Bullet points` to `Description_Body`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `image_url_medium_res` to `image1`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `image_url_low_res` to `image2`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `image_url_high_res` to `image3`;")
				curr.execute("ALTER TABLE BTC RENAME COLUMN `VAT Code` to `VAT_Rate`;")
				curr.execute("ALTER TABLE BTC ADD COLUMN Material TEXT;")
				curr.execute("UPDATE BTC SET Material = 'Unavailable';")
				curr.execute("ALTER TABLE BTC ADD COLUMN Supplier TEXT;")
				curr.execute("UPDATE BTC SET Supplier = 'BTC';")
				curr.execute("ALTER TABLE BTC ADD COLUMN Commodity_Code TEXT;")
				curr.execute("UPDATE BTC SET Commodity_Code = 'Unavailable';")
				curr.execute("ALTER TABLE BTC ADD COLUMN CodeColour TEXT;")
				curr.execute("UPDATE BTC SET CodeColour = `Style_Code` || ' ' || `Colourway_Name`;")
				db.commit()

def Createdatabase():
	conn = sqlite3.connect('productdata.db')
	c = conn.cursor()

	c.execute('''
            CREATE TABLE IF NOT EXISTS products
            ([product_id] INTEGER PRIMARY KEY,
            [Style_Code] TEXT,
            [Brand] TEXT,
            [Colourway_Name] TEXT,
            [Size] TEXT,
            [Title] TEXT,
            [Carton_Price] REAL,
            [Our_discounted_Price] REAL,
            [VAT_Rate] REAL,
            [Supplier] TEXT,
            [Image1] TEXT,
            [Image2] TEXT,
            [Image3] TEXT,
            [Commodity_Code] TEXT,
            [Material] TEXT,
            [CodeColour] TEXT,
            [Supplier_Code] TEXT,
            [Product_Catergory] TEXT,
            [Description_Body] TEXT)
            ''')
	conn.commit
	c.close()
	conn.close()


	connection = sqlite3.connect("productdata.db")
	cursor = connection.cursor()

	Pencarrie_table = 'Pencarrie'
	target_table = 'products'

	Pencarrie = "INSERT INTO products(Style_Code, Brand, Colourway_Name, Size, Title, Carton_Price, Our_Discounted_Price, VAT_Rate, Supplier, Image1, Image2, Image3, Commodity_Code, Material, CodeColour, Supplier_Code, Product_Catergory, Description_Body) SELECT Style_Code, Brand, Colourway_Name, Size, Title, Carton_Price, Our_Discounted_Price, VAT_Rate, Supplier, Image1, Image2, Image3, Commodity_Code, Material, CodeColour, Supplier_Code, Product_Catergory, Description_Body FROM Pencarrie;"

	cursor.execute(Pencarrie)
	connection.commit()
	BTC = "INSERT INTO products(Style_Code, Brand, Colourway_Name, Size, Title, Carton_Price, Our_Discounted_Price, VAT_Rate, Supplier, Image1, Image2, Image3, Commodity_Code, Material, CodeColour, Supplier_Code, Product_Catergory, Description_Body) SELECT Style_Code, Brand, Colourway_Name, Size, Title, Carton_Price, Our_Discounted_Price, VAT_Rate, Supplier, Image1, Image2, Image3, Commodity_Code, Material, CodeColour, Supplier_Code, Product_Catergory, Description_Body FROM BTC;"
	cursor.execute(BTC)

	connection.commit()
	connection.close()

def printRecords():
	global z, count
	connection = sqlite3.connect('productdata.db')
	cur = connection.cursor()
	cur.execute("SELECT DISTINCT  `Style_Code`, Title, `Colourway_Name`, `Carton_Price`, Supplier  FROM Products WHERE `Style_Code` LIKE ?", (z.get(),))
	
	variablename = cur.fetchall()

	count = 0
	for row in variablename:
        #print(z)
		if count % 2 == 0:
			my_tree.insert("",tk.END,values=row, tags=('evenrow'))
		else:
			my_tree.insert("",tk.END,values=row, tags=('oddrow'))
		count += 1
	connection.commit()
	connection.close
   
def cleartreeview():
	x = my_tree.get_children()
	for item in x:
		my_tree.delete(item)

def primary_color():
	# Pick Color
	primary_color = colorchooser.askcolor()[1]

	# Update Treeview Color
	if primary_color:
		# Create Striped Row Tags
		my_tree.tag_configure('evenrow', background=primary_color)

		# Config file
		parser = ConfigParser()
		parser.read("treebase.ini")
		# Set the color change
		parser.set('colors', 'primary_color', primary_color)
		# Save the config file
		with open('treebase.ini', 'w') as configfile:
			parser.write(configfile)

def secondary_color():
	# Pick Color
	secondary_color = colorchooser.askcolor()[1]
	
	# Update Treeview Color
	if secondary_color:
		# Create Striped Row Tags
		my_tree.tag_configure('oddrow', background=secondary_color)
		
		# Config file
		parser = ConfigParser()
		parser.read("treebase.ini")
		# Set the color change
		parser.set('colors', 'secondary_color', secondary_color)
		# Save the config file
		with open('treebase.ini', 'w') as configfile:
			parser.write(configfile)

def highlight_color():
	# Pick Color
	highlight_color = colorchooser.askcolor()[1]

	#Update Treeview Color
	# Change Selected Color
	if highlight_color:
		style.map('Treeview',
			background=[('selected', highlight_color)])

		# Config file
		parser = ConfigParser()
		parser.read("treebase.ini")
		# Set the color change
		parser.set('colors', 'highlight_color', highlight_color)
		# Save the config file
		with open('treebase.ini', 'w') as configfile:
			parser.write(configfile)

def reset_colors():
	# Save original colors to config file
	parser = ConfigParser()
	parser.read('treebase.ini')
	parser.set('colors', 'primary_color', 'lightblue')
	parser.set('colors', 'secondary_color', 'white')
	parser.set('colors', 'highlight_color', '#347083')
	with open('treebase.ini', 'w') as configfile:
			parser.write(configfile)
	# Reset the colors
	my_tree.tag_configure('oddrow', background='white')
	my_tree.tag_configure('evenrow', background='lightblue')
	style.map('Treeview', background=[('selected', '#347083')])

def GetImageURL():
	global e ,ImageURl
	connection = sqlite3.connect('productdata.db')
	cur = connection.cursor()
	cur.execute("SELECT DISTINCT  `Image1` FROM Products WHERE `CodeColour` LIKE ?", (e.get(),))
	connection.commit()
	ImURl = cur.fetchall()
	stringURL = str(ImURl)
	#ImURl1 = (stringURL+ '1')
	
	ImageURl = stringURL.replace(',', '')
	ImageURl = ImageURl.replace("[('","")
	ImageURl = ImageURl.replace("')]","")


	#print(ImageURl)
	connection.close

def CreateOrderDatabase():
	conn = sqlite3.connect('.db')
	c = conn.cursor()

	c.execute('''
            CREATE TABLE IF NOT EXISTS products
            ([product_id] INTEGER PRIMARY KEY,
			[Order_Ref] TEXT,
            [Style_Code] TEXT,
            [Colourway_Name] TEXT,
            [Size] TEXT,
			[Quantity] INTEGER,
            [Title] TEXT,
            [Carton_Price] REAL,
            [Our_discounted_Price] REAL,
			[Sale_Price] REAL,
			[Decoration_Cost] REAL,
            [VAT_Rate] REAL,
            [Supplier] TEXT,
            [CodeColour] TEXT,
            [Supplier_Code] TEXT,
            ''')
	conn.commit
	c.close()
	conn.close()

def ViewOrder(event):
	global Selected_order, count, custref, Selected_order, CusLabel
	
	x = my_ordertree.get_children()
	for item in x:
		my_ordertree.delete(item)
	
	connection = sqlite3.connect('Orders.db')
	cur = connection.cursor()
	cur.execute("SELECT DISTINCT rowid, `Style_Code`, `Colourway_Name`, `Size`, Sell_Price, Quantity  FROM Orders WHERE `Orderref` LIKE ?", (Selected_order.get(),))
	
	variablename = cur.fetchall()

	count = 0
	for row in variablename:
        #print(z)
		if count % 2 == 0:
			my_ordertree.insert("",tk.END,values=row, tags=('evenrow'))
		else:
			my_ordertree.insert("",tk.END,values=row, tags=('oddrow'))
		count += 1
	connection.commit()
	connection.close

	
	connection = sqlite3.connect('Orders.db')
	cur = connection.cursor()
	cur.execute("SELECT DISTINCT `Customer_Ref` FROM Orders WHERE `Orderref` LIKE ?", (Selected_order.get(),))
	
	custref = cur.fetchall()
	custref= [i[0] for i in custref]
	my_customers = ""
	for mc in custref:
		my_customers += str(mc)+ " "

	


	#print(my_customers)
	
	
	
	connection.commit()
	connection.close

	CusLabel.destroy()
	CusLabel = Label(f4, text=("Customer: " + str(my_customers)))
	CusLabel.grid(row = 0, column = 0, sticky = 'e', padx=5)

def currentorders():
	global Orderrefs, Selected_order, w, CusLabel, custref
	connection = sqlite3.connect('Orders.db')
	cur = connection.cursor()
	cur.execute("SELECT DISTINCT  `Orderref` FROM Orders")
	Orderrefs = cur.fetchall()
	
	connection.commit()
	connection.close()
	Selected_order = tk.StringVar()
	connection.close()
	w.destroy()
	w = ttk.Combobox(f4, textvariable=Selected_order)
	
	# get first 3 letters of every month name
	w['values'] = Orderrefs

	# prevent typing a value
	w['state'] = 'readonly'


	w.bind('<<ComboboxSelected>>', ViewOrder)
	
	w.grid(row=0,column=2,sticky='e')

	CusLabel.destroy()
	CusLabel = Label(f4, textvariable=("Customer: " + str(custref)))
	CusLabel.grid(row = 0, column = 0, sticky = 'e', padx=5)

def clearordertree():
	for i in my_ordertree.get_children():
		my_ordertree.delete(i)

def remove_order():
	global Selected_order
	

	# Create a database or connect to one that exists
	conn = sqlite3.connect('Orders.db')

	# Create a cursor instance
	c = conn.cursor()

	# Delete From Database
	c.execute("DELETE from Orders WHERE Orderref like ?" , (Selected_order.get(),))
	


	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()

	# Clear The Entry Boxes
	clearordertree()

	#Update Order Menu
	currentorders()

	# Add a little message box for fun
	messagebox.showinfo("Deleted!", "Your Order Has Been Deleted!")

def remove_line_from_order():
	# Remove one record
	ln=StringVar()
	x = my_ordertree.selection()[0]
	
	selected = my_ordertree.focus()
	
	ln.set(my_ordertree.item(selected)['values'][0])
	#print(ln)
		
	# Create a database or connect to one that exists
	conn = sqlite3.connect('Orders.db')

	# Create a cursor instance
	c = conn.cursor()

	# Delete From Database
	sql = ("DELETE  from Orders WHERE oid =" + ln.get())
	c.execute(sql)


	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()

	my_ordertree.delete(x)
	

	# Add a little message box for fun
	messagebox.showinfo("Deleted!", "Your Item Has Been Deleted!")

def CRM():
	global Customer_Ref
	CRM = Tk()
	CRM.title('Customers')
	#CRM.iconbitmap('c:/gui/codemy.ico')
	CRM.geometry("1100x550")

	# Read our config file and get colors
	parser = ConfigParser()
	parser.read("treebase.ini")
	saved_primary_color = parser.get('colors', 'primary_color')
	saved_secondary_color = parser.get('colors', 'secondary_color')
	saved_highlight_color = parser.get('colors', 'highlight_color')


	def query_database():
		# Clear the Treeview
		for record in my_tree.get_children():
			my_tree.delete(record)
			
		# Create a database or connect to one that exists
		conn = sqlite3.connect('Customers_crm.db')

		# Create a cursor instance
		c = conn.cursor()

		c.execute("SELECT Customer_Ref, * FROM customers")
		records = c.fetchall()
		
		# Add our data to the screen
		global count
		count = 0
		
		#for record in records:
		#	print(record)


		for record in records:
			if count % 2 == 0:
				my_tree.insert(parent='', index='end', iid=count, text='', values=( record[1], record[2], record[3], record[4], record[5], record[6], record[7],record[8], record[9], record[10]), tags=('evenrow',))
			else:
				my_tree.insert(parent='', index='end', iid=count, text='', values=( record[1], record[2], record[3], record[4], record[5], record[6], record[7],record[8], record[9], record[10]), tags=('oddrow',))
			# increment counter
			count += 1


		# Commit changes
		conn.commit()

		# Close our connection
		conn.close()



	def search_records():
		lookup_record = search_entry.get()
		# close the search box
		search.destroy()
		
		# Clear the Treeview
		for record in my_tree.get_children():
			my_tree.delete(record)
		
		# Create a database or connect to one that exists
		conn = sqlite3.connect('Customers_crm.db')

		# Create a cursor instance
		c = conn.cursor()

		c.execute("SELECT rowid, * FROM customers WHERE last_name like ?", (lookup_record,))
		records = c.fetchall()
		
		# Add our data to the screen
		global count
		count = 0
		
		#for record in records:
		#	print(record)


		for record in records:
			if count % 2 == 0:
				my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7],record[8], record[9], record[10]), tags=('evenrow',))
			else:
				my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7],record[8], record[9], record[10]), tags=('oddrow',))
			# increment counter
			count += 1


		# Commit changes
		conn.commit()

		# Close our connection
		conn.close()



	def lookup_records():
		global search_entry, search

		search = Toplevel(CRM)
		search.title("Lookup Records")
		search.geometry("400x200")
		#search.iconbitmap('c:/gui/codemy.ico')

		# Create label frame
		search_frame = LabelFrame(search, text="Customer Reference")
		search_frame.pack(padx=10, pady=10)

		# Add entry box
		search_entry = Entry(search_frame, font=("Helvetica", 18))
		search_entry.pack(pady=20, padx=20)

		# Add button
		search_button = Button(search, text="Search Records", command=search_records)
		search_button.pack(padx=20, pady=20)



	def primary_color():
		# Pick Color
		primary_color = colorchooser.askcolor()[1]

		# Update Treeview Color
		if primary_color:
			# Create Striped Row Tags
			my_tree.tag_configure('evenrow', background=primary_color)

			# Config file
			parser = ConfigParser()
			parser.read("treebase.ini")
			# Set the color change
			parser.set('colors', 'primary_color', primary_color)
			# Save the config file
			with open('treebase.ini', 'w') as configfile:
				parser.write(configfile)


	def secondary_color():
		# Pick Color
		secondary_color = colorchooser.askcolor()[1]
		
		# Update Treeview Color
		if secondary_color:
			# Create Striped Row Tags
			my_tree.tag_configure('oddrow', background=secondary_color)
			
			# Config file
			parser = ConfigParser()
			parser.read("treebase.ini")
			# Set the color change
			parser.set('colors', 'secondary_color', secondary_color)
			# Save the config file
			with open('treebase.ini', 'w') as configfile:
				parser.write(configfile)

	def highlight_color():
		# Pick Color
		highlight_color = colorchooser.askcolor()[1]

		#Update Treeview Color
		# Change Selected Color
		if highlight_color:
			style.map('Treeview',
				background=[('selected', highlight_color)])

			# Config file
			parser = ConfigParser()
			parser.read("treebase.ini")
			# Set the color change
			parser.set('colors', 'highlight_color', highlight_color)
			# Save the config file
			with open('treebase.ini', 'w') as configfile:
				parser.write(configfile)

	def reset_colors():
		# Save original colors to config file
		parser = ConfigParser()
		parser.read('treebase.ini')
		parser.set('colors', 'primary_color', 'lightblue')
		parser.set('colors', 'secondary_color', 'white')
		parser.set('colors', 'highlight_color', '#347083')
		with open('treebase.ini', 'w') as configfile:
				parser.write(configfile)
		# Reset the colors
		my_tree.tag_configure('oddrow', background='white')
		my_tree.tag_configure('evenrow', background='lightblue')
		style.map('Treeview',
				background=[('selected', '#347083')])

	# Add Menu
	my_menu = Menu(CRM)
	CRM.config(menu=my_menu)



	# Configure our menu
	option_menu = Menu(my_menu, tearoff=0)
	my_menu.add_cascade(label="Options", menu=option_menu)
	# Drop down menu
	option_menu.add_command(label="Primary Color", command=primary_color)
	option_menu.add_command(label="Secondary Color", command=secondary_color)
	option_menu.add_command(label="Highlight Color", command=highlight_color)
	option_menu.add_separator()
	option_menu.add_command(label="Reset Colors", command=reset_colors)
	option_menu.add_separator()
	option_menu.add_command(label="Exit", command=CRM.quit)

	#Search Menu
	search_menu = Menu(my_menu, tearoff=0)
	my_menu.add_cascade(label="Search", menu=search_menu)
	# Drop down menu
	search_menu.add_command(label="Search", command=lookup_records)
	search_menu.add_separator()
	search_menu.add_command(label="Reset", command=query_database)

	# Add Fake Data
	'''
	data = [
		
		
	]
	'''

	# Do some database stuff
	# Create a database or connect to one that exists
	conn = sqlite3.connect('Customers_crm.db')

	# Create a cursor instance
	c = conn.cursor()

	# Create Table
	c.execute("""CREATE TABLE if not exists customers (
		Customer_Ref text,
		Company_name,
		first_name text,
		last_name text,
		address text,
		city text,
		county text,
		postcode text,
		email text,
		phone text)
		""")
	# Add dummy data to table
	'''
	for record in data:
		c.execute("INSERT INTO customers VALUES (:Customer_Ref, :Company_name, :first_name, :last_name, :address, :city, :county, :postcode, :email, :phone)", 
			{
			'Customer_Ref': record[1],
			'Company_name': record[2],
			'first_name': record[3],
			'last_name': record[4],
			'address': record[5],
			'city': record[6],
			'county': record[7],
			'postcode': record[8],
			'email': record[9],
			'phone': record[10]
			}
			)
	'''


	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()



	# Add Some Style
	style = ttk.Style()

	# Pick A Theme
	style.theme_use('default')

	# Configure the Treeview Colors
	style.configure("Treeview",
		background="#D3D3D3",
		foreground="black",
		rowheight=25,
		fieldbackground="#D3D3D3")

	# Change Selected Color #347083
	style.map('Treeview',
		background=[('selected', saved_highlight_color)])

	# Create a Treeview Frame
	tree_frame = Frame(CRM)
	tree_frame.pack(pady=10)

	# Create a Treeview Scrollbar
	tree_scroll = Scrollbar(tree_frame)
	tree_scroll.pack(side=RIGHT, fill=Y)

	# Create The Treeview
	my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
	my_tree.pack()

	# Configure the Scrollbar
	tree_scroll.config(command=my_tree.yview)

	# Define Our Columns
	my_tree['columns'] = ( "Customer Ref","Company Name", "First Name", "Last Name", "Address", "City", "County", "postcode", "Email", "Phone")

	# Format Our Columns
	my_tree.column("#0", width=0, stretch=NO)
	my_tree.column("Customer Ref", anchor=W, width=80)
	my_tree.column("Company Name", anchor=W, width=140)
	my_tree.column("First Name", anchor=W, width=100)
	my_tree.column("Last Name", anchor=W, width=100)
	my_tree.column("Address", anchor=CENTER, width=140)
	my_tree.column("City", anchor=CENTER, width=100)
	my_tree.column("County", anchor=CENTER, width=100)
	my_tree.column("postcode", anchor=CENTER, width=80)
	my_tree.column("Email", anchor=CENTER, width=140)
	my_tree.column("Phone", anchor=CENTER, width=80)

	# Create Headings
	my_tree.heading("#0", text="", anchor=W)
	my_tree.heading("Customer Ref", text="Customer Ref", anchor=W)
	my_tree.heading("Company Name", text="Company Name", anchor=W)
	my_tree.heading("First Name", text="First Name", anchor=W)
	my_tree.heading("Last Name", text="Last Name", anchor=W)
	my_tree.heading("Address", text="Address", anchor=CENTER)
	my_tree.heading("City", text="City", anchor=CENTER)
	my_tree.heading("County", text="County", anchor=CENTER)
	my_tree.heading("postcode", text="Postcode", anchor=CENTER)
	my_tree.heading("Email", text="Email", anchor=CENTER)
	my_tree.heading("Phone", text="Phone", anchor=CENTER)

	# Create Striped Row Tags
	my_tree.tag_configure('oddrow', background=saved_secondary_color)
	my_tree.tag_configure('evenrow', background=saved_primary_color)



	# Add Record Entry Boxes
	data_frame = LabelFrame(CRM, text="Record")
	data_frame.pack(fill="x", expand="yes", padx=25)

	Customerref_label = Label(data_frame, text="Customer Ref")
	Customerref_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
	Customerref_entry = Entry(data_frame, width = 25)
	Customerref_entry.grid(row=0, column=1, padx=10, pady=10)

	Companyname_label = Label(data_frame, text="Company")
	Companyname_label.grid(row=0, column=2, padx=10, pady=10, sticky='w')
	Companyname_entry = Entry(data_frame, width = 25)
	Companyname_entry.grid(row=0, column=3, padx=10, pady=10)

	fn_label = Label(data_frame, text="First Name")
	fn_label.grid(row=0, column=4, padx=10, pady=10, sticky='w')
	fn_entry = Entry(data_frame, width = 25)
	fn_entry.grid(row=0, column=5, padx=10, pady=10)

	ln_label = Label(data_frame, text="Last Name")
	ln_label.grid(row=0, column=6, padx=10, pady=10, sticky='w')
	ln_entry = Entry(data_frame, width = 25)
	ln_entry.grid(row=0, column=7, padx=10, pady=10)

	address_label = Label(data_frame, text="Address")
	address_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
	address_entry = Entry(data_frame, width = 25)
	address_entry.grid(row=1, column=1, padx=10, pady=10)

	city_label = Label(data_frame, text="City")
	city_label.grid(row=1, column=2, padx=10, pady=10, sticky='w')
	city_entry = Entry(data_frame, width = 25)
	city_entry.grid(row=1, column=3, padx=10, pady=10)

	county_label = Label(data_frame, text="County")
	county_label.grid(row=1, column=4, padx=10, pady=10, sticky='w')
	county_entry = Entry(data_frame, width = 25)
	county_entry.grid(row=1, column=5, padx=10, pady=10)

	postcode_label = Label(data_frame, text="Postcode")
	postcode_label.grid(row=1, column=6, padx=10, pady=10, sticky='w')
	postcode_entry = Entry(data_frame, width = 25)
	postcode_entry.grid(row=1, column=7, padx=10, pady=10)

	email_label = Label(data_frame, text="Email")
	email_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
	email_entry = Entry(data_frame, width = 25)
	email_entry.grid(row=2, column=1, padx=10, pady=10)

	phone_label = Label(data_frame, text="Phone")
	phone_label.grid(row=2, column=2, padx=10, pady=10, sticky='w')
	phone_entry = Entry(data_frame, width = 25)
	phone_entry.grid(row=2, column=3, padx=10, pady=10)

	# Move Row Up
	def up():
		rows = my_tree.selection()
		for row in rows:
			my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

	# Move Rown Down
	def down():
		rows = my_tree.selection()
		for row in reversed(rows):
			my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)



	# Remove one record
	def remove_one():
		x = my_tree.selection()[0]
		my_tree.delete(x)

		# Create a database or connect to one that exists
		conn = sqlite3.connect('Customers_crm.db')

		# Create a cursor instance
		c = conn.cursor()

		# Delete From Database
		c.execute("DELETE from customers WHERE Customer_Ref = ?" , (Customerref_entry.get(),))
		


		# Commit changes
		conn.commit()

		# Close our connection
		conn.close()

		# Clear The Entry Boxes
		clear_entries()

		# Add a little message box for fun
		messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")



	# Remove Many records
	def remove_many():
		# Add a little message box for fun
		response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")

		#Add logic for message box
		if response == 1:
			# Designate selections
			x = my_tree.selection()

			# Create List of ID's
			ids_to_delete = []
			
			# Add selections to ids_to_delete list
			for record in x:
				ids_to_delete.append(my_tree.item(record, 'values')[1])

			# Delete From Treeview
			for record in x:
				my_tree.delete(record)

			# Create a database or connect to one that exists
			conn = sqlite3.connect('Customers_crm.db')

			# Create a cursor instance
			c = conn.cursor()
			

			# Delete Everything From The Table
			c.executemany("DELETE FROM customers WHERE Customer_Ref = ?", [(a,) for a in ids_to_delete])

			# Reset List
			ids_to_delete = []


			# Commit changes
			conn.commit()

			# Close our connection
			conn.close()

			# Clear entry boxes if filled
			clear_entries()


	# Remove all records
	def remove_all():
		# Add a little message box for fun
		response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING From The Table\nAre You Sure?!")

		#Add logic for message box
		if response == 1:
			# Clear the Treeview
			for record in my_tree.get_children():
				my_tree.delete(record)

			# Create a database or connect to one that exists
			conn = sqlite3.connect('Customers_crm.db')

			# Create a cursor instance
			c = conn.cursor()

			# Delete Everything From The Table
			c.execute("DROP TABLE customers")
				


			# Commit changes
			conn.commit()

			# Close our connection
			conn.close()

			# Clear entry boxes if filled
			clear_entries()

			# Recreate The Table
			create_table_again()

	# Clear entry boxes
	def clear_entries():
		# Clear entry boxes
		Customerref_entry.delete(0, END)
		Companyname_entry.delete(0,END)
		fn_entry.delete(0, END)
		ln_entry.delete(0, END)
		address_entry.delete(0, END)
		city_entry.delete(0, END)
		county_entry.delete(0, END)
		postcode_entry.delete(0, END)
		email_entry.delete(0, END)
		phone_entry.delete(0, END)


	# Select Record
	def select_record(e):
		# Clear entry boxes
		Customerref_entry.delete(0, END)
		Companyname_entry.delete(0,END)
		fn_entry.delete(0, END)
		ln_entry.delete(0, END)
		address_entry.delete(0, END)
		city_entry.delete(0, END)
		county_entry.delete(0, END)
		postcode_entry.delete(0, END)
		email_entry.delete(0, END)
		phone_entry.delete(0, END)

		# Grab record Number
		selected = my_tree.focus()
		# Grab record values
		values = my_tree.item(selected, 'values')

		# outpus to entry boxes
		Customerref_entry.insert(0, values[0])
		Companyname_entry.insert(0, values[1])
		fn_entry.insert(0, values[2])
		ln_entry.insert(0, values[3])
		address_entry.insert(0, values[4])
		city_entry.insert(0, values[5])
		county_entry.insert(0, values[6])
		postcode_entry.insert(0, values[7])
		email_entry.insert(0, values[8])
		phone_entry.insert(0, values[9])

	# Update record
	def update_record():
		# Grab the record number
		selected = my_tree.focus()
		# Update record
		my_tree.item(selected, text="", values=(Customerref_entry.get(), Companyname_entry.get(), fn_entry.get(), ln_entry.get(), address_entry.get(), city_entry.get(), county_entry.get(), postcode_entry.get(), email_entry.get(),phone_entry.get(),))

		# Update the database
		# Create a database or connect to one that exists
		conn = sqlite3.connect('Customers_crm.db')

		# Create a cursor instance
		c = conn.cursor()

		c.execute("""UPDATE customers SET
			Company_name= :Company_name,
			first_name = :first,
			last_name = :last,
			address = :address,
			city = :city,
			county = :county,
			postcode = :postcode,
			email = :email,
			phone = :phone
			WHERE Customer_Ref = :Customer_Ref
			""",
			{
				'Customer_Ref': Customerref_entry.get(),
				'Company_name': Companyname_entry.get(),
				'first': fn_entry.get(),
				'last': ln_entry.get(),
				'address': address_entry.get(),
				'city': city_entry.get(),
				'county': county_entry.get(),
				'postcode': postcode_entry.get(),
				'email': email_entry.get(),
				'phone': phone_entry.get(),
			})
		


		# Commit changes
		conn.commit()

		# Close our connection
		conn.close()


		# Clear entry boxes
		Customerref_entry.delete(0, END)
		Companyname_entry.delete(0,END)
		fn_entry.delete(0, END)
		ln_entry.delete(0, END)
		address_entry.delete(0, END)
		city_entry.delete(0, END)
		county_entry.delete(0, END)
		postcode_entry.delete(0, END)
		email_entry.delete(0, END)
		phone_entry.delete(0, END)

	# add new record to database
	def add_record():
		# Update the database
		# Create a database or connect to one that exists
		conn = sqlite3.connect('Customers_crm.db')

		# Create a cursor instance
		c = conn.cursor()

		# Add New Record
		c.execute("INSERT INTO customers VALUES (:Customer_Ref, :Company_name, :first_name, :last_name, :address, :city, :county, :postcode, :email, :phone)", 
			{
				'Customer_Ref': Customerref_entry.get(),
				'Company_name': Companyname_entry.get(),
				'first_name': fn_entry.get(),
				'last_name': ln_entry.get(),
				'address': address_entry.get(),
				'city': city_entry.get(),
				'county': county_entry.get(),
				'postcode': postcode_entry.get(),
				'email': email_entry.get(),
				'phone': phone_entry.get()
				
			})
		

		# Commit changes
		conn.commit()

		# Close our connection
		conn.close()

		# Clear entry boxes
		Customerref_entry.delete(0, END)
		Companyname_entry.delete(0,END)
		fn_entry.delete(0, END)
		ln_entry.delete(0, END)
		address_entry.delete(0, END)
		city_entry.delete(0, END)
		county_entry.delete(0, END)
		postcode_entry.delete(0, END)
		email_entry.delete(0, END)
		phone_entry.delete(0, END)

		# Clear The Treeview Table
		my_tree.delete(*my_tree.get_children())

		# Run to pull data from database on start
		query_database()

	def create_table_again():
		# Create a database or connect to one that exists
		conn = sqlite3.connect('Customers_crm.db')

		# Create a cursor instance
		c = conn.cursor()

		# Create Table
		c.execute("""CREATE TABLE if not exists customers (
			Customer_Ref text,
			Company_name, text,
			first_name text,
			last_name text,
			address text,
			city text,
			county text,
			postcode text,
			email text,
			phone text
			)
			""")
		
		# Commit changes
		conn.commit()

		# Close our connection
		conn.close()

	# Add Buttons
	button_frame = LabelFrame(CRM, text="Commands")
	button_frame.pack(fill="x", expand="yes", padx=20)

	update_button = Button(button_frame, text="Update Record", command=update_record)
	update_button.grid(row=0, column=0, padx=10, pady=10)

	add_button = Button(button_frame, text="Add Record", command=add_record)
	add_button.grid(row=0, column=1, padx=10, pady=10)

	remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
	remove_all_button.grid(row=0, column=2, padx=10, pady=10)

	remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
	remove_one_button.grid(row=0, column=3, padx=10, pady=10)

	remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
	remove_many_button.grid(row=0, column=4, padx=10, pady=10)

	move_up_button = Button(button_frame, text="Move Up", command=up)
	move_up_button.grid(row=0, column=5, padx=10, pady=10)

	move_down_button = Button(button_frame, text="Move Down", command=down)
	move_down_button.grid(row=0, column=6, padx=10, pady=10)

	select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
	select_record_button.grid(row=0, column=7, padx=10, pady=10)

	# Bind the treeview
	my_tree.bind("<ButtonRelease-1>", select_record)

	# Run to pull data from database on start
	query_database()

	CRM.mainloop()

def CopyOrder(event):
	global Selected_order2, Addorder, Customrefs2, Addcustomer, mycust, SC

	Addorder.delete(0, END)
	od= Selected_order2.get()
	#print(od)
	Addorder.insert(0, od)
	
	#get Customer Ref from Order Number
	
	connection = sqlite3.connect('Orders.db')
	cur = connection.cursor()
	cur.execute("SELECT DISTINCT `Customer_Ref` FROM Orders WHERE `Orderref` = ?", (Selected_order2.get(),))
	mycustomer = cur.fetchall()
	connection.commit()
	connection.close()
	mycust=str()
	
	mycustomer= [i[0] for i in mycustomer]
	mycust = ""
	for mc in mycustomer:
		mycust += str(mc)+ ""
	
	print(mycust)

	Addcustomer.delete(0, END)
	Addcustomer.insert(0, mycust)
	#Addcustomer = Entry(info_frame, text=(str(mycust)))
	

def CopyCustomer(event):
	global Selected_Customer, Addcustomer, SC, mycust
	Addcustomer.delete(0, END)
	oc=mycust.get()
	Addcustomer.insert(0, oc)
	
	

def selector():
	global c, d, e ,f ,g ,h
	c=StringVar()
	d=StringVar()
	e=StringVar()
	selected = my_tree.selection()
	for row in selected:
		# Grab record values
		c.set (my_tree.item(selected)['values'][0])
		d.set (my_tree.item(selected)['values'][2])
		f=(my_tree.item(selected)['values'][0])
		g=(my_tree.item(selected)['values'][1])
		h=(my_tree.item(selected)['values'][2])
		f=str(f)
		g=str(g)
		h=str(h)
		e.set (c.get() + " " + d.get())

def Close():
	global p
	p.destroy()

def addtoorder():
	global all_entries, mycust , quantity,SC, Addcustomer, e, orderref, Addorder, SO, z, d, Selected_Customer, sellprice, size, all_sizes, q, s, all_prices, all_labels, sizelabel, c, Customer_Ref
	thecust = SC.get()
	#SC = SC.replace(" ", "_")
	
	#print(SC)
	orderref = SO.get()
	orderref = orderref.replace(" ", "_")
	#print(orderref)
	all_prices=all_prices[e.get()].items()
	all_entries= all_entries[e.get()].items()

	conn = sqlite3.connect('Orders.db')
	newcon = conn.cursor()

	newcon.execute('''CREATE TABLE IF NOT EXISTS Orders

					(
					[Customer_Ref] TEXT,
					[Orderref] TEXT,
					[Style_Code] TEXT,
					[Colourway_Name] TEXT,
					[Size] TEXT,
					[Sell_Price] REAL,
					[Quantity] INTEGER)
					''')
	
	my_order = []
	for prices,entries in zip(all_prices,all_entries):
		y = prices[1].get()        
		x = entries[1].get()
		
		sell=thecust, orderref, c.get(), d.get(), prices[0] , y, x
		my_order.append(sell)

	#print(my_order)
	conn.commit
	newcon.close()
	conn.close()
	

	connection = sqlite3.connect("Orders.db")
	cursor = connection.cursor()
		
	
	for record in my_order:
		cursor.execute("INSERT INTO orders VALUES (:Customer_Ref, :Orderref, :Style_Code, :Colourway_Name, :Size, :Sell_Price, :Quantity)", 
		{
		'Customer_Ref': record[0],
		'Orderref': record[1],
		'Style_Code': record[2],
		'Colourway_Name': record[3],
		'Size': record[4],
		'Sell_Price': record[5],
		'Quantity': record[6]
		}
		)
	

	connection.commit()

	connection.close()

	conn = sqlite3.connect('Orders.db')

	# Create a cursor instance
	c = conn.cursor()

	# Delete From Database
	c.execute("DELETE from Orders WHERE Quantity like '0'")
	
	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()

	
	
	

conn = sqlite3.connect('Orders.db')
newcon = conn.cursor()

newcon.execute('''CREATE TABLE IF NOT EXISTS Orders

					([Customer_Ref] TEXT,
					[Orderref] TEXT,
					[Style_Code] TEXT,
					[Colourway_Name] TEXT,
					[Size] TEXT,
					[Sell_Price] REAL,
					[Quantity] INTEGER)
					''')

conn.commit()
newcon.close()
conn.close()

root = Tk()
global z, Selected_order, Orderrefs, custref

root.title ( "Search a Product")
root.geometry("1100x370+150+50")
#root.state('zoomed')
root.configure(background='#D3D3D3')

#root.iconbitmap('c:/gui/codemy.ico')
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
#f1.rowconfigure(2, weight=1)

f1 = tk.Frame(root)
f1.grid(column=1, row=0,  sticky='ne', padx=10)
f1.columnconfigure(0 , weight=1)
f1.rowconfigure(1, weight=1)


f2 = tk.Frame(root)
f2.grid(column=1, row=1, sticky="ne", padx=10)
f2.columnconfigure(0 , weight=1)
f2.rowconfigure(0, weight=1)

f3 = tk.Frame(root)
f3.grid(column=0, row=1, sticky="nw", padx=10)
f3.columnconfigure(0 , weight=1)
f3.rowconfigure(0, weight=1)

f4 = tk.Frame(root)
f4.grid(column=0, row=0, sticky="nw", padx=10)
f4.columnconfigure(0 , weight=1)
f4.rowconfigure(0, weight=1)

f5 = tk.Frame(root)
f5.grid(column=0, row=2, sticky="nw", padx=10)
f5.columnconfigure(0 , weight=1)
f5.rowconfigure(0, weight=1)

# Read our config file and get colors
parser = ConfigParser()
configFilePath = 'treebase.ini'
parser.read(configFilePath)
saved_primary_color = parser.get('colors', 'primary_color')
saved_secondary_color = parser.get('colors', 'secondary_color')
saved_highlight_color = parser.get('colors', 'highlight_color')


# Add Menu
Menu_bar = Menu(root)


# Configure our menu
option_menu = Menu(Menu_bar, tearoff=0)
customer_menu = Menu(Menu_bar, tearoff=0)
order_menu = Menu(Menu_bar,tearoff=0)
Menu_bar.add_cascade(label="Orders", menu=order_menu)
Menu_bar.add_cascade(label="Customers", menu=customer_menu)
Menu_bar.add_cascade(label="Options", menu=option_menu)

#Customer down menu
customer_menu.add_command(label="Customers", command=CRM)


#Order menu
order_menu.add_command(label="New Order")

# Options down menu
option_menu.add_command(label="Primary Colour", command=primary_color)
option_menu.add_command(label="Secondary Colour", command=secondary_color)
option_menu.add_command(label="Highlight Colour", command=highlight_color)
option_menu.add_separator()
option_menu.add_command(label="Reset Colours", command=reset_colors)
option_menu.add_separator()
option_menu.add_command(label="Update Prices", command=lambda:[Priceupdate(),updateDatabase(),BTCPriceupdate(),Createdatabase()])
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)

root.config(menu=Menu_bar)
#Search Menu
#search_menu = Menu(my_menu, tearoff=0)
#my_menu.add_cascade(label="Update Pencarrie Prices", menu=search_menu)
# Drop down menu

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=20,
	fieldbackground="#D3D3D3")

# Change Selected Color #347083
style.map('Treeview',
	background=[('selected', saved_highlight_color)])



z= StringVar()
# Create a Treeview Frame
tree_frame = Frame(f2)
tree_frame.pack(expand=True, fill='both')

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)
# Define Our Columns
my_tree['columns'] = ("Style Code", "Description", "Colour", "Carton Price", "Supplier")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Style Code", anchor=W, width=100, stretch=YES)
#my_tree.column("Index", width=0, stretch=NO)
my_tree.column("Description", anchor=W, width=220, stretch=YES)
my_tree.column("Colour", anchor=W, width=140, stretch=YES)
#my_tree.column("Sizes", anchor=CENTER, width=50, stretch=YES)
my_tree.column("Carton Price", anchor=CENTER, width=70, stretch=YES)
my_tree.column("Supplier", anchor=CENTER, width=70, stretch=YES)
#my_tree.column("VAT code", anchor=CENTER, width=40, stretch=YES)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Style Code", text="Style Code", anchor=W)
#my_tree.heading("Index", text="", anchor=W)
my_tree.heading("Description", text="Description", anchor=W)
my_tree.heading("Colour", text="Colour", anchor=W)
#my_tree.heading("Sizes", text="Sizes", anchor=CENTER)
my_tree.heading("Carton Price", text="Carton Price", anchor=CENTER)
my_tree.heading("Supplier", text="Supplier", anchor=CENTER)

#my_tree.heading("VAT code", text="VAT code", anchor=CENTER)


# Create Striped Row Tags
my_tree.tag_configure('oddrow', background=saved_secondary_color)
my_tree.tag_configure('evenrow', background=saved_primary_color)

ordertree_frame = Frame(f3)
# Create a Treeview Frame

ordertree_frame.pack(expand=True, fill='both')

# Create a Treeview Scrollbar
ordertree_scroll = Scrollbar(ordertree_frame)
ordertree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_ordertree = ttk.Treeview(ordertree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_ordertree.pack()

# Configure the Scrollbar
ordertree_scroll.config(command=my_ordertree.yview)
# Define Our Columns
my_ordertree['columns'] = ("ID", "Style Code", "Colour", "Size" ,  "Sell Price",  "Quantity")

# Format Our Columns2
my_ordertree.column("ID", width=0, stretch=NO)
my_ordertree.column("Style Code", anchor=W, width=60, stretch=YES)
my_ordertree.column("#0", width=0, stretch=NO)
#my_ordertree.column("Description", anchor=W, width=150, stretch=YES)
my_ordertree.column("Colour", anchor=W, width=140, stretch=YES)
my_ordertree.column("Size", anchor=CENTER, width=50, stretch=YES)
my_ordertree.column("Sell Price", anchor=CENTER, width=70, stretch=YES)
my_ordertree.column("Quantity", anchor=CENTER, width=70, stretch=YES)
#my_ordertree.column("VAT code", anchor=CENTER, width=40, stretch=YES)

# Create Headings
my_ordertree.heading("ID", text="ID", anchor=W)
my_ordertree.heading("Style Code", text="Style Code", anchor=W)
my_ordertree.heading("#0", text="", anchor=W)
#my_ordertree.heading("Description", text="Description", anchor=W)
my_ordertree.heading("Colour", text="Colour", anchor=W)
my_ordertree.heading("Size", text="Size", anchor=CENTER)
my_ordertree.heading("Sell Price", text="Sell Price", anchor=CENTER)
my_ordertree.heading("Quantity", text="Quantity", anchor=CENTER)

#my_ordertree.heading("VAT code", text="VAT code", anchor=CENTER)


# Create Striped Row Tags
my_ordertree.tag_configure('oddrow', background=saved_secondary_color)
my_ordertree.tag_configure('evenrow', background=saved_primary_color)

#Dropdown order selector
#Query all orders and return distinct orderref
connection = sqlite3.connect('Orders.db')
cur = connection.cursor()
cur.execute("SELECT DISTINCT  `Orderref` FROM Orders")
Orderrefs = cur.fetchall()

connection.commit()
connection.close()
Selected_order = tk.StringVar()
connection.close()

w = ttk.Combobox(f4, textvariable=Selected_order)
w.pack_forget()

w['values'] = Orderrefs

# prevent typing a value
w['state'] = 'readonly'


w.bind('<<ComboboxSelected>>', ViewOrder)

w.grid(row=0,column=2,sticky='e')
Label(f4, text = "Select Order:").grid(row = 0, column = 1, sticky = 'e', padx=5)

connection = sqlite3.connect('Orders.db')
cur = connection.cursor()
cur.execute("SELECT DISTINCT `Customer_Ref` FROM Orders WHERE `Orderref` LIKE ?", (Selected_order.get(),))

custref = cur.fetchall()


connection.commit()
connection.close

CusLabel = Label(f4, text=("Customer:   " ))
CusLabel.grid(row = 0, column = 0, sticky = 'e', padx=5)

#Button frame f5 items

DeleteOrderButton = Button(f5, text = "Delete Selected Order", command = lambda:[clearordertree(), remove_order()])
DeleteOrderButton.grid(row=0, column=0, sticky='w')


DeleteLineButton = Button(f5, text = "Delete Selected Line", command = remove_line_from_order)
DeleteLineButton.grid(row=0, column=1, sticky='e')





#Label
Label(f1, text = "Enter the Product Code you are searching for:      ").grid(row = 0, column = 0, sticky = 'e')
#Textbox
bookSearchEntry = Entry(f1, textvariable = z)
bookSearchEntry.bind('<Return>', lambda _:[cleartreeview(),printRecords()])
bookSearchEntry.grid(row = 0, column = 1 , sticky= 'w')
#Button
bookSearchButton = Button(f1, text = "Search", command = lambda:[cleartreeview(), printRecords()])
bookSearchButton.grid(row = 0, column = 2)
ClearButton = Button(f1, text = "Clear", command = cleartreeview)
ClearButton.grid(row = 0, column = 3)




#("SELECT Title, `Colourway_Name`, Size, `Carton_Price`, Supplier  FROM Products WHERE CodeColour = ?", (e.get(),))

def Productviewer():
	global e , c , f, g ,h, Selected_order2, SC, mycust, info_frame, Selected_Customer, Addcustomer, Customrefs2, p, img, Selected_Customer, sizelabel, ImageURl, all_entries, quantity, orderref, Addorder, SO, sellprice, size, all_sizes, q, s, all_prices, all_labels
	
	

    # Toplevel object which will
    # be treated as a new window
	p = Toplevel(root)
	URl = str(ImageURl)
	SC = StringVar(p)
	SO = StringVar(p)
	q = StringVar(p)
	s = StringVar(p)
	# Create a Treeview Frame
	picture_frame = tk.Frame(p, bg='lightblue')
	picture_frame.grid(row=2, column=0, sticky='w')
	#send the request to get the image from URL
	response = requests.get(URl)
	#Open image
	img = Image.open(BytesIO(response.content))
	#Resize Image
	img = img.resize((250,280), Image.ANTIALIAS)

	#create the label for the image
	ph = ImageTk.PhotoImage(img)
	#put the label in the frame
	picture = Label(picture_frame, image=ph)
	#reference the image and label together
	picture.image=ph
	#put the picture label in the frame
	picture.grid(row=2, column=0)
	
	#create frame for treeview in 'p' new top level
	product_frame = tk.Frame(p, bg='red')
	#grid frame
	product_frame.grid(row = 8, column = 0)
	Label(p, text = f + ' ' + g,font=("Arial", 20,"bold")).grid(row = 0, column = 0, sticky = 'nw')
	Label(p, text = h,font=("Arial", 12,"bold")).grid(row = 1, column = 0, sticky = 'nw')

	#calculations and ordering frame
	sizes_frame = tk.Frame(p, bg='yellow')
	sizes_frame.grid(row=8, column=1, sticky= 'n')

	#Customer and Order Info Frame
	info_frame = tk.Frame(p, bg='light blue')
	info_frame.grid(row=2, column=1, sticky= 'n')
	
	Label(info_frame, text= 'Current Orders', font=('Helvatical bold',10)).grid(row= 0, column=1,  padx=10, pady=5)
	Label(info_frame, text= 'New Order', font=('Helvatical bold',10)).grid(row= 0, column=2,  padx=10, pady=5)
	
	#Order Drop Down Box & Label
	Label(info_frame, text= 'Order Number', font=('Helvatical bold',10)).grid(row= 1, column=0, sticky='ne', padx=10, pady=5)
	connection = sqlite3.connect('Orders.db')
	cur = connection.cursor()
	cur.execute("SELECT DISTINCT  `Orderref` FROM Orders")
	Orderrefs2 = cur.fetchall()

	connection.commit()
	connection.close()
	Selected_order2 = tk.StringVar()
	
	Order_drop = ttk.Combobox(info_frame, textvariable=Selected_order2)
		
	Order_drop['values'] = Orderrefs2
	Order_drop.bind('<<ComboboxSelected>>', CopyOrder)
	Order_drop.grid(row=1,column=1,sticky='nw', padx=10, pady=5)


	#Customer Drop Down Box & Label
	Label(info_frame, text= 'Customer Ref', font=('Helvatical bold',10)).grid(row= 2, column=0, sticky='ne', padx=10, pady=5)
	connection = sqlite3.connect('Customers_crm.db')
	cur = connection.cursor()
	cur.execute("SELECT DISTINCT  `Customer_Ref` FROM customers")
	Customrefs2 = cur.fetchall()

	connection.commit()
	connection.close()

	mycust = tk.StringVar()
	
	Customer_drop = ttk.Combobox(info_frame, textvariable=mycust)
		
	Customer_drop['values'] = Customrefs2
	Customer_drop.bind('<<ComboboxSelected>>', CopyCustomer)
	Customer_drop.grid(row=2,column=2,sticky='nw', padx=10, pady=5)
	#Addcustomer.destroy()
	Addcustomer = Entry(info_frame, textvariable = SC)
	Addcustomer.grid(row = 2, column = 1 )

	#New Customer Button
	Button(info_frame, text = 'New Customer',command=lambda:[CRM()]).grid(row = 3, column = 0, sticky = 'e', padx=10, pady=5)

	Addorder = Entry(info_frame, textvariable = SO)
	Addorder.bind('<Return>', lambda _:[addtoorder(),Close(), currentorders()])
	Addorder.grid(row = 1, column = 2 )
	Button(info_frame, text = 'Add to order', command = lambda:[addtoorder(),Close(), currentorders()]).grid(row = 3, column = 2)

	connection = sqlite3.connect('productdata.db')
	
	pro = connection.cursor()
	
	pro.execute("SELECT Size FROM Products WHERE CodeColour = ?", (e.get(),))
	connection.commit()


	all_sizes = pro.fetchall()
	all_sizes= [i[0] for i in all_sizes]
	

	all_labels = { e.get(): {} }
	all_entries = { e.get(): {} }
	all_prices = { e.get(): {} }
	

	for number, size in enumerate(all_sizes):
		pricelabel = tk.Label(sizes_frame, text = 'Sell Price',font=("Arial", 10,"bold"))
		Quantitylabel = tk.Label(sizes_frame, text = 'Quantity',font=("Arial", 10,"bold"))
		sizelabel = tk.Label(sizes_frame, text=size, font=('Helvatical bold',10))
		quantity = tk.Entry(sizes_frame, width=6)
		sellprice = tk.Entry(sizes_frame, width=10)
		if number < 10:
			Quantitylabel.grid(row=0, column=2, padx=5, pady=5)
			sizelabel.grid(row=number+1, column=1, padx=5, pady=5)
			quantity.grid(row=number+1, column=2, padx=5, pady=5)
			sellprice.grid(row=number+1, column=3, padx=5, pady=5)
			pricelabel.grid(row=0, column=3)

		else:
			Quantitylabel.grid(row=0, column=3, padx=5, pady=5)
			sizelabel.grid(row=number-9, column=4, padx=5, pady=5)
			quantity.grid(row=number-9, column=5, padx=5, pady=5)
			sellprice.grid(row=number-9, column=6, padx=5, pady=5)
			pricelabel.grid(row=0, column=6)

		quantity.insert(0,'0')
		sellprice.insert(0,'£0.00')
		
		all_labels[e.get()][size] = sizelabel
		all_entries[e.get()][size] = quantity
		all_prices[e.get()][size] = sellprice
		
		
	connection.close
	

	# Create a Treeview Scrollbar
	tree_scroll = Scrollbar(product_frame)
	tree_scroll.pack(side=RIGHT, fill=Y)

	# Create The Treeview
	secondtree = ttk.Treeview(product_frame, yscrollcommand=tree_scroll.set, selectmode="extended",height=12)
	secondtree.pack()

	# Configure the Scrollbar
	tree_scroll.config(command=secondtree.yview)
	# Define Our Columns
	secondtree['columns'] = ("Description", "Colour", "Sizes" ,  "Carton Price", "Supplier")

	# Format Our Columns
	secondtree.column("#0", width=0, stretch=NO)
	#secondtree.column("Style Code", anchor=W, width=100, stretch=YES)
	secondtree.column("Description", anchor=W, width=220, stretch=YES)
	secondtree.column("Colour", anchor=W, width=140, stretch=YES)
	secondtree.column("Sizes", anchor=CENTER, width=50, stretch=YES)
	secondtree.column("Carton Price", anchor=CENTER, width=70, stretch=YES)
	secondtree.column("Supplier", anchor=CENTER, width=50, stretch=YES)
	#my_tree.column("VAT code", anchor=CENTER, width=40, stretch=YES)

	# Create Headings
	secondtree.heading("#0", text="", anchor=W)
	#secondtree.heading("Style Code", text="Style Code", anchor=W)
	secondtree.heading("Description", text="Description", anchor=W)
	secondtree.heading("Colour", text="Colour", anchor=W)
	secondtree.heading("Sizes", text="Sizes", anchor=CENTER)
	secondtree.heading("Carton Price", text="Carton Price", anchor=CENTER)
	secondtree.heading("Supplier", text="Supplier", anchor=CENTER)

	#my_tree.heading("VAT code", text="VAT code", anchor=CENTER)
	
	# sets the title of the
    # Toplevel widget
	p.title("Product Viewer")
 
   	# sets the geometry of toplevel
	p.geometry("1000x800")
	
		
	#create connection to db	
	connection = sqlite3.connect('productdata.db')
	pro = connection.cursor()
	pro.execute("SELECT Title, `Colourway_Name`, Size, `Carton_Price`, Supplier  FROM Products WHERE CodeColour = ?", (e.get(),))
	connection.commit()
	product = pro.fetchall()
	for row in product:
		#print(row)
		secondtree.insert("",tk.END,values=row)
	connection.close	

my_tree.bind("<Double-1>", lambda e: [selector(),GetImageURL(),Productviewer()])



root.mainloop()