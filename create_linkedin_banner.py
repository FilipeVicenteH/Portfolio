from PIL import Image, ImageDraw, ImageFont
import os

def generate_banner():
    width = 1584
    height = 396

    # Create image with dark navy gradient
    img = Image.new("RGBA", (width, height), "#0F172A")
    draw = ImageDraw.Draw(img)

    # Draw gradient background manually
    for y in range(height):
        # Blend from #0F172A (15, 23, 42) to #1E293B (30, 41, 59)
        r = int(15 + (30 - 15) * (y / height))
        g = int(23 + (41 - 23) * (y / height))
        b = int(42 + (59 - 42) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

    # Add subtle grid lines on the right side
    grid_color = (255, 255, 255, 12)
    for x in range(450, width, 40):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 40):
        draw.line([(450, y), (width, y)], fill=grid_color, width=1)

    # Decorative accent glowing line at top right
    accent_teal = (13, 148, 136, 255) # #0D9488
    light_teal = (20, 184, 166, 255)  # #14B8A6

    draw.rectangle([500, 70, 506, 320], fill=light_teal)

    # Fonts - Use Arial or default truetype font
    try:
        font_name = ImageFont.truetype("arialbd.ttf", 46)
        font_sub = ImageFont.truetype("arialbd.ttf", 22)
        font_stack = ImageFont.truetype("arial.ttf", 18)
        font_contact = ImageFont.truetype("arial.ttf", 17)
    except:
        font_name = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_stack = ImageFont.load_default()
        font_contact = ImageFont.load_default()

    # Text positioning (x starts at 540 to avoid avatar overlap on left)
    start_x = 540

    # Name
    draw.text((start_x, 80), "FILIPE VICENTE HIDALGO", fill=(255, 255, 255, 255), font=font_name)

    # Tagline
    draw.text((start_x, 145), "Front-End Developer  |  Suporte Técnico N1/N2  |  Customer Success", fill=light_teal, font=font_sub)

    # Tech Stack Badges / Text
    stack_text = "React  •  JavaScript  •  APIs & Webhooks  •  Power BI  •  UI/UX Design"
    draw.text((start_x, 195), stack_text, fill=(203, 213, 225, 255), font=font_stack)

    # Divider line
    draw.line([(start_x, 240), (1450, 240)], fill=(51, 65, 85, 255), width=1)

    # Contact & Portfolio
    contact_text = "🌐 filipevicenteh.vercel.app   •   ✉️ filipe_vicente@hotmail.com   •   📱 (11) 96615-2956"
    draw.text((start_x, 260), contact_text, fill=(148, 163, 184, 255), font=font_contact)

    out_path = r"C:\Users\User\Desktop\linkedin_banner_filipe.png"
    img.save(out_path)
    print(f"Banner generated at: {out_path}")

if __name__ == "__main__":
    generate_banner()
