# Import necessary libraries
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, ReLU
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# Step 1: Load and preprocess CIFAR-10
# -------------------------------
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize to [0, 1]
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# One-hot encode labels
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# Class labels
class_names = ['airplane', 'car', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Show one image per class
plt.figure(figsize=(10, 5))
for i in range(10):
    idx = np.where(y_train == i)[0][0]
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[idx])
    plt.title(class_names[i])
    plt.axis("off")
plt.suptitle("Pictures classes")
plt.show()

# -------------------------------
# Step 2: Define CNN model
# -------------------------------
def create_model():
    model = Sequential()

    # Layer 1: Conv + ReLU + MaxPool
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3)))
    model.add(ReLU())
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 2: Conv + ReLU
    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(ReLU())

    # Layer 3: Conv + ReLU
    model.add(Conv2D(64, (5, 5), padding='same'))
    model.add(ReLU())

    # Layer 4: Conv + ReLU
    model.add(Conv2D(128, (5, 5), padding='same'))
    model.add(ReLU())

    # Layer 5: Conv + ReLU + MaxPool
    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(ReLU())
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Fully Connected Layers
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    return model

# Show model summary
model = create_model()
model.summary()

# -------------------------------
# Step 3: Train with SGD
# -------------------------------
model_sgd = create_model()
model_sgd.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

history_sgd = model_sgd.fit(
    x_train, y_train_cat,
    epochs=20,
    batch_size=64,
    validation_data=(x_test, y_test_cat),
    verbose=2
)

# -------------------------------
# Step 4: Train with Adam
# -------------------------------
model_adam = create_model()
model_adam.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history_adam = model_adam.fit(
    x_train, y_train_cat,
    epochs=20,
    batch_size=64,
    validation_data=(x_test, y_test_cat),
    verbose=2
)

# -------------------------------
# Step 5: Plot Training Results
# -------------------------------
def plot_history(history, title):
    plt.figure(figsize=(12, 4))

    # Accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Val Accuracy')
    plt.title(f'{title} - Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    # Loss
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Val Loss')
    plt.title(f'{title} - Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Plot both training histories
plot_history(history_sgd, "SGD")
plot_history(history_adam, "Adam")

# -------------------------------
# Step 6: Evaluate Models
# -------------------------------
loss_sgd, acc_sgd = model_sgd.evaluate(x_test, y_test_cat, verbose=0)
loss_adam, acc_adam = model_adam.evaluate(x_test, y_test_cat, verbose=0)

print(f"\nSGD Optimizer - Test Accuracy: {acc_sgd:.4f}, Loss: {loss_sgd:.4f}")
print(f"Adam Optimizer - Test Accuracy: {acc_adam:.4f}, Loss: {loss_adam:.4f}")

# -------------------------------
# Step 7: Accuracy Comparison Chart
# -------------------------------
plt.figure(figsize=(6, 4))
plt.bar(["SGD", "Adam"], [acc_sgd, acc_adam], color=["skyblue", "lightgreen"])
plt.ylabel("Test Accuracy")
plt.title("Final Accuracy Comparison")
plt.ylim(0, 1)
plt.grid(axis='y')
plt.show()
