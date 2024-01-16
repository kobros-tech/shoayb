from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.addons.website_sale.controllers.main import WebsiteSale, WebsiteSaleForm
from odoo.http import request, Response
from odoo import http
import json
import base64
from PIL import Image


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

    
    def logo_description(self, line):
        description = line.get_description_following_lines()

        descrip_dict = {}
        for i in description:
            key_value = i.split(":")
            if len(key_value) == 2:
                descrip_dict[key_value[0]] = key_value[1].strip()
        
        return descrip_dict


    @http.route(["/logo/post/<model('sale.order.line'):line>"], type="http", method=["POST"], auth="public", csrf=False, cors='*')
    def post_logo_upload(self, line, **kw):

        print("************************JSON************************")
        data = json.loads(request.httprequest.data)
        
        print(type(data))
        print(data["logo_position"])
        print("************************JSON************************")


        headers = {'Content-Type': 'application/json'}

        body = self.logo_description(line)
        print(body)

        return Response(json.dumps(body), headers=headers)

    
    @http.route(["/logo/get/<model('sale.order.line'):line>"], type="http", method=["GET"], auth="public", cors='*')
    def get_logo_upload(self, line, **kw):
        body = self.logo_description(line)
        
        print("****************************************")
        print(body)
        print("****************************************")
        headers = {'Content-Type': 'application/json'}
        
        return Response(json.dumps(body), headers=headers)

