from odoo  import models

class bookifyStockInventory(models.Model):
    _inherit = "bookify.stocks"

    def order_stock(self):
        print("AAAAAAAAAAAAAAAAAAAAAaa")
        self.env['stock.picking'].create(
            {
                
            }
        )
        return super(bookifyStockInventory,self).order_stock()
