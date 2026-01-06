import os
import random
import shutil

# Paths
base_path = r"c:\Users\Manasvi\OneDrive\Desktop\AI Enhanced ehr - final1\AI_Enhanced_EHR_TeamB"
enhanced_path = os.path.join(base_path, "Milestone2", "enhanced")
enhance_compare_path = os.path.join(base_path, "Milestone2", "enhance_compare")
raw_path = os.path.join(base_path, "Milestone2", "raw")
dest_path = os.path.join(base_path, "Milestone4", "Images", "ehr_processedimages")

# Function to get image files
def get_images(folder):
    files = os.listdir(folder)
    images = [f for f in files if f.lower().endswith(('.jpeg', '.jpg', '.png', '.jpeg.png'))]
    return [os.path.join(folder, img) for img in images]

# Get images
enhanced_images = get_images(enhanced_path)
enhance_compare_images = get_images(enhance_compare_path)
raw_images = get_images(raw_path)

# Select randomly
selected_enhanced = random.sample(enhanced_images, min(30, len(enhanced_images)))
selected_enhance_compare = random.sample(enhance_compare_images, min(20, len(enhance_compare_images)))
selected_raw = random.sample(raw_images, min(20, len(raw_images)))

# Combine
selected = selected_enhanced + selected_enhance_compare + selected_raw

# Shuffle to randomize order
random.shuffle(selected)

# Copy and rename
for i, src in enumerate(selected, 1):
    ext = os.path.splitext(src)[1]
    dest_file = f"EHR_{i:02d}{ext}"
    dest_full = os.path.join(dest_path, dest_file)
    shutil.copy2(src, dest_full)
    print(f"Copied {src} to {dest_full}")

print("Done!")