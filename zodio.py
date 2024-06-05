print()
print()
print('Zodio Mart')
print('---------------------------------------------------Welcome to Zodio Mart--------------------------------------------------')
print('Product List')
print('-------------')
print('1.Mobiles','\t\t\t','2.Watches','\t\t\t','3.TV','\t\t\t','4.Laptops')
product=input('Pic any One : ')
# Mobiles--------------------------------------------------------
if product.lower() == 'mobiles' or product == '1':
    print('----------------------------------------------------------Mobiles---------------------------------------------------------')
    print('1.Redmi','\t\t\t','2.Oppo','\t\t\t','3.Vivo','\t\t\t','4.Apple')
    mobile=input('Phick Any One : ')

    m_dict = { 'redmi':{'Brand Name':' Redmi',
                    'Model Name':' Note 13 Pro',
                    'Product ID':' MR001',
                    'Price     ':' 14999',
                    'Discount  ':' 5%'},

               'oppo':{'Brand Name':' Oppo',
                    'Model Name':' Reno 15 Pro',
                    'Product ID':' MO001',
                    'Price     ':' 21499',
                    'Discount  ':' 7%'},

               'vivo':{'Brand Name':' Vivo',
                    'Model Name':' Y12 Plus',
                    'Product ID':' MV001',
                    'Price     ':' 20000',
                    'Discount  ':' 8%'},

               'apple':{'Brand Name':' Apple',
                    'Model Name':' 15 Pro Max',
                    'Product ID':' MA001',
                    'Price     ':' 121499',
                    'Discount  ':' 7%'},          
             }
    if mobile.lower() == 'redmi' :
        print('----------------Redmi----------------')
        for key,value in m_dict['redmi'].items():
            print(key,'\t',':','\t',value)
        p_id=m_dict['redmi'].get('Product ID').strip()
        price=int(m_dict['redmi'].get('Price     '))
        disc=float(m_dict['redmi'].get('Discount  ').strip('%'))/100
        pd1=m_dict['redmi'].get('Brand Name')
        pd2=m_dict['redmi'].get('Model Name')
        
    elif mobile.lower() == 'oppo' :
        print('----------------Oppo----------------')
        for key,value in m_dict['oppo'].items():
            print(key,'\t',':','\t',value)
        p_id=m_dict['oppo'].get('Product ID').strip()
        price=int(m_dict['oppo'].get('Price     '))
        disc=float(m_dict['oppo'].get('Discount  ').strip('%'))/100
        pd1=m_dict['oppo'].get('Brand Name')
        pd2=m_dict['oppo'].get('Model Name')

    elif mobile.lower() == 'vivo' :
        print('-----------------Vivo----------------')
        for key,value in m_dict['vivo'].items():
            print(key,'\t',':','\t',value)
        p_id=m_dict['vivo'].get('Product ID').strip()
        price=int(m_dict['vivo'].get('Price     '))
        disc=float(m_dict['vivo'].get('Discount  ').strip('%'))/100
        pd1=m_dict['vivo'].get('Brand Name')
        pd2=m_dict['vivo'].get('Model Name')

    elif mobile.lower() == 'apple' :
        print('----------------Apple----------------')
        for key,value in m_dict['apple'].items():
            print(key,'\t',':','\t',value)
        p_id=m_dict['apple'].get('Product ID').strip()
        price=int(m_dict['apple'].get('Price     '))
        disc=float(m_dict['apple'].get('Discount  ').strip('%'))/100
        pd1=m_dict['apple'].get('Brand Name')
        pd2=m_dict['apple'].get('Model Name')
