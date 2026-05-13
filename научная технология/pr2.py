import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)




EPOCHS = 5
BATCH_SIZE = 32

for i in range(32,97,16):
  print(f"Модель НС c {i} нейронами:")
  model = Sequential([
        Flatten(input_shape=(28, 28, 1)),
        Dense(i, activation='relu', use_bias=True, name='hidden'),
        Dense(10, activation='softmax', use_bias=True, name='output')
    ])
  model.compile(
      optimizer='adam',
      loss='categorical_crossentropy',
      metrics=['accuracy']
  )
  model.summary()
  model.fit(
      x_train, y_train_cat,
      batch_size=BATCH_SIZE,
      epochs=EPOCHS,
      validation_split=0.2,
      verbose=1
  )
  test_loss, test_acc = model.evaluate(x_test, y_test_cat, verbose=0)
  print(f"Модель НС c {i} нейронами    - Точность на тесте: {test_acc:.4f} ({test_acc*100:.2f}%)")
  print(f"Модель  НС c {i} нейронами    - Критерий качества на тесте: {test_loss:.4f} ({test_loss*100:.2f}%)")
  print()


# Вариант 6
print("Модель c BIAS:")
model_with_bias = Sequential([
        Flatten(input_shape=(28, 28, 1)),
        Dense(128, activation='relu', use_bias=True, name='hidden_without_bias'),
        Dense(10, activation='softmax', use_bias=True, name='output_without_bias')
    ])
model_with_bias.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
model_with_bias.summary()
model_with_bias.fit(
    x_train, y_train_cat,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    validation_split=0.2,
    verbose=1
)
test_loss_with_bias, test_acc_with_bias = model_with_bias.evaluate(x_test, y_test_cat, verbose=0)

print(f"Модель c BIAS  - Точность на тесте: {test_acc_with_bias:.4f} ({test_acc_with_bias*100:.2f}%)")
print(f"Модель c BIAS  - Критерий качества на тесте: {test_acc_with_bias:.4f} ({test_acc_with_bias*100:.2f}%)")


print("Модель без BIAS:")
model_without_bias = Sequential([
        Flatten(input_shape=(28, 28, 1)),
        Dense(128, activation='relu', use_bias=False, name='hidden_without_bias'),
        Dense(10, activation='softmax', use_bias=False, name='output_without_bias')
    ])
model_without_bias.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
model_without_bias.summary()
history_without_bias = model_without_bias.fit(
    x_train, y_train_cat,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    validation_split=0.2,
    verbose=1
)
test_loss_without_bias, test_acc_without_bias = model_without_bias.evaluate(x_test, y_test_cat, verbose=0)

print(f"Модель без BIAS  - Точность на тесте: {test_acc_without_bias:.4f} ({test_acc_without_bias*100:.2f}%)")
print(f"Модель без BIAS  - Критерий качества на тесте: {test_loss_without_bias:.4f} ({test_loss_without_bias*100:.2f}%)")

total_params_with_bias = model_with_bias.count_params()
total_params_without_bias = model_without_bias.count_params()
print("""
1. КОЛИЧЕСТВО ПАРАМЕТРОВ:
   - Модель с bias:    {} параметров
   - Модель без bias:  {} параметров
   - Разница: {} параметров (ровно на количество нейронов)

2. ТОЧНОСТЬ КЛАССИФИКАЦИИ:
   - С bias:    {:.2f}%
   - Без bias:  {:.2f}%
   """.format(total_params_with_bias, total_params_without_bias, 
              total_params_with_bias - total_params_without_bias,
              test_acc_with_bias*100, test_acc_without_bias*100))