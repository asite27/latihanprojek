from odoo import api, fields, models


class kelompokBarang(models.Model):
    _name = 'audreymarket.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('cemilan', 'Cemilan'),
        ('makanan', 'Makanan'),
        ('minuman', 'Minuman')
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok Barang')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'cemilan':
            self.kode_kelompok = 'C100'
        elif self.name == 'makanan':
            self.kode_kelompok = 'M110'
        elif self.name == 'minuman':
            self.kode_kelompok = 'M111'

    kode_rak = fields.Char(string='Kode Rak')
    
    barang_ids = fields.One2many(comodel_name='audreymarket.barang',
                                inverse_name='kelompokbarang_id',
                                string='Daftar Barang')
            
    

    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['audreymarket.barang'].search([('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')