from odoo import models,fields

class userCategory(models.Model):
    _name ="user.category"
    _description="category of the user"

    name = fields.Char(required=True)

