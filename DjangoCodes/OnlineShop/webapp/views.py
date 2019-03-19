from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(req):
#     return HttpResponse("<h1>This is hello world app</h1>")

productsList = [
    {"p_category" :"mobile", "brand" : "Apple", "p_id":101,"p_name":'Apple Iphone X', 'p_price':80000,'p_image':'https://www.yaphone.com/1469-tm_large_default/apple-iphone-x-256gb-silver.jpg'},
    {"p_category" :"mobile", "brand" : "Apple", "p_id":102,"p_name":'Apple Iphone XS', 'p_price':90000,'p_image':'https://static.toiimg.com/photo/65786818/Apple-iPhone-XS-Max.jpg'},
    {"p_category" :"mobile", "brand" : "Samsung","p_id":103,"p_name":"Samsung Galaxy","p_price":67000,'p_image':'https://www.91-img.com/pictures/117874-v1-samsung-galaxy-s9-mobile-phone-large-1.jpg'},
    {"p_category" :"mobile", "brand" : "Vivo","p_id":104,"p_name":"Vivo V11","p_price":30000,"p_image":'https://images.sg.content-cdn.io/cdn//in-resources/0211f4bd-ce6a-4162-95a2-f801e5ae9176/Images/ProductImages/Source/Z11-Front.jpg;width=600;height=900;scale=canvas;anchor=bottomcenter'},
    {"p_category" :"laptop", "brand" : "Apple","p_id":105,"p_name":'Apple Macbook', 'p_price':65000,'p_image':'https://johnlewis.scene7.com/is/image/JohnLewis/237841771?$rsp-pdp-port-1440$'},
    {"p_category" :"headphones", "brand" : "JBL","p_id":106,"p_name":"JBL Headphones","p_price":3000,"p_image":'http://assets.myntassets.com/assets/images/7827829/2018/11/27/2ee4f3bf-01b3-4a50-8154-1cb0688ac0b61543314894148-JBL-T500-Powerful-Bass-On-Ear-Headphones-with-Mic-Black-8301-1.jpg'},
    {"p_category" :"shoes", "brand" : "Adidas","p_id":107,"p_name":"Adidas Shoes","p_price":5000,'p_image':'https://assets.adidas.com/images/w_600,f_auto,q_auto/954ed7d53b674738b128a7840137c369_9366/EQT_Support_91_17_Shoes_Black_BZ0585_01_standard.jpg'},
    {"p_category" :"headphones", "brand" : "JBL","p_id":108,"p_name":"JBL Headphones","p_price":3000,"p_image":'http://assets.myntassets.com/assets/images/7827829/2018/11/27/2ee4f3bf-01b3-4a50-8154-1cb0688ac0b61543314894148-JBL-T500-Powerful-Bass-On-Ear-Headphones-with-Mic-Black-8301-1.jpg'},
    {"p_category" :"mobile", "brand" : "Apple","p_id":109,"p_name":'Apple Iphone X', 'p_price':70000,'p_image':'https://www.yaphone.com/1469-tm_large_default/apple-iphone-x-256gb-silver.jpg'},
    {"p_category" :"shoes", "brand" : "Adidas","p_id":110,"p_name":"Adidas Shoes","p_price":5000,'p_image':'https://assets.adidas.com/images/w_600,f_auto,q_auto/954ed7d53b674738b128a7840137c369_9366/EQT_Support_91_17_Shoes_Black_BZ0585_01_standard.jpg'},
    {"p_category" :"mobile", "brand" : "Samsung","p_id":111,"p_name":"Samsung Galaxy","p_price":55000,'p_image':'https://www.91-img.com/pictures/117874-v1-samsung-galaxy-s9-mobile-phone-large-1.jpg'},
    {"p_category" :"laptop", "brand" : "Apple","p_id":112,"p_name":'Apple Macbook', 'p_price':65000,'p_image':'https://johnlewis.scene7.com/is/image/JohnLewis/237841771?$rsp-pdp-port-1440$'},
    {"p_category" :"headphones", "brand" : "JBL","p_id":113,"p_name":"JBL Headphones","p_price":3000,"p_image":'http://assets.myntassets.com/assets/images/7827829/2018/11/27/2ee4f3bf-01b3-4a50-8154-1cb0688ac0b61543314894148-JBL-T500-Powerful-Bass-On-Ear-Headphones-with-Mic-Black-8301-1.jpg'},
    {"p_category" :"mobile", "brand" : "Apple","p_id":114,"p_name":'Apple Iphone XS', 'p_price':90000,'p_image':'https://static.toiimg.com/photo/65786818/Apple-iPhone-XS-Max.jpg'},
    {"p_category" :"laptop", "brand" : "Apple","p_id":115,"p_name":'Apple Macbook', 'p_price':65000,'p_image':'https://static.digit.in/product/da4f92d644244c7a2b198396de26249d3290f6bb.png'},
    {"p_category" :"headphones", "brand" : "JBL","p_id":116,"p_name":"JBL Headphones","p_price":3000,"p_image":'http://assets.myntassets.com/assets/images/7827829/2018/11/27/2ee4f3bf-01b3-4a50-8154-1cb0688ac0b61543314894148-JBL-T500-Powerful-Bass-On-Ear-Headphones-with-Mic-Black-8301-1.jpg'},
    {"p_category" :"mobile", "brand" : "Apple","p_id":117,"p_name":'Apple Iphone X', 'p_price':85000,'p_image':'https://www.yaphone.com/1469-tm_large_default/apple-iphone-x-256gb-silver.jpg'},
    {"p_category" :"mobile", "brand" : "Apple","p_id":118,"p_name":'Apple Iphone XS', 'p_price':88000,'p_image':'https://static.toiimg.com/photo/65786818/Apple-iPhone-XS-Max.jpg'},
    {"p_category" :"mobile", "brand" : "Samsung","p_id":119,"p_name":"Samsung Galaxy","p_price":60000,'p_image':'https://www.91-img.com/pictures/117874-v1-samsung-galaxy-s9-mobile-phone-large-1.jpg'},
    {"p_category" :"mobile", "brand" : "Vivo","p_id":120,"p_name":"Vivo V11","p_price":28000,"p_image":'https://images.sg.content-cdn.io/cdn//in-resources/0211f4bd-ce6a-4162-95a2-f801e5ae9176/Images/ProductImages/Source/Z11-Front.jpg;width=600;height=900;scale=canvas;anchor=bottomcenter'},
    {"p_category" :"mobile", "brand" : "Apple","p_id":121,"p_name":'Apple Iphone X', 'p_price':70000,'p_image':'https://www.yaphone.com/1469-tm_large_default/apple-iphone-x-256gb-silver.jpg'},
    {"p_category" :"mobile", "brand" : "Apple","p_id":122,"p_name":'Apple Iphone XS', 'p_price':80000,'p_image':'https://static.toiimg.com/photo/65786818/Apple-iPhone-XS-Max.jpg'},
    {"p_category" :"mobile", "brand" : "Samsung","p_id":123,"p_name":"Samsung Galaxy","p_price":55000,'p_image':'https://www.91-img.com/pictures/117874-v1-samsung-galaxy-s9-mobile-phone-large-1.jpg'},
    {"p_category" :"mobile", "brand" : "Vivo","p_id":124,"p_name":"Vivo V11","p_price":32000,"p_image":'https://images.sg.content-cdn.io/cdn//in-resources/0211f4bd-ce6a-4162-95a2-f801e5ae9176/Images/ProductImages/Source/Z11-Front.jpg;width=600;height=900;scale=canvas;anchor=bottomcenter'},
]

def index(req):
    return render(req, 'index.html', {'products':productsList})

def products(req):
    return render(req, 'products.html')

def mobiles(req):
    mobile = []
    for data in productsList:
        if data['p_category'] == 'mobile':
            mobile.append(data)
    print(mobile)
    return render(req, 'include/mobiles.html', {'products':mobile})

def contact(req):
    return render(req, 'contact.html')

def about(req):
    return render(req, 'about.html')

def search(req):
    product = req.GET['product']
    product = product.lower()
    searchResult = []
    # print(product)
    for data in productsList:
        if product == data['brand'].lower() or product == data['p_category'].lower():
            searchResult.append(data)
    
    return render(req, 'include/search.html', {'products':searchResult})

def register(req):
    useremail = req.POST['u_email']
    userpwd = req.POST['u_pwd']

    return render(req, 'index.html', {'user_id':useremail, 'products':productsList})