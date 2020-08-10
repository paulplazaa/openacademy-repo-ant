from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description="openacademy of test"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
