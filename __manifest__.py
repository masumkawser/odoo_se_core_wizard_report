# -*- coding: utf-8 -*-
{
    'name': "SmartEdu Core",
    'summary': 'Manage Students, Faculties and Education Institute',
    'author': "DSL",
    'category': 'Education',
    'version': '0.1',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        # security
        'security/ir.model.access.csv',
        # Wizard
        'wizard/admission_report_date.xml',
        # views
        'views/se_student_view.xml',
        'views/se_address_type.xml',
        'views/se_menus.xml',
        'reports/report.xml',
        'reports/student_card.xml',
        'reports/admission_req.xml'
    ],
}
