from PIL import Image, ImageDraw
import torch

def process_photo(image_path):
    """Effectue la prédiction et ajoute des annotations à l'image."""
    model = torch.hub.load('/Users/yanisbestaoui/Downloads/MLOPS-Project/app/yolov5', 'custom', path='Data/weights.pt', source='local')
    image = Image.open(image_path).convert('RGB')
    results = model(image)

    draw = ImageDraw.Draw(image)
    for *xyxy, conf, cls in results.xyxy[0]:
        x1, y1, x2, y2 = map(int, xyxy)
        draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
        draw.text((x1, y1 - 10), f"{cls} {conf:.2f}", fill="red")

    # Sauvegarde de l'image annotée
    annotated_image_path = image_path.replace('.jpg', '_annotated.jpg')
    image.save(annotated_image_path)
    return annotated_image_path