# Watches----------------------------------------------
elif product.lower() == 'watches' or product == '2' :
    print('----------------------------------------------------------Watches---------------------------------------------------------')
    print('1.Sonata','\t\t\t','2.Fastrack','\t\t\t','3.Titan','\t\t\t','4.Rolex')
    watch=input('Phick Any One : ')

    w_dict = { 'sonata':{'Brand Name':' Sonata',
                    'Model Name':' RMP-3',
                    'Product ID':' SW001',
                    'Price     ':' 25499',
                    'Discount  ':' 5%'},

               'fastrack':{'Brand Name':' Fastrack',
                    'Model Name':' QM01y',
                    'Product ID':' FW001',
                    'Price     ':' 5600',
                    'Discount  ':' 7%'},

               'titan':{'Brand Name':' Titan',
                    'Model Name':' 9011SL',
                    'Product ID':' TW001',
                    'Price     ':' 11450',
                    'Discount  ':' 8%'},

               'rolex':{'Brand Name':' Rolex',
                    'Model Name':' GMT-Mster',
                    'Product ID':' RW001',
                    'Price     ':' 1833000',
                    'Discount  ':' 7%'},          
             }    
    if watch.lower() == 'sonata' :
        print('----------------Sonata----------------')
        for key,value in w_dict['sonata'].items():
            print(key,'\t',':','\t',value)
        p_id=w_dict['sonata'].get('Product ID').strip()
        price=int(w_dict['sonata'].get('Price     '))
        disc=float(w_dict['sonata'].get('Discount  ').strip('%'))/100
        pd1=w_dict['sonata'].get('Brand Name')
        pd2=w_dict['sonata'].get('Model Name')
    
    elif watch.lower() == 'fastrack' :
        print('----------------Fastrack----------------')
        for key,value in w_dict['fastrack'].items():
            print(key,'\t',':','\t',value)
        p_id=w_dict['fastrack'].get('Product ID').strip()
        price=int(w_dict['fastrack'].get('Price     '))
        disc=float(w_dict['fastrack'].get('Discount  ').strip('%'))/100
        pd1=w_dict['fastrack'].get('Brand Name')
        pd2=w_dict['fastrack'].get('Model Name')

    elif watch.lower() == 'titan' :
        print('----------------Titan----------------')
        for key,value in w_dict['titan'].items():
            print(key,'\t',':','\t',value)
        p_id=w_dict['titan'].get('Product ID').strip()
        price=int(w_dict['titan'].get('Price     '))
        disc=float(w_dict['titan'].get('Discount  ').strip('%'))/100
        pd1=w_dict['titan'].get('Brand Name')
        pd2=w_dict['titan'].get('Model Name')

    elif watch.lower() == 'rolex' :
        print('----------------Rolex----------------')
        for key,value in w_dict['rolex'].items():
            print(key,'\t',':','\t',value)
        p_id=w_dict['rolex'].get('Product ID').strip()
        price=int(w_dict['rolex'].get('Price     '))
        disc=float(w_dict['rolex'].get('Discount  ').strip('%'))/100
        pd1=w_dict['rolex'].get('Brand Name')
        pd2=w_dict['rolex'].get('Model Name')        
# TV ------------------------------------------------------------
elif product.lower() == 'tv' or product == '3':
    print('------------------------------------------------------------TV\'s\'------------------------------------------------------')
    print('1.Samsung','\t\t\t','2.LG','\t\t\t','3.MI','\t\t\t','4.Sony')
    tv=input('Phick Any One : ')

    tv_dict = { 'samsung':{'Brand Name':' Samsung',
                    'Model Name':' UHD4',
                    'Product ID':' SW001',
                    'Price     ':' 32550',
                    'Discount  ':' 5%'},

               'lg':{'Brand Name':' LG',
                    'Model Name':' Smart8 Plus',
                    'Product ID':' FW001',
                    'Price     ':' 47500',
                    'Discount  ':' 7%'},

               'mi':{'Brand Name':' MI',
                    'Model Name':' UHD L43RS',
                    'Product ID':' TW001',
                    'Price     ':' 25000',
                    'Discount  ':' 6%'},

               'sony':{'Brand Name':' Sony',
                    'Model Name':' 4KU TS1',
                    'Product ID':' RW001',
                    'Price     ':' 1833000',
                    'Discount  ':' 7%'},          
             } 
    if tv.lower() == 'samsung' :
        print('----------------Samsung----------------')
        for key,value in tv_dict['samsung'].items():
            print(key,'\t',':','\t',value)
        p_id=tv_dict['samsung'].get('Product ID').strip()
        price=int(tv_dict['samsung'].get('Price     '))
        disc=float(tv_dict['samsung'].get('Discount  ').strip('%'))/100
        pd1=tv_dict['samsung'].get('Brand Name')
        pd2=tv_dict['samsung'].get('Model Name')

    elif tv.lower() == 'lg' :
        print('----------------LG----------------')
        for key,value in tv_dict['lg'].items():
            print(key,'\t',':','\t',value)
        p_id=tv_dict['lg'].get('Product ID').strip()
        price=int(tv_dict['lg'].get('Price     '))
        disc=float(tv_dict['lg'].get('Discount  ').strip('%'))/100
        pd1=tv_dict['lg'].get('Brand Name')
        pd2=tv_dict['lg'].get('Model Name')

    elif tv.lower() == 'mi' :
        print('----------------MI----------------')
        for key,value in tv_dict['mi'].items():
            print(key,'\t',':','\t',value)
        p_id=tv_dict['mi'].get('Product ID').strip()
        price=int(tv_dict['mi'].get('Price     '))
        disc=float(tv_dict['mi'].get('Discount  ').strip('%'))/100
        pd1=tv_dict['mi'].get('Brand Name')
        pd2=tv_dict['mi'].get('Model Name')

    elif tv.lower() == 'sony' :
        print('----------------Sony----------------')
        for key,value in tv_dict['sony'].items():
            print(key,'\t',':','\t',value)
        p_id=tv_dict['sony'].get('Product ID').strip()
        price=int(tv_dict['sony'].get('Price     '))
        disc=float(tv_dict['sony'].get('Discount  ').strip('%'))/100 
        pd1=tv_dict['sony'].get('Brand Name')
        pd2=tv_dict['sony'].get('Model Name')      
