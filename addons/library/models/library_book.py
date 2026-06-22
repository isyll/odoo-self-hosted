from odoo import fields, models


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"
    _order = "name"

    name = fields.Char(required=True)
    author = fields.Char()
    isbn = fields.Char(string="ISBN")
    published_date = fields.Date()
    category = fields.Selection(
        [
            ("fiction", "Fiction"),
            ("nonfiction", "Non-Fiction"),
            ("reference", "Reference"),
        ],
        default="fiction",
    )
    available = fields.Boolean(default=True)
    notes = fields.Text()
