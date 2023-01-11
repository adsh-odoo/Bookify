from odoo import models,fields,api

class authorDescription(models.Model):
    _name="author.description"
    _description="Descriptions of the author"

    name = fields.Char(required=True)
    date_of_birth = fields.Date('Date of Birth')
    age = fields.Integer()
    genres_ids = fields.Many2many('book.genres' , string="Genres")
    country = fields.Char()
    rating = fields.Integer()
    awards = fields.Char(string="Awards and Acolades")
    author_descriptions = fields.Text()
    total_books_ids = fields.One2many('book.description','author_id',string="Books")
    book_count = fields.Integer(compute = "_book_count" ,string ="Available books")


    # Sql costraints
    _sql_constraints = [
        ('check_authors_uniqness','unique(name)',
        'Author already exist in the database'),

        ('check_rating_condition' , 'CHECK(rating>=0 and rating<=10)',
        'Please rate between the 0 to 10')
    ]

    @api.depends("total_books_ids")
    def _book_count(self):
        for record in self:
            record.book_count = len(record.total_books_ids)