# Laptops ---------------------------------------------------------
elif product.lower() == 'laptops' or product == '4':
    print('----------------------------------------------------------Laptops---------------------------------------------------------')
    print('1.Lenovo','\t\t\t','2.Dell','\t\t\t','3.Asus','\t\t\t','4.Apple')
    laptop=input('Phick Any One : ')

    l_dict = { 'lenovo':{'Brand Name':' Lenovo',
                    'Model Name':' IdeaPad',
                    'Product ID':' LL001',
                    'Price     ':' 41550',
                    'Discount  ':' 5%'},

               'dell':{'Brand Name':' Dell',
                    'Model Name':' Vp9.5',
                    'Product ID':' DL001',
                    'Price     ':' 77500',
                    'Discount  ':' 7%'},

               'asus':{'Brand Name':' Asus',
                    'Model Name':' VivoBook',
                    'Product ID':' AL001',
                    'Price     ':' 65000',
                    'Discount  ':' 6%'},

               'apple':{'Brand Name':' Sony',
                    'Model Name':' MacBook Pro',
                    'Product ID':' AL001',
                    'Price     ':' 150000',
                    'Discount  ':' 7%'},          
             }
    if laptop.lower() == 'lenovo' :
        print('----------------Lenovo----------------')
        for key,value in l_dict['lenovo'].items():
            print(key,'\t',':','\t',value)
        p_id=l_dict['lenovo'].get('Product ID').strip()
        price=int(l_dict['lenovo'].get('Price     '))
        disc=float(l_dict['lenovo'].get('Discount  ').strip('%'))/100
        pd1=l_dict['lenovo'].get('Brand Name')
        pd2=l_dict['lenevo'].get('Model Name')


    if laptop.lower() == 'dell' :
        print('----------------Dell----------------')
        for key,value in l_dict['dell'].items():
            print(key,'\t',':','\t',value)
        p_id=l_dict['dell'].get('Product ID').strip()
        price=int(l_dict['dell'].get('Price     '))
        disc=float(l_dict['dell'].get('Discount  ').strip('%'))/100   
        pd1=l_dict['dell'].get('Brand Name')
        pd2=l_dict['dell'].get('Model Name')

    if laptop.lower() == 'asus' :
        print('----------------Asus----------------')
        for key,value in l_dict['asus'].items():
            print(key,'\t',':','\t',value)
        p_id=l_dict['asus'].get('Product ID').strip()
        price=int(l_dict['asus'].get('Price     '))
        disc=float(l_dict['asus'].get('Discount  ').strip('%'))/100 
        pd1=l_dict['asus'].get('Brand Name')
        pd2=l_dict['asus'].get('Model Name')

    if laptop.lower() == 'apple' :
        print('----------------Apple----------------')
        for key,value in l_dict['apple'].items():
            print(key,'\t',':','\t',value)
        p_id=l_dict['apple'].get('Product ID').strip()
        price=int(l_dict['apple'].get('Price     '))
        disc=float(l_dict['apple'].get('Discount  ').strip('%'))/100 
        pd1=l_dict['apple'].get('Brand Name')
        pd2=l_dict['apple'].get('Model Name')
                
pd=pd1+pd2
tot_prc=price-(disc*price)
print('-----------------------------------')
print('Total Price      :       ',tot_prc)
print('-----------------------------------')            
        
buy=input('Enter \'yes\' To Buy Now or Enter \'no\' To Close : ')
if buy.lower() == 'yes':
    print('---------------------------------------------------------Buy Now---------------------------------------------------------')   
    name=input('Enter your Full Name       : ')
    num=int(input('Enter your Mobile Number   : '))
    add=input('Enter your Address         : ')
    print('Product ID                 :',p_id)
    qty=int(input('Enter the Quantity         : '))

    
    print('-------------------------------------------------------Bill--------------------------------------------------------------')  
    print('Full Name','\t','Mobile Number','\t','Address','\t','Product ID','\t','Product Details','\t','Quantity','\t','Total Price')
    print(name,'\t\t',num,'\t',add,'\t',p_id,'\t\t',pd,'\t',qty,'\t\t',qty*tot_prc)
    print('-------------------------------------------------------------------------------------------------------------------------')
else:
    print()
    print('Thank you for Visiting Zodio Mart')
    print('------------------------------------------------------See You Again-------------------------------------------------------')
    print()
    print()