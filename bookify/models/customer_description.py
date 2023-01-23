from odoo import models, fields,api


class customerDescription(models.Model):
    _name = "customer.description"
    _inherits = {'user.description':'user_desc'}
    _description = "models for storing the customers record"

    user_desc_id = fields.Many2one('user.description' ,string = "customer_description")
    book_name_id = fields.Many2one('book.description')

    # user_type= fields.Char(related = "user_desc.category_id.name" ,inherited = True, default = 1)

    # @api.multi
    def sold_order(self):
        print(self.book_name_id)
        self.env['bookify.stocks'].update_stock(self.book_name_id)

        # for record in self:
        #     print(record.book_name_id.stock_id)
        #     for rec in record.book_name_id.stock_id:
        #         print("hello")

            # print(record.book_name_id.stock_id.available_stock)
            # record.book_name_id.stock_id.available_stock = record.book_name_id.stock_id.available_stock-1
            