from odoo import api, fields, models

class Kedatanganbarang(models.TransientModel):
    _name = 'audreymarket.kedatanganbarang'

    barang_id = fields.Many2one(
        comodel_name='audreymarket.barang', 
        string='Nama Barang', 
        required=True)

    jumlah = fields.Integer(
        string='Jumlah', 
        required=False)

    def button_barang_datang(self):
        for line in self:
            self.env['audreymarket.barang'].search([('id', '=', line.barang_id.id)]).write(
                {'stok': line.barang_id.stok +  line.jumlah}
            )