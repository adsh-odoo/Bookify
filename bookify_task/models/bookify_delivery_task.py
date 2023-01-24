from odoo import models

class bookifyDeliveryTask(models.Model):
    _inherit = "customer.description"

    def sold_order(self):
        desc = ""
        print("AAAAAAAAAAAAAAAAAAA")
        self.env['project.task'].create(
            {
                'name' : self.name,
                'project_id':4,
                'description':self.Residential_address
            }
        )

        
        return super().sold_order()
