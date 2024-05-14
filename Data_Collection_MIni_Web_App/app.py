from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    # Get the drawing data from the request
    drawing_data = request.form['drawing']
    
    # Create a new image with a white background
    img = Image.new('L', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw the image based on the drawing data
    for line in drawing_data.split(';'):
        if line:
            x_values, y_values = map(int, line.split(','))
            draw.line([x_values, y_values, x_values+1, y_values+1], fill='black', width=2)
    
    # Resize the image to (28, 28)
    img = img.resize((28, 28))

    # Save the image locally
    filename = 'drawing.png'
    img.save(filename)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
