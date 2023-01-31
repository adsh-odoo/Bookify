from odoo import models,fields

class bookCategoryModel(models.Model):
    _name="book.category"
    _description="category of the book"

    name=fields.Char(required=True)
    color = fields.Integer()
    book_ids = fields.One2many('book.description','category_ids')