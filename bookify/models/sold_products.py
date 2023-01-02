from odoo import models,fields

class soldProducts(models.Model):
    _name="sold.products"
    _description="Record of the sold products"

    sold_ids = fields.One2many('book.description' ,'product_id',string="sold products")
    user_ids = fields.One2many('user.description','user_id',string="info-of-user")
    salesperson_id = fields.Many2one('res.users', string="salesperson" , default = lambda self: self.env.user)
