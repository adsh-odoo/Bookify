from odoo import models,fields

class bookCategoryModel(models.Model):
    _name="book.category"
    _description="category of the book"

    name=fields.Char(required=True)