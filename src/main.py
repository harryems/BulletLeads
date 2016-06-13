from utilities.customcsv import CustomCSV
from utilities.customdriver import CustomDriver
from utilities.feed import Feed
from utilities.row import ROW
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException   
from bs4 import BeautifulSoup     
import unicodecsv as csv
import re
import sys
import glob
from collections import defaultdict


reload(sys)  
sys.setdefaultencoding('utf8')

def check_exists_by_class(_class,driver):
    try:
        driver.find_element_by_class_name(_class)
    except NoSuchElementException:
        return False
    return True
def check_exists_by_id(_id,driver):
    try:
        driver.find_element_by_id(_id)
    except NoSuchElementException:
        return False
    return True

if __name__ == '__main__':
    mainUrls=['http://www.pcna.com/Bullet/en-us','http://www.pcna.com/Leeds/en-us']
    writerImegesUpload=csv.writer(open('images_Upload.csv', 'wb'))
    writerColors = csv.writer(open('attributeColors.csv', 'wb'))
    writerColors.writerow(['sku','color'])
    writerCategories = csv.writer(open('Categories_cliente_leedBullet.csv', 'wb'))     
    writerCategories.writerow(['sku','categories'])
    writerImages = csv.writer(open('images_leedBullet.csv', 'wb'))
    writerImages.writerow(['sku','media_gallery','image','small_image','thumbnail'])
    header=['sku','colors','_store','_attribute_set','_type','_product_websites','color','cost','country_of_manufacture','created_at','custom_design','custom_design_from','custom_design_to','custom_layout_update','description','gallery','gift_message_available','has_options','image','image_label','media_gallery','meta_description','meta_keyword','meta_title','minimal_price','msrp','msrp_display_actual_price_type','msrp_enabled','name','news_from_date','news_to_date','options_container','page_layout','price','required_options','short_description','small_image','small_image_label','special_from_date','special_price','special_to_date','status','tax_class_id','thumbnail','thumbnail_label','visibility','weight','qty','is_in_stock','manage_stock','_tier_price_customer_group','_tier_price_qty','_tier_price_price','_tier_price_website','_group_price_customer_group','_group_price_price','_media_attribute_id','_media_image','_media_lable','_media_position','_media_is_disabled','_absolute_price','_absolute_weight','_sku_policy','_custom_option_store','_custom_option_type','_custom_option_title','_custom_option_is_required','_custom_option_price','_custom_option_sku','_custom_option_max_characters','_custom_option_sort_order','_custom_option_file_extension','_custom_option_image_size_x','_custom_option_image_size_y','_custom_option_template_id','_custom_option_view_mode','_custom_option_customoptions_is_onetime','_custom_option_show_swatch_title','_custom_option_image_path','_custom_option_customer_groups','_custom_option_store_views','_custom_option_qnty_input','_custom_option_in_group_id','_custom_option_is_dependent','_custom_option_div_class','_custom_option_image_mode','_custom_option_exclude_first_image','_custom_option_description','_custom_option_default_text','_custom_option_sku_policy','_custom_option_row_title','_custom_option_row_price','_custom_option_row_sort','_custom_option_row_sku','_custom_option_row_image_data','_custom_option_row_default','_custom_option_row_in_group_id','_custom_option_row_dependent_ids','_custom_option_row_weight','_custom_option_row_cost','_custom_option_row_special_data','_custom_option_row_tier_data','use_config_manage_stock','_super_products_sku','_super_attribute_code','_super_attribute_option','_super_attribute_price_corr','use_config_enable_qty_inc','use_config_qty_increments','use_config_max_sale_qty','use_config_notify_stock_qty','use_config_min_qty','use_config_backorders','use_config_min_sale_qty','min_qty','is_qty_decimal','backorders','min_sale_qty','max_sale_qty','stock_status_changed_auto','qty_increments','enable_qty_increments','is_decimal_divided','tiertabs','video','productofrente','productoaltura','productoprofundidad','productodiametro','productopeso','cartonfrente','cartonaltura','cartonprofundidad','cartonpieza','cartonpeso','empaque','manufacturer','sku_b']
    writer = csv.writer(open('leedBullet.csv', 'wb'))
    writer.writerow(header)    
    
    
    customCSV=CustomCSV()
    customDriver = CustomDriver()
    index=0
    productIndex=0
