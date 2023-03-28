import pytz
from odoo import models, fields
from odoo.http import request


time_zone_dhaka = pytz.timezone('Asia/Dhaka')


class AdmissionDateSelector(models.TransientModel):
    _name = 'se.admission.date.selector'

    status = fields.Selection(
        [
            ('all', 'All'),
            ('submit', 'Submit'),
            ('response', 'Responded'),
        ],
        string='Status',
        default='all'
    )

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def check_report(self):
        start_date = str(self.start_date)
        end_date = str(self.end_date)

        # # print(self.birth)
        # logging.info("PRINT = self.birth")
        filter_report = [('birth_date', '>=', start_date),
                         ('birth_date', '<=', end_date)]

        if self.status != 'all':
            filter_report.append(('status', '=', self.status))

        all_requisitions = request.env['se.student'].sudo().search(
            filter_report)

        all_reports = []
        for requisition in all_requisitions:
            report = {
                'birth_date': requisition.birth_date,
                'name': requisition.name,
                'email': requisition.email,
                'mobile':requisition.mobile,
                'blood_group':requisition.blood_group,
            }
            all_reports.append(report)

        return self.env.ref('se_education_core-main.report_admission_requisition') \
            .report_action(self, {'requisition': all_reports}, config=False)
