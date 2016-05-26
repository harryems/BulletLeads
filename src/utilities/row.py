# -*- coding: utf-8 -*-

class ROW(object):
    
    def __init__(self,_type=None):
        self.sku=''
        self.sku_b=''
        self._store=''
        self._attribute_set=''
        self._type=''
        self._category=''
        self._root_category=''
        self._product_websites=''
        self.color=''
        self.cost=''
        self.country_of_manufacture=''
        self.created_at=''
        self.custom_design=''
        self.custom_design_from=''
        self.custom_design_to=''
        self.custom_layout_update=''
        self.description=''
        self.gallery=''
        self.gift_message_available=''
        self.has_options=''
        self.image=''
        self.image_label=''
        self.manufacturer=''
        self.media_gallery=''
        self.meta_description=''
        self.meta_keyword=''
        self.meta_title=''
        self.minimal_price=''
        self.msrp=''
        self.msrp_display_actual_price_type=''
        self.msrp_enabled=''
        self.name=''
        self.news_from_date=''
        self.news_to_date=''
        self.options_container=''
        self.page_layout=''
        self.price=''
        self.required_options=''
        self.short_description=''
        self.small_image=''
        self.small_image_label=''
        self.special_from_date=''
        self.special_price=''
        self.special_to_date=''
        self.status=''
        self.tax_class_id=''
        self.thumbnail=''
        self.thumbnail_label=''
        self.visibility=''
        self.weight=''
        self.qty=''
        self.is_in_stock=''
        self.manage_stock=''
        self._tier_price_customer_group=''
        self._tier_price_qty=''
        self._tier_price_price=''
        self._tier_price_website=''
        self._group_price_customer_group=''
        self._group_price_price=''
        self._media_attribute_id=''
        self._media_image=''
        self._media_lable=''
        self._media_position=''
        self._media_is_disabled=''
        self._absolute_price=''
        self._absolute_weight=''
        self._sku_policy=''
        self._custom_option_store=''
        self._custom_option_type=''
        self._custom_option_title=''
        self._custom_option_is_required=''
        self._custom_option_price=''
        self._custom_option_sku=''
        self._custom_option_max_characters=''
        self._custom_option_sort_order=''
        self._custom_option_file_extension=''
        self._custom_option_image_size_x=''
        self._custom_option_image_size_y=''
        self._custom_option_template_id=''
        self._custom_option_view_mode=''
        self._custom_option_customoptions_is_onetime=''
        self._custom_option_show_swatch_title=''
        self._custom_option_image_path=''
        self._custom_option_customer_groups=''
        self._custom_option_store_views=''
        self._custom_option_qnty_input=''
        self._custom_option_in_group_id=''
        self._custom_option_is_dependent=''
        self._custom_option_div_class=''
        self._custom_option_image_mode=''
        self._custom_option_exclude_first_image=''
        self._custom_option_description=''
        self._custom_option_default_text=''
        self._custom_option_sku_policy=''
        self._custom_option_row_title=''
        self._custom_option_row_price=''
        self._custom_option_row_sku=''
        self._custom_option_row_image_data=''
        self._custom_option_row_default=''
        self._custom_option_row_in_group_id=''
        self._custom_option_row_dependent_ids=''
        self._custom_option_row_weight=''
        self._custom_option_row_cost=''
        self._custom_option_row_special_data=''
        self._custom_option_row_tier_data=''
        self.use_config_manage_stock=''
        self.colors=''
        self._super_products_sku=''
        self._super_attribute_code=''
        self._super_attribute_option=''
        self._super_attribute_price_corr=''
        self.use_config_enable_qty_inc=''
        self.use_config_qty_increments=''
        self.use_config_max_sale_qty=''
        self.use_config_notify_stock_qty=''
        self.use_config_min_qty=''
        self.use_config_backorders=''
        self.use_config_min_sale_qty=''
        self.min_qty=''
        self.is_qty_decimal=''
        self.backorders=''
        self.min_sale_qty=''
        self.max_sale_qty=''
        self.stock_status_changed_auto=''
        self.qty_increments=''
        self.enable_qty_increments=''
        self.is_decimal_divided=''
        self.tiertabs=''
        self.Video=''
        self.ProductoFrente=''
        self.ProductoAltura=''
        self.ProductoProfundidad=''
        self.ProductoDiametro=''
        self.ProductoPeso=''
        self.CartonFrente=''
        self.CartonAltura=''
        self.CartonProfundidad=''
        self.CartonPieza=''
        self.CartonPeso=''
        self.Empaque=''
        self.Property01=''
        self.Property02=''
        self.Property03=''
        self.Property04=''
        self.Property05=''
        self.Property06=''
        self.Property07=''
        self.Property08=''
        self.Property09=''
        self.Property10=''
        self.Property11=''
        self.Property12=''
        self.AreasFiltro=''
        self._custom_option_row_sort=''
        self.brand=''

        if _type=='configurable' or _type=='simple':
            self._attribute_set='Default'
            self._type='simple'
            self._root_category='Default Category'
            self._product_websites='base'
            self.created_at='2015-10-19 14:28:59'  
            self.has_options='1'
            self.options_container='Product Info Column'
            self.required_options='1'
            self.status='1'
            self.tax_class_id='2'            
            self._media_is_disabled='0'
            self._absolute_price='0'
            self._absolute_weight='0'
            self._sku_policy='4'
            self.visibility='4'
            self.msrp_display_actual_price_type='Use config'
            self.msrp_enabled='Use config'
            self.weight='1.000'
            self.manage_stock='0'
            self.is_in_stock='1'
            self.manage_stock='0'
            self.use_config_manage_stock='0'
            self.use_config_enable_qty_inc='1'
            self.use_config_qty_increments='1'
            self.use_config_max_sale_qty='1'
            self.use_config_notify_stock_qty='1'
            self.use_config_min_qty='1'
            self.use_config_backorders='1'
            self.use_config_min_sale_qty='1'
            self.min_qty='0'
            self.is_qty_decimal='0'
            self.backorders='0'
            self.min_sale_qty='0'
            self.max_sale_qty='0'
            self.stock_status_changed_auto='0'
            self.qty_increments='0'
            self.enable_qty_increments='0'
            self.is_decimal_divided='0'
        if _type=='configurable':
            self._type='configurable'
        if _type=='simple':
            self.manage_stock='1'
            self.use_config_manage_stock='0'
            self.visibility='1'
    def set_custom_option_row_sort(self,_custom_option_row_sort):
        self._custom_option_row_sort=_custom_option_row_sort
    def setSkub(self,sku_b):
        self.sku_b=sku_b
    def setBrand(self,brand):
        self.brand=brand
    def setVideo(self,Video):
        self.Video=Video
    def setProductoFrente(self,ProductoFrente):
        self.ProductoFrente=ProductoFrente
    def setProductoAltura(self,ProductoAltura):
        self.ProductoAltura=ProductoAltura                            
            
    def setProductoProfundidad(self,ProductoProfundidad):
        self.ProductoProfundidad=ProductoProfundidad
    def setProductoDiametro(self,ProductoDiametro):
        self.ProductoDiametro=ProductoDiametro
    def setProductoPeso(self,ProductoPeso):
        self.ProductoPeso=ProductoPeso   
    def setTecnicadecoracion(self,AreasFiltro):
        self.AreasFiltro=AreasFiltro     
    def setCartonFrente(self,CartonFrente):
        self.CartonFrente=CartonFrente
    def setCartonAltura(self,CartonAltura):
        self.CartonAltura=CartonAltura
    def setCartonProfundidad(self,CartonProfundidad):
        self.CartonProfundidad=CartonProfundidad                       

    def setCartonPieza(self,CartonPieza):
        self.CartonPieza=CartonPieza
    def setCartonPeso(self,CartonPeso):
        self.CartonPeso=CartonPeso
    def setEmpaque(self,Empaque):
        self.Empaque=Empaque   
            
    def setTiertabs(self,html):
        self.tiertabs=html     
    def setSku(self,sku):
        self.sku=sku
    def setColors(self,colors):
        self.colors=colors
    def set_Store(self,_store):
        self._store=_store
    def set_Attribute_Set(self,_attribute_set):
        self._attribute_set=_attribute_set
    def set_Type(self,_type):
        self._type=_type
    def set_Category(self,_category):
        self._category=_category
    def set_Root_Category(self,_root_category):
        self._root_category=_root_category
    def set_Product_Websites(self,_product_websites):
        self._product_websites=_product_websites
    def setColor(self,color):
        self.color=color
    def setCost(self,cost):
        self.cost=cost
    def setCountry_Of_Manufacture(self,country_of_manufacture):
        self.country_of_manufacture=country_of_manufacture
    def setCreated_At(self,created_at):
        self.created_at=created_at
    def setCustom_Design(self,custom_design):
        self.custom_design=custom_design
    def setCustom_Design_From(self,custom_design_from):
        self.custom_design_from=custom_design_from
    def setCustom_Design_To(self,custom_design_to):
        self.custom_design_to=custom_design_to
    def setCustom_Layout_Update(self,custom_layout_update):
        self.custom_layout_update=custom_layout_update
    def setDescription(self,description):
        self.description=description.decode('utf8')
    def setGallery(self,gallery):
        self.gallery=gallery
    def setGift_Message_Available(self,gift_message_available):
        self.gift_message_available=gift_message_available
    def setHas_Options(self,has_options):
        self.has_options=has_options
    def setImage(self,image):
        self.image=image
    def setImage_Label(self,image_label):
        self.image_label=image_label
    def setManufacturer(self,manufacturer):
        self.manufacturer=manufacturer
    def setMedia_Gallery(self,media_gallery):
        self.media_gallery=media_gallery
    def setMeta_Description(self,meta_description):
        self.meta_description=meta_description
    def setMeta_Keyword(self,meta_keyword):
        self.meta_keyword=meta_keyword
    def setMeta_Title(self,meta_title):
        self.meta_title=meta_title
    def setMinimal_Price(self,minimal_price):
        self.minimal_price=minimal_price
    def setMsrp(self,msrp):
        self.msrp=msrp
    def setMsrp_Display_Actual_Price_Type(self,msrp_display_actual_price_type):
        self.msrp_display_actual_price_type=msrp_display_actual_price_type
    def setMsrp_Enabled(self,msrp_enabled):
        self.msrp_enabled=msrp_enabled
    def setName(self,name):
        self.name=name.decode('utf8')
    def setNews_From_Date(self,news_from_date):
        self.news_from_date=news_from_date
    def setNews_To_Date(self,news_to_date):
        self.news_to_date=news_to_date
    def setOptions_Container(self,options_container):
        self.options_container=options_container
    def setPage_Layout(self,page_layout):
        self.page_layout=page_layout
    def setPrice(self,price):
        self.price=price
    def setRequired_Options(self,required_options):
        self.required_options=required_options
    def setShort_Description(self,short_description):
        self.short_description=short_description.decode('utf8')
    def setSmall_Image(self,small_image):
        self.small_image=small_image
    def setSmall_Image_Label(self,small_image_label):
        self.small_image_label=small_image_label
    def setSpecial_From_Date(self,special_from_date):
        self.special_from_date=special_from_date
    def setSpecial_Price(self,special_price):
        self.special_price=special_price
    def setSpecial_To_Date(self,special_to_date):
        self.special_to_date=special_to_date
    def setStatus(self,status):
        self.status=status
    def setTax_Class_Id(self,tax_class_id):
        self.tax_class_id=tax_class_id
    def setThumbnail(self,thumbnail):
        self.thumbnail=thumbnail
    def setThumbnail_Label(self,thumbnail_label):
        self.thumbnail_label=thumbnail_label
    def setVisibility(self,visibility):
        self.visibility=visibility
    def setWeight(self,weight):
        self.weight=weight
    def setQty(self,qty):
        self.qty=qty
    def setIs_In_Stock(self,is_in_stock):
        self.is_in_stock=is_in_stock
    def setManage_Stock(self,manage_stock):
        self.manage_stock=manage_stock
    def set_Tier_Price_Customer_Group(self,_tier_price_customer_group):
        self._tier_price_customer_group=_tier_price_customer_group
    def set_Tier_Price_Qty(self,_tier_price_qty):
        self._tier_price_qty=_tier_price_qty
    def set_Tier_Price_Price(self,_tier_price_price):
        self._tier_price_price=_tier_price_price
    def set_Tier_Price_Website(self,_tier_price_website):
        self._tier_price_website=_tier_price_website
    def set_Group_Price_Customer_Group(self,_group_price_customer_group):
        self._group_price_customer_group=_group_price_customer_group
    def set_Group_Price_Price(self,_group_price_price):
        self._group_price_price=_group_price_price
    def set_Media_Attribute_Id(self,_media_attribute_id):
        self._media_attribute_id=_media_attribute_id
    def set_Media_Image(self,_media_image):
        self._media_image=_media_image
    def set_Media_Lable(self,_media_lable):
        self._media_lable=_media_lable
    def set_Media_Position(self,_media_position):
        self._media_position=_media_position
    def set_Media_Is_Disabled(self,_media_is_disabled):
        self._media_is_disabled=_media_is_disabled
    def set_Absolute_Price(self,_absolute_price):
        self._absolute_price=_absolute_price
    def set_Absolute_Weight(self,_absolute_weight):
        self._absolute_weight=_absolute_weight
    def set_Sku_Policy(self,_sku_policy):
        self._sku_policy=_sku_policy
    def set_Custom_Option_Store(self,_custom_option_store):
        self._custom_option_store=_custom_option_store
    def set_Custom_Option_Type(self,_custom_option_type):
        self._custom_option_type=_custom_option_type
    def set_Custom_Option_Title(self,_custom_option_title):
        self._custom_option_title=_custom_option_title
    def set_Custom_Option_Is_Required(self,_custom_option_is_required):
        self._custom_option_is_required=_custom_option_is_required
    def set_Custom_Option_Price(self,_custom_option_price):
        self._custom_option_price=_custom_option_price
    def set_Custom_Option_Sku(self,_custom_option_sku):
        self._custom_option_sku=_custom_option_sku
    def set_Custom_Option_Max_Characters(self,_custom_option_max_characters):
        self._custom_option_max_characters=_custom_option_max_characters
    def set_Custom_Option_Sort_Order(self,_custom_option_sort_order):
        self._custom_option_sort_order=_custom_option_sort_order
    def set_Custom_Option_File_Extension(self,_custom_option_file_extension):
        self._custom_option_file_extension=_custom_option_file_extension
    def set_Custom_Option_Image_Size_X(self,_custom_option_image_size_x):
        self._custom_option_image_size_x=_custom_option_image_size_x
    def set_Custom_Option_Image_Size_Y(self,_custom_option_image_size_y):
        self._custom_option_image_size_y=_custom_option_image_size_y
    def set_Custom_Option_Template_Id(self,_custom_option_template_id):
        self._custom_option_template_id=_custom_option_template_id
    def set_Custom_Option_View_Mode(self,_custom_option_view_mode):
        self._custom_option_view_mode=_custom_option_view_mode
    def set_Custom_Option_Customoptions_Is_Onetime(self,_custom_option_customoptions_is_onetime):
        self._custom_option_customoptions_is_onetime=_custom_option_customoptions_is_onetime
    def set_Custom_Option_Show_Swatch_Title(self,_custom_option_show_swatch_title):
        self._custom_option_show_swatch_title=_custom_option_show_swatch_title
    def set_Custom_Option_Image_Path(self,_custom_option_image_path):
        self._custom_option_image_path=_custom_option_image_path
    def set_Custom_Option_Customer_Groups(self,_custom_option_customer_groups):
        self._custom_option_customer_groups=_custom_option_customer_groups
    def set_Custom_Option_Store_Views(self,_custom_option_store_views):
        self._custom_option_store_views=_custom_option_store_views
    def set_Custom_Option_Qnty_Input(self,_custom_option_qnty_input):
        self._custom_option_qnty_input=_custom_option_qnty_input
    def set_Custom_Option_In_Group_Id(self,_custom_option_in_group_id):
        self._custom_option_in_group_id=_custom_option_in_group_id
    def set_Custom_Option_Is_Dependent(self,_custom_option_is_dependent):
        self._custom_option_is_dependent=_custom_option_is_dependent
    def set_Custom_Option_Div_Class(self,_custom_option_div_class):
        self._custom_option_div_class=_custom_option_div_class
    def set_Custom_Option_Image_Mode(self,_custom_option_image_mode):
        self._custom_option_image_mode=_custom_option_image_mode
    def set_Custom_Option_Exclude_First_Image(self,_custom_option_exclude_first_image):
        self._custom_option_exclude_first_image=_custom_option_exclude_first_image
    def set_Custom_Option_Description(self,_custom_option_description):
        self._custom_option_description=_custom_option_description
    def set_Custom_Option_Default_Text(self,_custom_option_default_text):
        self._custom_option_default_text=_custom_option_default_text
    def set_Custom_Option_Sku_Policy(self,_custom_option_sku_policy):
        self._custom_option_sku_policy=_custom_option_sku_policy
    def set_Custom_Option_Row_Title(self,_custom_option_row_title):
        self._custom_option_row_title=_custom_option_row_title
    def set_Custom_Option_Row_Price(self,_custom_option_row_price):
        self._custom_option_row_price=_custom_option_row_price
    def set_Custom_Option_Row_Sku(self,_custom_option_row_sku):
        self._custom_option_row_sku=_custom_option_row_sku
    def set_Custom_Option_Row_Image_Data(self,_custom_option_row_image_data):
        self._custom_option_row_image_data=_custom_option_row_image_data
    def set_Custom_Option_Row_Default(self,_custom_option_row_default):
        self._custom_option_row_default=_custom_option_row_default
    def set_Custom_Option_Row_In_Group_Id(self,_custom_option_row_in_group_id):
        self._custom_option_row_in_group_id=_custom_option_row_in_group_id
    def set_Custom_Option_Row_Dependent_Ids(self,_custom_option_row_dependent_ids):
        self._custom_option_row_dependent_ids=_custom_option_row_dependent_ids
    def get_Custom_Option_Row_Dependent_Ids(self):
        return self._custom_option_row_dependent_ids    
    def set_Custom_Option_Row_Weight(self,_custom_option_row_weight):
        self._custom_option_row_weight=_custom_option_row_weight
    def set_Custom_Option_Row_Cost(self,_custom_option_row_cost):
        self._custom_option_row_cost=_custom_option_row_cost
    def set_Custom_Option_Row_Special_Data(self,_custom_option_row_special_data):
        self._custom_option_row_special_data=_custom_option_row_special_data
    def set_Custom_Option_Row_Tier_Data(self,_custom_option_row_tier_data):
        self._custom_option_row_tier_data=_custom_option_row_tier_data
    def set_Super_Products_Sku(self,_super_products_sku):
        self._super_products_sku=_super_products_sku
    def set_Super_Attribute_Code(self,_super_attribute_code):
        self._super_attribute_code=_super_attribute_code
    def set_Super_Attribute_Option(self,_super_attribute_option):
        self._super_attribute_option=_super_attribute_option

        
    def __set__(self, obj, value):
