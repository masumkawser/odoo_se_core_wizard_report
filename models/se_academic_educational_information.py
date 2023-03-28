from odoo import models, fields, api
from odoo.exceptions import ValidationError

import datetime


class SeAcademicEducationalInformation(models.Model):
    _name = 'se.academic.educational.information'
    _description = 'Academic Educational Information'

    name = fields.Char()
    result_type = fields.Selection([
        ('gpa', 'GPA'),
        ('cgpa', 'CGPA'),
        ('grade', 'Grade'),
        ('division', 'Division'),
    ], string='Result Type', default='gpa')
    result_point = fields.Float(string='Result')
    result_division = fields.Selection([
        ('1st division', '1st Division'),
        ('2nd division', '2nd Division'),
        ('3rd division', '3rd Division')],
        string='Result')
    result_grade = fields.Selection(
        [('a+', 'A+'),
         ('b', 'B'),
         ('c', 'C')],
        string='Result_grade')
    institution_name = fields.Char(string='Institution Name')
    passing_year = fields.Selection(selection='_get_year_options', string='Passing Year')

    education_type_id = fields.Many2one('se.academic.education.type', string='Education Type')
    student_id = fields.Many2one('se.student', string='Student')

    # @api.onchange('result_type')
    # def onchange_method(self):
    #     if self.result_type == 'cgpa':
    #         self.result = fields.Selection(related='education_type_id.division_type', string='Result')
    #     else:
    #         self.result = fields.Float(string='Result')

    @api.constrains('result_type')
    def _check_point_limit(self):
        if self.result_type == 'cgpa':
            if self.result_point < 0.0:
                raise ValidationError("Point can't be add less then 0.0.")
            elif self.result_point > 4.0:
                raise ValidationError("Point can't be add more then 4.0.")

        elif self.result_type == 'gpa':
            if self.result_point < 0.0:
                raise ValidationError("Point can't be add less then 0.0.")
            elif self.result_point > 5.0:
                raise ValidationError("Point can't be add more then 5.0.")

    def _get_year_options(self):
        year_options = []
        current_year = fields.Date.today().year
        for year in range(1989, current_year+10):
            year_options.append((str(year), str(year)))
        return year_options

class SeAcademicEducationType(models.Model):
    _name = 'se.academic.education.type'
    _description = 'Academic Education Type'

    name = fields.Char(string='Education Type')
    active = fields.Boolean(string='Active')
    # division_type = fields.Selection([
    #     ('1st division', '1st Division')
    #     ('2nd division', '2nd Division')
    #     ('3rd division', '3rd Division')
    # ])
