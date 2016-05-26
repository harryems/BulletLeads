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
    writerColors = csv.writer(open('attributeColors.csv', 'a'))
#     writerColors.writerow(['sku','color'])
    writerCategories = csv.writer(open('Categories_cliente_leedBullet.csv', 'wb'))     
    writerCategories.writerow(['sku','categories'])
    writerImagesCategories = csv.writer(open('images_.csv', 'wb'))
    writerImagesCategories.writerow(['sku','media_gallery','image','small_image','thumbnail'])
    header=['sku','colors','_store','_attribute_set','_type','_product_websites','color','cost','country_of_manufacture','created_at','custom_design','custom_design_from','custom_design_to','custom_layout_update','description','gallery','gift_message_available','has_options','image','image_label','media_gallery','meta_description','meta_keyword','meta_title','minimal_price','msrp','msrp_display_actual_price_type','msrp_enabled','name','news_from_date','news_to_date','options_container','page_layout','price','required_options','short_description','small_image','small_image_label','special_from_date','special_price','special_to_date','status','tax_class_id','thumbnail','thumbnail_label','visibility','weight','qty','is_in_stock','manage_stock','_tier_price_customer_group','_tier_price_qty','_tier_price_price','_tier_price_website','_group_price_customer_group','_group_price_price','_media_attribute_id','_media_image','_media_lable','_media_position','_media_is_disabled','_absolute_price','_absolute_weight','_sku_policy','_custom_option_store','_custom_option_type','_custom_option_title','_custom_option_is_required','_custom_option_price','_custom_option_sku','_custom_option_max_characters','_custom_option_sort_order','_custom_option_file_extension','_custom_option_image_size_x','_custom_option_image_size_y','_custom_option_template_id','_custom_option_view_mode','_custom_option_customoptions_is_onetime','_custom_option_show_swatch_title','_custom_option_image_path','_custom_option_customer_groups','_custom_option_store_views','_custom_option_qnty_input','_custom_option_in_group_id','_custom_option_is_dependent','_custom_option_div_class','_custom_option_image_mode','_custom_option_exclude_first_image','_custom_option_description','_custom_option_default_text','_custom_option_sku_policy','_custom_option_row_title','_custom_option_row_price','_custom_option_row_sort','_custom_option_row_sku','_custom_option_row_image_data','_custom_option_row_default','_custom_option_row_in_group_id','_custom_option_row_dependent_ids','_custom_option_row_weight','_custom_option_row_cost','_custom_option_row_special_data','_custom_option_row_tier_data','use_config_manage_stock','_super_products_sku','_super_attribute_code','_super_attribute_option','_super_attribute_price_corr','use_config_enable_qty_inc','use_config_qty_increments','use_config_max_sale_qty','use_config_notify_stock_qty','use_config_min_qty','use_config_backorders','use_config_min_sale_qty','min_qty','is_qty_decimal','backorders','min_sale_qty','max_sale_qty','stock_status_changed_auto','qty_increments','enable_qty_increments','is_decimal_divided','tiertabs','video','productofrente','productoaltura','productoprofundidad','productodiametro','productopeso','cartonfrente','cartonaltura','cartonprofundidad','cartonpieza','cartonpeso','empaque','manufacturer','sku_b']
    writer = csv.writer(open('bulletleeds.csv', 'wb'))
    writer.writerow(header)    
    
    
    customCSV=CustomCSV()
    customDriver = CustomDriver()
    index=0
    productIndex=0
#     for mainUrl in mainUrls:
    #driver=Firefox()
    #feed=Feed()
    #items=feed.read()
    #print "lend " +str(len(items))
    for item in glob.glob("C:/Users/carlos.espinosa/Documents/workspace/usb/src/*.html"):
        
        soup = BeautifulSoup(open(item), "html.parser") 
        print item
        _sku=soup.find('p',{'class':'product-style'}).text.strip()
        print _sku
        continue
        _brand=item['brand']
        rows=[]
        simplesSkus=[]
        rowsIndex=0
        productIndex+=1
#         if productIndex<20:
#             continue
        print str(productIndex)+" "+_sku
        if _brand == 'BL':
#             mainUrl='http://www.pcna.com/Bullet/en-us'
            brand="Bullet"
        elif _brand == 'LE':
#             mainUrl='http://www.pcna.com/Leeds/en-us'
            brand="Leeds"
        else:
            continue
