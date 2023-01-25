from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
class bookDescriptionModel(models.Model):
    _name="book.description"
    _description="description of the book"
    _order = "rating desc"

    name= fields.Char(required = True)
    # image = fields.Binary('Image')
    description= fields.Text()
    author_id=fields.Many2one('author.description')
    price=fields.Integer(required = True , string ="printed price")
    selling_price = fields.Float(compute ="_selling_price")
    tax = fields.Float(compute = "_tax_calculation")
    pages=fields.Integer(required = True)
    published_date=fields.Date('Published date', default = lambda self: fields.datetime.now()-relativedelta(months=6))
    type=fields.Selection(
        required=True,
        selection=[("new","New"),("old","Old")]
        )
    rating = fields.Integer(required = True,default =1 , store = True)
    publication = fields.Char()
    editions = fields.Char()
    genres_id=fields.Many2one('book.genres', string="Genres")
    category_ids=fields.Many2many('book.category')
    product_id = fields.Many2one('sold.products', string ="sold products")
    state = fields.Selection(string = "Availability",
        selection = [('new','New'),('queued','Queued'),('sold','Sold')]
    )
    stock = fields.Integer(default = 50)


    @api.depends("price")
    def _tax_calculation(self):
        for record in self:
            record.tax= 0.18*record.price
    
    @api.depends("price","tax")
    def _selling_price(self):
        for record in self:
            record.selling_price= record.price+record.tax



    # sql constraints
    _sql_constraints =[
        ('check_page_number', 'CHECK(pages>=0)',
        'total pages cannot be negative'),
        ('check_price' , 'CHECK(price>=0)',
        'price must be strictly positive'),
        ('check_rating' , 'CHECK(rating>=0 and rating<10)',
        'Please rate between 0 to 10')

    ]
    