#         if self.fset is None:
#             raise AttributeError("can't set attribute")
        self.fset(obj, value)    
#     def setValue(self,attribute,value):
#         setattr(self,attribute,value)
    def printRow(self):
        
        return [self.sku,self.colors,self._store,self._attribute_set,self._type,self._product_websites,self.color,self.cost,self.country_of_manufacture,self.created_at,self.custom_design,self.custom_design_from,self.custom_design_to,self.custom_layout_update,self.description,self.gallery,self.gift_message_available,self.has_options,self.image,self.image_label,self.media_gallery,self.meta_description,self.meta_keyword,self.meta_title,self.minimal_price,self.msrp,self.msrp_display_actual_price_type,self.msrp_enabled,self.name,self.news_from_date,self.news_to_date,self.options_container,self.page_layout,self.price,self.required_options,self.short_description,self.small_image,self.small_image_label,self.special_from_date,self.special_price,self.special_to_date,self.status,self.tax_class_id,self.thumbnail,self.thumbnail_label,self.visibility,self.weight,self.qty,self.is_in_stock,self.manage_stock,self._tier_price_customer_group,self._tier_price_qty,self._tier_price_price,self._tier_price_website,self._group_price_customer_group,self._group_price_price,self._media_attribute_id,self._media_image,self._media_lable,self._media_position,self._media_is_disabled,self._absolute_price,self._absolute_weight,self._sku_policy,self._custom_option_store,self._custom_option_type,self._custom_option_title,self._custom_option_is_required,self._custom_option_price,self._custom_option_sku,self._custom_option_max_characters,self._custom_option_sort_order,self._custom_option_file_extension,self._custom_option_image_size_x,self._custom_option_image_size_y,self._custom_option_template_id,self._custom_option_view_mode,self._custom_option_customoptions_is_onetime,self._custom_option_show_swatch_title,self._custom_option_image_path,self._custom_option_customer_groups,self._custom_option_store_views,self._custom_option_qnty_input,self._custom_option_in_group_id,self._custom_option_is_dependent,self._custom_option_div_class,self._custom_option_image_mode,self._custom_option_exclude_first_image,self._custom_option_description,self._custom_option_default_text,self._custom_option_sku_policy,self._custom_option_row_title,self._custom_option_row_price,self._custom_option_row_sort,self._custom_option_row_sku,self._custom_option_row_image_data,self._custom_option_row_default,self._custom_option_row_in_group_id,self._custom_option_row_dependent_ids,self._custom_option_row_weight,self._custom_option_row_cost,self._custom_option_row_special_data,self._custom_option_row_tier_data,self.use_config_manage_stock,self._super_products_sku,self._super_attribute_code,self._super_attribute_option,self._super_attribute_price_corr,self.use_config_enable_qty_inc,self.use_config_qty_increments,self.use_config_max_sale_qty,self.use_config_notify_stock_qty,self.use_config_min_qty,self.use_config_backorders,self.use_config_min_sale_qty,self.min_qty,self.is_qty_decimal,self.backorders,self.min_sale_qty,self.max_sale_qty,self.stock_status_changed_auto,self.qty_increments,self.enable_qty_increments,self.is_decimal_divided,self.tiertabs,self.Video,self.ProductoFrente,self.ProductoAltura,self.ProductoProfundidad,self.ProductoDiametro,self.ProductoPeso,self.CartonFrente,self.CartonAltura,self.CartonProfundidad,self.CartonPieza,self.CartonPeso,self.Empaque,self.brand,self.sku_b]
    def printHeader(self):
        return ['sku','_store','_attribute_set','_type','_category','_root_category','_product_websites','color','cost','country_of_manufacture','created_at','custom_design','custom_design_from','custom_design_to','custom_layout_update','description','gallery','gift_message_available','has_options','image','image_label','manufacturer','media_gallery','meta_description','meta_keyword','meta_title','minimal_price','msrp','msrp_display_actual_price_type','msrp_enabled','name','news_from_date','news_to_date','options_container','page_layout','price','required_options','short_description','small_image','small_image_label','special_from_date','special_price','special_to_date','status','tax_class_id','thumbnail','thumbnail_label','visibility','weight','qty','is_in_stock','manage_stock','_tier_price_customer_group','_tier_price_qty','_tier_price_price','_tier_price_website','_group_price_customer_group','_group_price_price','_media_attribute_id','_media_image','_media_lable','_media_position','_media_is_disabled','_absolute_price','_absolute_weight','_sku_policy','_custom_option_store','_custom_option_type','_custom_option_title','_custom_option_is_required','_custom_option_price','_custom_option_sku','_custom_option_max_characters','_custom_option_sort_order','_custom_option_file_extension','_custom_option_image_size_x','_custom_option_image_size_y','_custom_option_template_id','_custom_option_view_mode','_custom_option_customoptions_is_onetime','_custom_option_show_swatch_title','_custom_option_image_path','_custom_option_customer_groups','_custom_option_store_views','_custom_option_qnty_input','_custom_option_in_group_id','_custom_option_is_dependent','_custom_option_div_class','_custom_option_image_mode','_custom_option_exclude_first_image','_custom_option_description','_custom_option_default_text','_custom_option_sku_policy','_custom_option_row_title','_custom_option_row_price','_custom_option_row_sku','_custom_option_row_image_data','_custom_option_row_default','_custom_option_row_in_group_id','_custom_option_row_dependent_ids','_custom_option_row_weight','_custom_option_row_cost','_custom_option_row_special_data','_custom_option_row_tier_data','use_config_manage_stock']