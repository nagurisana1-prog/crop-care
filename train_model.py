import os
import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader


# ==============================
# SETTINGS
# ==============================

TRAIN_DIR = "dataset/train"
VALIDATION_DIR = "dataset/validation"

IMAGE_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 1
LEARNING_RATE = 0.0001

MODEL_PATH = "model/crop_disease_model.pth"


# ==============================
# DEVICE
# ==============================

device = torch.device("cpu")

print("🖥️ Device:", device)


# ==============================
# IMAGE TRANSFORMS
# ==============================

train_transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])


validation_transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])


# ==============================
# LOAD DATASET
# ==============================

print("\n📂 Loading Dataset...")

train_dataset = datasets.ImageFolder(
    TRAIN_DIR,
    transform=train_transform
)

validation_dataset = datasets.ImageFolder(
    VALIDATION_DIR,
    transform=validation_transform
)


train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=0
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False,
    num_workers=0
)


# ==============================
# DATASET INFORMATION
# ==============================

class_names = train_dataset.classes

print("✅ Training images:", len(train_dataset))
print("✅ Validation images:", len(validation_dataset))
print("✅ Number of classes:", len(class_names))

print("\n🌱 Classes:")

for number, name in enumerate(class_names):
    print(number, "→", name)


# ==============================
# CREATE MODEL
# ==============================

print("\n🧠 Creating MobileNetV3-Small...")

model = models.mobilenet_v3_small(
    weights="DEFAULT"
)


# Replace final layer
model.classifier[3] = nn.Linear(
    model.classifier[3].in_features,
    len(class_names)
)


model = model.to(device)


# ==============================
# LOSS FUNCTION
# ==============================

criterion = nn.CrossEntropyLoss()


# ==============================
# OPTIMIZER
# ==============================

optimizer = optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)


# ==============================
# TRAINING
# ==============================

print("\n🚀 Training Started...\n")

best_accuracy = 0.0


for epoch in range(EPOCHS):

    model.train()

    running_loss = 0.0
    correct = 0
    total = 0


    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)


        optimizer.zero_grad()


        outputs = model(images)


        loss = criterion(
            outputs,
            labels
        )


        loss.backward()

        optimizer.step()


        running_loss += loss.item()


        _, predicted = torch.max(
            outputs,
            1
        )


        total += labels.size(0)

        correct += (
            predicted == labels
        ).sum().item()


    train_accuracy = (
        100 * correct / total
    )


    # ==============================
    # VALIDATION
    # ==============================

    model.eval()

    validation_correct = 0
    validation_total = 0


    with torch.no_grad():

        for images, labels in validation_loader:

            images = images.to(device)
            labels = labels.to(device)


            outputs = model(images)


            _, predicted = torch.max(
                outputs,
                1
            )


            validation_total += labels.size(0)

            validation_correct += (
                predicted == labels
            ).sum().item()


    validation_accuracy = (
        100 * validation_correct / validation_total
    )


    print(
        f"Epoch [{epoch + 1}/{EPOCHS}] "
        f"Loss: {running_loss / len(train_loader):.4f} "
        f"Train Accuracy: {train_accuracy:.2f}% "
        f"Validation Accuracy: {validation_accuracy:.2f}%"
    )


    # ==============================
    # SAVE BEST MODEL
    # ==============================

    if validation_accuracy > best_accuracy:

        best_accuracy = validation_accuracy


        os.makedirs(
            "model",
            exist_ok=True
        )


        torch.save(
            {
                "model_state": model.state_dict(),
                "classes": class_names
            },
            MODEL_PATH
        )


        print(
            f"💾 Model saved! "
            f"Validation Accuracy: {best_accuracy:.2f}%"
        )


# ==============================
# COMPLETE
# ==============================

print("\n🎉 TRAINING COMPLETE!")

print(
    f"🏆 Best Validation Accuracy: "
    f"{best_accuracy:.2f}%"
)

print(
    f"📁 Model location: {MODEL_PATH}"
)