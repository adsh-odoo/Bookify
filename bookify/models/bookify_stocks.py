from odoo import models,fields,api
# from dateutil.relativedelta import relativedelta


class bookifyStocks(models.Model):
    _name ="bookify.stocks"
    _description = "This is stocks description model"

    book_description_id = fields.Many2one('book.description')
    author_name= fields.Char("Author" , related = "book_description_id.author_id.name")
    rating = fields.Integer(related ="book_description_id.rating" ,default =1)
    available_stock = fields.Integer("Available in stocks",default = 100)
    expected_replenishment = fields.Integer(compute = "_expected_days")
    supplier_detail_ids = fields.One2many('user.description','stocks_id')



    
    @api.depends("rating","available_stock")
    def _expected_days(self):
        for record in self:
            # if record.book_description_id:
            record.expected_replenishment = record.available_stock/record.rating
            # else:
            #     record.rating =1

         



   