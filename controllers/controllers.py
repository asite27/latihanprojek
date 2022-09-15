from odoo import http, models, fields
from odoo.http import request

import json

class Audreymarket(http.Controller):
    @http.route('/audreymarket/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        # Mengambil semua barang dari table barang
        barang = request.env['audreymarket.barang'].search([])
        brg = []

        for item in barang:
            brg.append({
                'nama_barang': item.name,
                'harga_jual': item.harga_jual,
                'stok': item.stok
            })
        return json.dumps(brg)

    @http.route('/audreymarket/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['audreymarket.supplier'].search([])
        pemasok = []

        for item in supplier:
            pemasok.append({
                'nama_perusahaan': item.name,
                'alamat': item.alamat,
                'no_telepon': item.no_telp,
                'barang_id': item.barang_id[0].name
            })
        return json.dumps(pemasok)