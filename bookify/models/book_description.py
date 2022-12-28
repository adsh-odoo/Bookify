from odoo import models,fields
from dateutil.relativedelta import relativedelta
class bookDescriptionModel(models.Model):
    _name="book.description"
    _description="description of the book"

    name= fields.Char(required = True )
    description= fields.Text()
    author=fields.Char()
    price=fields.Integer(required = True)
    pages=fields.Integer(required = True)
    published_date=fields.Date('Published date', default = lambda self: fields.datetime.now()-relativedelta(months=6))
    type=fields.Selection(
        required=True,
        selection=[("new","New"),("old","Old")]
        )
    genres=fields.Many2one('book.genres', string="Genres")
    category=fields.Many2many('book.category')