#     for mainUrl in mainUrls:
    #driver=Firefox()
    #feed=Feed()
    #items=feed.read()
    total = str(len(glob.glob("C:/Users/carlos.espinosa/Documents/workspace/usb/src/*.html")))
    for item in glob.glob("C:/Users/carlos.espinosa/Documents/workspace/usb/src/*.html"):
        index+=1
        print str(index)+" of "+total
        soup = BeautifulSoup(open(item), "html.parser") 
        _sku=soup.find('p',{'class':'product-style'}).text.strip()
#         print "\t"+_sku
#         if _sku.strip()!='HL-603FLYER':
#             continue
        _description=soup.find('div',{'class':'wp-product-details-tab'}).find('p').text.strip()
        _clearance=True if soup.find('span',{'class':'callout-clearance'}) else False
        colors=soup.find('div',{'class':'regular-colors'}).findAll('a')
        breadcrumbs=soup.find('div',{'class':'wp-breadcrumb'})
        categories=[]
        brand=soup.find('div',{'class':'brand-logo'}).find('img')['alt'] if soup.find('div',{'class':'brand-logo'}) else ''
        productName=""
        productName=soup.find('div',{'class':'logo-and-title'}).h1.text.strip()
        for breadcrumb in breadcrumbs.findAll('a')[2:]:
            categories.append(breadcrumb.text.strip())
        writerCategories.writerow([_sku,'USA Partners/'+'/'.join(categories)])
        simplesSkus=[]
        for color in colors:
            _color= color['title'].strip()
            _hex=re.search('#(.*)\;',color.find('span')['style']).group(1)
            _id=color['id'].strip().replace('color_swatch_box_','')
            writerColors.writerow([_id,_color,_hex])
            simplesSkus.append({'sku':_id,'color':_color,'hex':_hex})
            
#         _brand=item['brand']
        images=soup.findAll('a',{'class':'image-s-links'})
        find = re.compile(r"\_(.*)")

        listImages = defaultdict(list)
        for image in images:
#             print image
#             print image['id']
#             print re.search(find,image['id']).group(1).split("_")[0]
            listImages[re.search(find,image['id']).group(1).split("_")[0].strip()].append(image.find('img')['data-original'].replace('medium','hires').strip())
#             print image.find('img')['data-original'].replace('medium','hires')
        imagesSimples=[]
        for _items in  listImages.keys():
            imagesSimples.append(listImages[_items][0])
            writerImages.writerow( [_items,";".join(listImages[_items]),"+"+listImages[_items][0],"+"+listImages[_items][0],"+"+listImages[_items][0]])
        writerImages.writerow( [_sku,";".join(imagesSimples),"+"+imagesSimples[0],"+"+imagesSimples[0],"+"+imagesSimples[0]])
#             for _url in listImages[_items]:
#                 print _url
#                 for _url in  _item:
#                     
#                     print  _url 
        _Material=soup.findAll('label', text = re.compile('Material'))[0].findNext('span').text.strip() if len(soup.findAll('label', text = re.compile('Material')))>0 else ''
        _Ounces=soup.findAll('label', text = re.compile('Ounces'))[0].findNext('span').text.strip() if len(soup.findAll('label', text = re.compile('Ounces')))>0 else ''
        _Packaging=soup.findAll('label', text = re.compile('Packaging'))[0].findNext('span').text.strip() if len(soup.findAll('label', text = re.compile('Packaging')))>0 else ''
        _Weight=soup.findAll('label', text = re.compile('Weight'))[0].findNext('span').text.strip() if len(soup.findAll('label', text = re.compile('Weight')))>0 else ''
        _MasterCartonCasePack=soup.findAll('label', text = re.compile('Master Carton Case Pack'))[0].findNext('span').text.strip() if len(soup.findAll('label', text = re.compile('Master Carton Case Pack')))>0 else ''
        _MasterCartonWeight=soup.findAll('label', text = re.compile('Master Carton Weight'))[0].findNext('span').text.strip() if len(soup.findAll('label', text = re.compile('Master Carton Weight')))>0 else ''
        __MasterCartonHeight=soup.findAll('label', text = re.compile('Master Carton Height'))[0].findNext('span').text.strip() if len(soup.findAll('label', text = re.compile('Master Carton Height')))>0 else '' 
        try:
            _MasterCartonHeight=2.54*float(__MasterCartonHeight)
        except:
            _MasterCartonHeight=''
        __MasterCartonDepth=soup.findAll('label', text = re.compile('Master Carton Depth'))[0].findNext('span').text.strip() if len(soup.findAll('label', text = re.compile('Master Carton Depth')))>0 else ''
        try:
            _MasterCartonDepth=2.54*float(__MasterCartonDepth)
        except:
            _MasterCartonDepth='' 
        __MasterCartonWidth=soup.findAll('label', text = re.compile('Master Carton Width'))[0].findNext('span').text.strip() if len(soup.findAll('label', text = re.compile('Master Carton Height')))>0 else ''
        try:
            _MasterCartonWidth=2.54*float(__MasterCartonWidth)
        except:
            _MasterCartonWidth='' 
        
        
        _price=0.0
        try:
            _price=float(soup.find('div',{'class':'price-list'}).findAll('tr')[1].findAll('td')[1].text.replace('$','').strip())
        except:
            pass
        _price=_price*17*1.4
        rows=[]
        rowsIndex=0
        productIndex+=1
        for skus_index,_optionsku in enumerate(simplesSkus):            
            _skuColor=_optionsku['sku']
            _color=_optionsku['color']
            rowsimple=ROW('simple')
            rows.insert(rowsIndex, rowsimple)
            rows[rowsIndex].setSku(_skuColor)
            rows[rowsIndex].setName(_sku+" "+productName)
            rows[rowsIndex].setColor(_color)
            rows[rowsIndex].setPrice('{0:.2f}'.format(_price))
            rowsIndex+=1
        for row in rows:
            data=row.printRow()
            writer.writerow(data)
