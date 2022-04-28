from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 

class medical_patient(models.Model):
    
    _name = 'medical.patient'
    _rec_name = 'patient_id'
    _inherit = ["mail.thread", "mail.activity.mixin", 'utm.mixin']

    @api.onchange('patient_id')
    def _onchange_patient(self):
        '''
        The purpose of the method is to define a domain for the available
        purchase orders.
        '''
        address_id = self.patient_id
        self.partner_address_id = address_id

    @api.multi
    def print_report(self):
        return self.env.ref('basic_hms.report_print_patient_card').report_action(self)
#        Calculate Age
    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            else:
                rec.age = "No Date Of Birth!!"

    def invoices_button(self):
        return{
            'name': "Paid ",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'account.invoice',
            'view_id': self.env.ref('account.invoice_form').id,
            'context': {
                # 'default_partner_id': self.name.id,
                },
                'target': 'new',
                }
    

    def action_send_email(self):
        self.ensure_one()
        compose_form_id = False
        return {
            'name': 'Compose Email',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            }

    fees = fields.Float(string="Fees", default=150)
    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient", required= True)
    name = fields.Char(string='OP Number')
    last_name = fields.Char('Last Name')
    date_of_birth = fields.Date(string="Date of Birth", required= True)
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex", required= True)
    height = fields.Integer(string="Height in Cms")
    weight = fields.Integer(string="Weight in Kgs")
    bp = fields.Integer(string='BP in mmHg')
    occupation = fields.Char(string="Occupation")
    designation = fields.Char(string="Designation")
    father_name = fields.Char(string="Father / Husband Name")
    father_occupation = fields.Char(string="Occupation")
    office_address = fields.Char(string="Office Address")
    address = fields.Char(string="Address")
    treatment = fields.Char(string="Treatment for")
    duration_ailmenmts = fields.Char(string="Duration of Ailments")
    early_treatment = fields.Char(string="Early Treatments if any Furnish details")
    duration_treatment = fields.Char(string="Duration of Earlier Treatments taken")
    operations_details = fields.Char(string="Operation if any furnish details")
    feedback = fields.Boolean(string="How you came to know about Daisy Health Care (p) Ltd.,?")
    radio1 = fields.Boolean(string="News Paper")
    radio2 = fields.Boolean(string="Tv Program")
    radio3 = fields.Boolean(string="Vasanth TV")
    radio4 = fields.Boolean(string="Radio")
    radio5 = fields.Boolean(string="Magazine")
    radio6 = fields.Boolean(string="Sathiyam TV")
    radio7 = fields.Boolean(string="Our Employee")
    radio8 = fields.Boolean(string="Camp")
    radio9 = fields.Boolean(string="Polimer TV")
    radio10 = fields.Boolean(string="Friend / Referral")
    radio11 = fields.Boolean(string="Other")
    radio12 = fields.Boolean(string="YouTube")
    radio13 = fields.Boolean(string="Ref.Doctor")
    radio14 = fields.Boolean(string="Ad. Wall")
    radio15 = fields.Boolean(string="Puthuyugam TV")
    contact_no = fields.Char(string="Contact No", required= True)
    age = fields.Char(compute=onchange_age,string="Patient Age",store=True, required= True)
    primary_care_physician_id = fields.Many2one('medical.physician', string="Primary Care Doctor")
    photo = fields.Binary(string="Picture")
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    deceased = fields.Boolean(string='Deceased')

    @api.model
    def create(self,val):
        appointment = self._context.get('appointment_id')
        res_partner_obj = self.env['res.partner']
        if appointment:
            val_1 = {'name': self.env['res.partner'].browse(val['patient_id']).name}
            patient= res_partner_obj.create(val_1)
            val.update({'patient_id': patient.id})
        if val.get('date_of_birth'):
            dt = val.get('date_of_birth')
            d1 = datetime.strptime(str(dt), "%Y-%m-%d").date()
            d2 = datetime.today().date()
            rd = relativedelta(d2, d1)
            age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            val.update({'age':age} )

        patient_id  = self.env['ir.sequence'].next_by_code('medical.patient')
        if patient_id:
            val.update({
                        'name':patient_id,
                       })
        result = super(medical_patient, self).create(val)
        return result

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: