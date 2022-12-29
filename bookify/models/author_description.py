from odoo import models,fields

class authorDescription(models.Model):
    _name="author.description"
    _description="Descriptions of the author"

    name = fields.Char(required=True)
    date_of_birth = fields.Date('Date of Birth')
    age = fields.Integer()
    genres_ids = fields.Many2many('book.genres' , string="Genres")
    country = fields.Char()
    awards = fields.Char(string="Awards and Acolades")
    author_descriptions = fields.Text()