#         
#         
        rows=[]
        rowsIndex=0
        x=ROW('configurable')
        rows.insert(rowsIndex, x)        
        rows[rowsIndex].setBrand(brand)
        rows[rowsIndex].setSku(_sku)
        rows[rowsIndex].setDescription(_description)
        rows[rowsIndex].setShort_Description(_description)
        rows[rowsIndex].setName(_sku+" "+productName)
        rows[rowsIndex].setPrice('{0:.2f}'.format(_price))
        rows[rowsIndex].setCartonFrente(_MasterCartonHeight)
        rows[rowsIndex].setCartonAltura(_MasterCartonWidth)
        rows[rowsIndex].setCartonProfundidad(_MasterCartonDepth)
        rows[rowsIndex].setCartonPieza(_MasterCartonCasePack)
        rows[rowsIndex].setCartonPeso(_MasterCartonWeight)
        rows[rowsIndex].setEmpaque(_Packaging)    
        rows[rowsIndex].setBrand(brand)   
        rows[rowsIndex].set_Custom_Option_Type('field')
        rows[rowsIndex].set_Custom_Option_Title('Cantidad')
        rows[rowsIndex].set_Custom_Option_Is_Required('1')
        rows[rowsIndex].set_Custom_Option_Price('0.0000')
        rows[rowsIndex].set_Custom_Option_Max_Characters('0')
        rows[rowsIndex].set_Custom_Option_Sort_Order('1')
        rows[rowsIndex].set_Custom_Option_View_Mode('1')
        rows[rowsIndex].set_Custom_Option_Customoptions_Is_Onetime('1')
        rows[rowsIndex].set_Custom_Option_Show_Swatch_Title('0')
        rows[rowsIndex].set_Custom_Option_Qnty_Input('0')
        rows[rowsIndex].set_Custom_Option_Is_Dependent('0')
        rows[rowsIndex].set_Custom_Option_Div_Class('qty-options')
        rows[rowsIndex].set_Custom_Option_Image_Mode('1')
        rows[rowsIndex].set_Custom_Option_Exclude_First_Image('0')
        rows[rowsIndex].set_Custom_Option_Sku_Policy('0')
        rows[rowsIndex].set_Custom_Option_In_Group_Id(rowsIndex+1)
       
        for skus_index,_optionsku in enumerate(simplesSkus):
            if skus_index>0:
                rowsIndex+=1
                x=ROW()
                rows.insert(rowsIndex, x)
            _skuColor=_optionsku['sku']
            _color=_optionsku['color']
            rows[rowsIndex].set_Super_Products_Sku(_skuColor)
            rows[rowsIndex].set_Super_Attribute_Code('color')
            rows[rowsIndex].set_Super_Attribute_Option(_color)
#  
# 
        for row in rows:
            data=row.printRow()
            writer.writerow(data)
#         html_source = driver.page_source
#         soup = BeautifulSoup(html_source, 'html.parser')
#         _file = open(brand+_sku+".html", "wb")
#         _file.write(soup.prettify().encode('UTF-8'))        
#         _file.close() 
        
#         print _sku,description,",".join(colors),medidas
#         for areaImpresion in areasImpresion:
#             writer.writerow([_sku,'','','',areaImpresion['name'],areaImpresion['description']])
             
        
#         except:
#             continue