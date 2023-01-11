from odoo import models,fields,api
from odoo.exceptions import ValidationError


class userdescription(models.Model):
    _name="user.description"
    _description="description of the user"

    name = fields.Char(required=True)
    email_id = fields.Char("Email-id")
    mobile_no= fields.Char("MobileNo")
    Residential_address= fields.Text("Address")
    category_id = fields.Many2one('user.category', string="User Type")
    user_id = fields.Many2one('sold.products', string ="User-info")



    # python constrains

    @api.constrains("mobile_no")
    def _mobile_no_verification(self):
        for record in self:
            for rec in record.mobile_no:
                x= ord(rec)
                if x in range (48,58):
                    pass
                else:
                    raise ValidationError("invalid characters in mobile numbers")
        if len(record.mobile_no) != 10:
                raise ValidationError("mobile number should be of 10 digits")