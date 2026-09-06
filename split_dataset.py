import os
import random
import shutil

# Original PlantVillage dataset
SOURCE = r"C:\Users\sanan\Downloads\archive (2)\PlantVillage"

# New dataset folders inside our project
DEST = "dataset"

TRAIN = os.path.join(DEST, "train")
VALIDATION = os.path.join(DEST, "validation")

# 80% training, 20% validation
TRAIN_RATIO = 0.8

random.seed(42)


print("🌱 Starting dataset split...")
print("📂 Source:", SOURCE)


if not os.path.exists(SOURCE):
    print("❌ PlantVillage folder was not found!")
    print("Please check that it is inside your Downloads folder.")
    exit()


# Create destination folders
os.makedirs(TRAIN, exist_ok=True)
os.makedirs(VALIDATION, exist_ok=True)


# Get disease/class folders
classes = [
    folder for folder in os.listdir(SOURCE)
    if os.path.isdir(os.path.join(SOURCE, folder))
]


print(f"✅ Found {len(classes)} classes.")


for class_name in classes:

    source_class = os.path.join(
        SOURCE,
        class_name
    )

    train_class = os.path.join(
        TRAIN,
        class_name
    )

    validation_class = os.path.join(
        VALIDATION,
        class_name
    )

    os.makedirs(train_class, exist_ok=True)
    os.makedirs(validation_class, exist_ok=True)


    # Get image files
    images = [
        file for file in os.listdir(source_class)
        if file.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp")
        )
    ]


    random.shuffle(images)


    split_point = int(
        len(images) * TRAIN_RATIO
    )


    train_images = images[:split_point]
    validation_images = images[split_point:]


    print(
        f"📁 {class_name}: "
        f"{len(train_images)} train | "
        f"{len(validation_images)} validation"
    )


    # Copy training images
    for image in train_images:

        shutil.copy2(
            os.path.join(source_class, image),
            os.path.join(train_class, image)
        )


    # Copy validation images
    for image in validation_images:

        shutil.copy2(
            os.path.join(source_class, image),
            os.path.join(validation_class, image)
        )


print("\n🎉 Dataset split completed!")
print("📂 Training data:", TRAIN)
print("📂 Validation data:", VALIDATION)