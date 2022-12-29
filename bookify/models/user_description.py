from odoo import models,fields

class userdescription(models.Model):
    _name="user.description"
    _description="description of the user"

    name = fields.Char(required=True)
    email_id = fields.Char("Email-id")
    mobile_no= fields.Integer("MobileNo")
    Residential_address= fields.Text("Address")
    category_id = fields.Many2one('user.category', string="User Type")
