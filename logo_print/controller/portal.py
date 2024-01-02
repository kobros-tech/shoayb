from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.addons.website_sale.controllers.main import WebsiteSale, WebsiteSaleForm
from odoo.http import request
from odoo import http
import base64
from PIL import Image
# from odoo.tools import groupby as groupbyelem
# from operator import itemgetter


class WeblearnsPortal(CustomerPortal):

    # display a value in template that has t-value "product_count"
    def _prepare_home_portal_values(self, counters):
        rtn = super(WeblearnsPortal, self)._prepare_home_portal_values(counters)
        rtn["products_count"] = request.env["product.product"].search_count([('is_published', '=', 'True')])
        print("RTN:.............", rtn["products_count"])
        return rtn


    # a controller that opens a tree view of products    
    @http.route(["/my/products", "/my/products/page/<int:page>"], type="http", website=True)
    def ProductsTemplatesListView(self, page=1, **kw):
        product_obj = request.env['product.product']
        all_products = product_obj.search_count([('is_published', '=', 'True')])
        page_details = pager(url="/my/products", total=all_products, page=page, step=3)

        products = product_obj.search(
            [('is_published', '=', 'True')], limit=3, offset=page_details['offset']
        )

        return request.render("logo.wb_products_list_view_portal", {
            'products': products,
            'page_name': "products_list_view",
            'pager': page_details,
        })


    # a controller that opens a form view for specific product
    @http.route(["/my/product/<model('product.product'):product>"], type='http', website=True)
    def ProductFormView(self, product, **kw):
        products = request.env['product.product'].search([('is_published', '=', 'True')])
        products_ids = products.ids
        product_index = products_ids.index(product.id)

        vals = {"product": product, "page_name": 'product_form_view', }

        if product_index !=0 and products_ids[product_index - 1]:
            vals['prev_record'] = "/my/product/{}".format(products_ids[product_index - 1])

        if product_index < len(products_ids) - 1 and products_ids[product_index + 1]:
            vals['next_record'] = "/my/product/{}".format(products_ids[product_index + 1])

        return request.render("logo.product_form_view_template", vals)
    

    @http.route(["/buy/product/"], type="http", method=["GET", "POST"], auth="user", website=True)
    def new_quotation(self, **kw):
        if request.httprequest.method == "POST":
            # read the image file object and then convert it to base64 byte object
            img_file = kw.get('a_document')
            img = base64.b64encode(img_file.read())

            request.env["product.template"].create({
                'name': kw.get('logo'),
                'image_1920': img,    
            })

            print("---------------------------------Success------------------------------------")
            print(img.decode('utf-8'))
        else:
            print("--------------------------GET Request")

        products = request.env['product.product'].search([('is_published', '=', 'True')])
        templates = request.env['product.template'].search([('is_published', '=', 'True')])
        attributes = request.env['product.attribute'].search([])
        variables = request.env['product.attribute.value'].search([])
        return request.render("logo.quotaion_form_view_template", {
            "products": products,
            "templates": templates,
            "attributes": attributes,
            "variables": variables,
        })



class LogoRecord(WebsiteSale):


    @http.route(['/shop/cart'], type='http', auth="public", website=True, sitemap=False)
    def cart(self, access_token=None, revive='', **post):
        
        result = super(LogoRecord, self).cart(access_token=None, revive='', **post)

        # sale order id
        order = request.website.sale_get_order()
        print(order)
        print(order.name)

        # customer        
        user = request.env.user
        print(f"{user.name}: ")

        # logo position
        position = post.get("order")

        print("-----------------------load-----------------------------")
        print("----------------------------------------------------")
        print("-------------------------GET---------------------------")
        print(order)
        print(position)
        print("----------------------------------------------------")
        print("----------------------------------------------------")

        return super(LogoRecord, self).cart(access_token=None, revive='', **post)

    
        
    @http.route(["/logo/form/"], type="http", method=["GET", "POST"], auth="user", website=True)
    def logo_upload(self, **kw):
        if request.httprequest.method == "POST":

            order = None
            order_line = None

            # values to be recorded in a new library logo object
            vals = {}

            # read the image file object and then convert it to base64 byte object
            try:    
                img_file = kw.get('a_document')
                img = base64.b64encode(img_file.read())
                vals['image'] = img

                print(img.decode('utf-8'))
            except:
                pass
            

            if kw.get('product_logo'):
                # product_id = int(kw.get('product_logo'))
                # vals['product_ids'] = product
                print(kw.get('product_logo'))
            
            if kw.get('describ_logo'):
                description = kw.get('describ_logo')
                vals['product_description'] = description
                print(description)

                
            if kw.get('order_logo'):
                order_line_str = kw.get('order_logo')

                # extra related to key value "yes"
                order_line = request.env['sale.order.line'].browse(int(order_line_str))
                print(order_line)

                order = order_line.order_id
                print(order)
                
                describ = order_line.get_description_following_lines()
                
                if "Extra_Printing: yes" in describ:
                    try:    
                        img2_file = kw.get('b_document')
                        img2 = base64.b64encode(img2_file.read())
                        vals['extra1'] = img2

                        print(img2.decode('utf-8'))
                    except:
                        pass
                
                # add the order to the library of logos
                
                # vals['order_ids'] = [(4, [order.id])]
                

            print("-------------------------------------------------------------------")
            print(vals)
            new_input = request.env["library"].create(vals)
            print(new_input)

            
            new_input.write({'order_ids': [(4, order_line.id)]})
            
            order.write({'library_ids': [(4, new_input.id)]})

            
            print("---------------------------------Success------------------------------------")
            print("---------------------------------Success------------------------------------")
            print("---------------------------------Success------------------------------------")
            print("---------------------------------Success------------------------------------")

            return request.redirect("/shop/cart")

        else:
            print("--------------------------GET Request")
            
            return request.redirect("/shop/cart")