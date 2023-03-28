from odoo import api, fields, models
from odoo.exceptions import ValidationError

class SeContact(models.Model):
    _name = 'se.contact'
    _description = 'SeContact'

    # name = fields.Char(string="Name")

    street = fields.Char(string="Street")
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    country = fields.Char(string='Country')
    state = fields.Char(string='State')
    zip = fields.Char(string='Zip')
    address_type_id = fields.Many2one('se.address.type', string="Address Type")
    student_id = fields.Many2one('se.student', string='Student_id')


class SeAddressType(models.Model):
    _name = "se.address.type"
    _description = "SmartEdu Address Type"

    name = fields.Char(string="Address Type")

