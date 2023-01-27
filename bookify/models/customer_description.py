from odoo import models, fields,Command


class customerDescription(models.Model):
    _name = "customer.description"
    _inherits = {'user.description':'user_desc_id'}
    _description = "models for storing the customers record"

    user_desc_id = fields.Many2one('user.description' ,string = "customer_description" )
    book_name_id = fields.Many2one('book.description')
    salesperson_id = fields.Many2one('res.users' ,default = lambda self: self.env.user)

    # user_type= fields.Char(related = "user_desc.category_id.name" ,inherited = True, default = 1)

    # @api.multi
    def sold_order(self):
        print("AAAAAAAAAAAAAAAaa")
        self.env['sold.products'].create(
            {
               'salesperson_id': self.salesperson_id.id,
               'sold_ids' :[ Command.create({
                'name': self.book_name_id.name,
                'author_id':self.book_name_id.author_id.id,
                'price':self.book_name_id.price,
                'pages': self.book_name_id.pages,
                'type': self.book_name_id.type,
                'rating': self.book_name_id.rating,
                # 'category_ids':self.book_name_id.category_ids,
                'genres_id':self.book_name_id.genres_id.id,

            })
            ],
            'user_ids':[
                 Command.create({
                    'name':self.user_desc_id.name,
                    'mobile_no': self.user_desc_id.mobile_no,
                    'email_id':self.user_desc_id.email_id,
                    # 'id_user': self.user_desc_id.id_user,
                
            })
            ]
            
            }
            
        )
        breakpoint()

        # for record in self:
        #     print(record.book_name_id.stock_id)
        #     for rec in record.book_name_id.stock_id:
        #         print("hello")

            # print(record.book_name_id.stock_id.available_stock)
            # record.book_name_id.stock_id.available_stock = record.book_name_id.stock_id.available_stock-1
            