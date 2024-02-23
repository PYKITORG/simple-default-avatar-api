from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)


def create_avatar(initials, bgcolor="#567", textcolor="white"):
    img_size = (128, 128)
    img = Image.new('RGB', img_size, color=bgcolor)
    draw = ImageDraw.Draw(img)

    # Load a font
    font = ImageFont.load_default(size=64)

    # Calculate text width and height
    bounding_box = font.getbbox(initials)

    print(bounding_box)
    text_width = bounding_box[2] + bounding_box[0]
    text_height = bounding_box[3] + bounding_box[1]

    # Calculate position for centered text
    position = ((img_size[0] - text_width) / 2, (img_size[1] - text_height) / 2)

    draw.text(position, initials, fill=textcolor, font=font)
    return img


@app.route('/avatar/<initials>')
def avatar(initials):
    # Validate initials
    valid_initials = ''.join(filter(str.isalpha, initials)).upper()[:2]
    if not valid_initials:
        return "Invalid initials.", 400

    img = create_avatar(valid_initials)
    img_path = f"temp_{valid_initials}.png"
    img.save(img_path)

    return send_file(img_path, mimetype='image/png', as_attachment=False, download_name=f"{valid_initials}.png")


if __name__ == '__main__':
    app.run(debug=True)
