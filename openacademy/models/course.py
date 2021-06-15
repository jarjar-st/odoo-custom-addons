# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    __description = "OpenAcademy.Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

# class openacademy(models.Model):
#     _name= 'openacademy.openacademy'

#     name = fields.Char()  