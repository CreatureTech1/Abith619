from odoo import models, api, fields


class WhatsappSendMessage(models.TransientModel):

    _name = 'whatsapp.wizard'

    user_id = fields.Many2one('res.partner', string="Recipient")
    mobile = fields.Char(required=True,readonly=True)
    message = fields.Text(string="Message", required=True)

    def send_message(self):
        if self.message and self.mobile:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string) - 3)]
            return {
                'type': 'ir.actions.act_url',
                'url': "https://api.whatsapp.com/send?phone="+self.mobile+"&text=" + message_string,
                'target': 'new',
                'res_id': self.id,
                
            }