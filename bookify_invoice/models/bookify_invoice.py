from odoo import models,Command

class bookifyInvoice(models.Model):
    _inherit = 'book.bill'

    def create_invoice(self):
        print("AAAAAAAAAAAAAAAAa")
        self.env['account.move'].create({
            
            'partner_id': self.created_by_id.id,
            'move_type': 'out_invoice',
            'line_ids':[ Command.create({
                'name': self.user_name_id.name,
                'quantity': self.quantity,
                'price_unit': self.total_price,

            })]
        })
        # breakpoint()
        return super(bookifyInvoice,self).create_invoice()