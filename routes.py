from flask import request, jsonify, render_template, send_from_directory
import os
from modules.quantize_image import quantize_image

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'image' not in request.files or 'bpp' not in request.form or 'brightness' not in request.form or 'contrast' not in request.form:
            return jsonify(success=False)
        file = request.files['image']
        bpp = int(request.form['bpp'])
        brightness = int(request.form['brightness'])
        contrast = float(request.form['contrast'])
        if file.filename == '':
            return jsonify(success=False)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            adjusted_image_path = quantize_image(filepath, bpp, brightness, contrast)
            return jsonify(success=True, url=f'/uploads/{os.path.basename(adjusted_image_path)}')
        return jsonify(success=False)

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)