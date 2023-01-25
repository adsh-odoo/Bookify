from odoo import models,fields,api

class booksBills(models.Model):
    _name= "book.bill"
    _description ="This is the model thst will store the bills  detail"

    ref = fields.Char("Refrence")
    user_name_id = fields.Many2one('user.description')
    book_name_id = fields.Many2one('book.description')
    user_id = fields.Char("user id" ,related = "user_name_id.id_user")
    quantity = fields.Integer("Quantity", default =1)
    printed_price = fields.Integer(related = "book_name_id.price")
    total_tax = fields.Float(compute =  "_total_tax")
    total_price = fields.Float(compute = "_total_price")
    date = fields.Date(default = fields.datetime.now())
    created_by_id  = fields.Many2one('res.partner') # for invoicing 


    @api.depends("book_name_id.tax","quantity")
    def _total_tax(self):
        for record in self:
            record.total_tax = record.book_name_id.tax * record.quantity
    
    @api.depends("total_tax" , "quantity")
    def _total_price(self):
        for record in self:
            record.total_price = record.total_tax + record.printed_price*record.quantity 
    

    # Generating the sequence for the bills
    @api.model
    def create(self,vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('bookify.bills')
        return super(booksBills,self).create(vals)

    def create_invoice(self):
        self.book_name_id.stock = self.book_name_id.stock-1
        x = self.book_name_id.stock
        # breakpoint()
