from odoo import models,fields

class bookGenresModel(models.Model):
    _name= "book.genres"
    _description = "The category of the books"

    name = fields.Char(required=True)
    color = fields.Integer()
    book_ids = fields.One2many("book.description",'genres_id')