#         mainUrl='http://www.pcna.com/en-us/'    
#         driver.get(mainUrl) 
# #         try:
#         searchbox=driver.find_element_by_id('SearchPhraseTextBox')
#         searchbox.clear()
# #         print _sku
#         searchbox.send_keys(_sku)
#         searchbox.send_keys(Keys.ENTER)
# #         except:
# #             continue
#         if check_exists_by_class('no-results',driver):
#             continue
#         productName=""
#         if check_exists_by_class('logo-and-title',driver):
#             productName=unicode(driver.find_element_by_class_name('logo-and-title').text.encode("utf-8", 'ignore'))
        
        print productName
#         price=0
#         if check_exists_by_id('table_Domestic',driver):
#             table_Domestic=driver.find_element_by_id('table_Domestic')
#             table_trs=table_Domestic.find_elements_by_tag_name('tr')
#             price=float(re.findall("\d+\.\d+",table_trs[1].find_elements_by_tag_name('td')[1].text)[0])*18.0*1.4
#         breadcrumbs=[]
#         if check_exists_by_class('wp-breadcrumb',driver):
#             wp_breadcrumb=driver.find_element_by_class_name('wp-breadcrumb')
#             for bread in wp_breadcrumb.find_elements_by_tag_name('a'):
#                 breadcrumbs.append(bread.text.encode("utf-8"))
#         categories="USA Partners/"+"/".join(breadcrumbs[-2:])
#         writerImagesCategories.writerow([_sku,categories])

        colors=[]
        try:
            regularcolors=driver.find_element_by_class_name('regular-colors')
        except:
#             writer.writerow([_sku,"Clearance"])
            continue
#         for color in regularcolors.find_elements_by_tag_name('a'):           
#             try:
#                 color.click()
#             except:
#                 continue                
#             data_colorname=color.get_attribute('data-colorname')
#             colorId=color.get_attribute('id').replace('color_swatch_box_','')
#             colors.append(colorId)
#             writerColors.writerow([colorId,colorId+" "+productName+" "+data_colorname])
#         writerColors.writerow([_sku,_sku+" "+productName])
        images=[]  
        for image in driver.find_element_by_class_name('all-images-thumbnails-slider').find_elements_by_tag_name('li'):
            img_src= image.find_element_by_tag_name('img').get_attribute('data-original')
            try:
                img_src.replace('medium','hires')
                img_name=img_src.split('/')[-2]+".jpg"
                images.append(img_name)
                index+=1
                writerImegesUpload.writerow([str(index),img_src,img_name])
            except:
                continue
#             _image="+"+images[0] if len(images)>0 else ''
#             writerImagesCategories.writerow([colorId,";".join(images),_image,_image,_image])
#             rowsimple=ROW('simple')
#             rows.insert(rowsIndex, rowsimple)
#             rows[rowsIndex].setSku(colorId)
#             rows[rowsIndex].setName(colorId+" "+productName+" "+data_colorname)
#             rows[rowsIndex].setColor(data_colorname)
#             rows[rowsIndex].setPrice('{0:.2f}'.format(price))
#             simplesSkus.append({'sku':colorId,'color':data_colorname})
#         for row in rows:
#             data=row.printRow()
#             writer.writerow(data)
#         
#         
#         rows=[]
#         rowsIndex=0
#         x=ROW('configurable')
#         rows.insert(rowsIndex, x)        
#         description,medidas,areasImpresion=customDriver.getInfo(driver)
#         description=description.encode("utf-8")
# #         writer.writerow([_sku,description,",".join(colors),medidas])
#         rows[rowsIndex].setBrand(brand)
#         rows[rowsIndex].setSku(_sku)
#         rows[rowsIndex].setDescription(description)
#         rows[rowsIndex].setShort_Description(description)
#         rows[rowsIndex].setName(_sku+" "+productName)
#         rows[rowsIndex].setPrice('{0:.2f}'.format(price))
#         for skus_index,_optionsku in enumerate(simplesSkus):
#             if skus_index>0:
#                 rowsIndex+=1
#                 x=ROW()
#                 rows.insert(rowsIndex, x)
#             _skuColor=_optionsku['sku']
#             _color=_optionsku['color']
#             rows[rowsIndex].set_Super_Products_Sku(_skuColor)
#             rows[rowsIndex].set_Super_Attribute_Code('color')
#             rows[rowsIndex].set_Super_Attribute_Option(_color)
#  
# 
#         for row in rows:
#             data=row.printRow()
#             writer.writerow(data)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        _file = open(brand+_sku+".html", "wb")
        _file.write(soup.prettify().encode('UTF-8'))        
        _file.close() 
        
#         print _sku,description,",".join(colors),medidas
#         for areaImpresion in areasImpresion:
#             writer.writerow([_sku,'','','',areaImpresion['name'],areaImpresion['description']])
             
        
#         except:
#             continue