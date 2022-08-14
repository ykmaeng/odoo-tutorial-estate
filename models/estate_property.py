from datetime import datetime
from email.policy import default
from odoo import api, fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(required=True)
    tag_ids = fields.Many2many("estate.property.tag")
    description = fields.Text()

    property_type_id = fields.Many2one(
        'estate.property.type', string='Property Type')

    postcode = fields.Char()
    date_availability = fields.Date(default=datetime.today(), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')],
        help="This is helpful message"
    )
    state = fields.Selection(
        selection=[('new', 'New'), ('offer_received', 'Offer Received'),
                   ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new',
        help="This is helpful message"
    )
    buyer = fields.Many2one('res.users', string='Buyer',
                            index=True, default=lambda self: self.env.user)
    salesperson = fields.Many2one('res.users', string='Salesperson',
                                  index=True, default=lambda self: self.env.user)
    offer_ids = fields.One2many(
        'estate.property.offer', 'property_id', string='Offers')
    active = fields.Boolean(default=True)
