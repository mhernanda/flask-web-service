from flask import Flask, jsonify
from db import get_producer, get_producer_detail

app = Flask(__name__)

bed = ['Kayu MDF', 'Sekrup self-tapping 5-6 mm', 'Baut dengan pucks 3x8x15',
       'Lem Kayu', 'Papan 40x100x2000', 'Papan 20x100x1600', 'Kuku 60x70 mm', 'pVA lem dan momen', 'Wood Varnish']
chair = ['Kayu', 'Papan', 'Sekrup', 'Lem Kayu',
         'Wood Varnish', 'Cat Kayu', 'Amplas']
sofa = ['Multiplek', 'Triplek', 'Kaso', 'Paku', 'Lem Kayu', 'Kain Fabric',
        'Kain Sofa Motif', 'Benang Jahit Nilon', 'Busa', 'Dakron', 'Silicon Hollow', 'Karet/Webing', 'Isi Staples 13/8', 'Lem Kuning']
swivelchair = ['belum dapet']
table = ['Kayu', 'Papan', 'Sekrup', 'Lem Kayu',
         'Wood Varnish', 'Cat Kayu', 'Amplas']


@app.route('/producer', methods=['GET'])
def producer():
    return get_producer()


@app.route('/producer/<producer_id>', methods=['GET'])
def producer_detail(producer_id):
    return get_producer_detail(producer_id)


@app.route('/materials/<name>', methods=['GET'])
def materials(name):
    if name == 'bed':
        return jsonify({'data_material': bed,
                        'original_name': 'bed'})
    elif name == 'chair':
        return jsonify({'data_material': chair,
                        'original_name': 'chair'})
    elif name == 'sofa':
        return jsonify({'data_material': sofa,
                        'original_name': 'sofa'})
    elif name == 'swivelchair':
        return jsonify({'data_material': swivelchair,
                        'original_name': 'swivelchair'})
    elif name == 'table':
        return jsonify({'data_material': table,
                        'original_name': 'table'})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
