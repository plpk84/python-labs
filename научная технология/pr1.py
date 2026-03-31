import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

np.random.seed(42)

n_samples = 100
x1 = np.random.uniform(-20, 20, n_samples)
x2 = np.random.uniform(-20, 20, n_samples)

X_train = np.column_stack((x1, x2))

y_train = x1 - x2

model = keras.Sequential()

model.add(Dense(units=1, input_shape=(2,), activation='linear'))

model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

history = model.fit(X_train, y_train, epochs=500, verbose=False)

plt.plot(history.history['loss'])
plt.grid(True)
plt.title('График ошибки обучения (MSE)')
plt.xlabel('Эпоха')
plt.ylabel('Среднеквадратичная ошибка')
plt.show()

test_x1 = np.array([15, 8, -5, 3.5])
test_x2 = np.array([7, 2, 3, 1.2])
test_input = np.column_stack((test_x1, test_x2))

predictions = model.predict(test_input)

print("\nРезультаты тестирования:")
print(" x1      x2    | Ожидаемая разность | Предсказанная разность")
print("-" * 60)
for i in range(len(test_x1)):
    expected = test_x1[i] - test_x2[i]
    predicted = predictions[i][0]
    print(f"{test_x1[i]:5.1f}  {test_x2[i]:5.1f}   | {expected:17.4f}   | {predicted:18.6f}")

weights = model.get_weights()
print("\nВесовые коэффициенты и смещение (bias):")
print(f"w1 = {weights[0][0][0]:.6f}")
print(f"w2 = {weights[0][1][0]:.6f}")
print(f"b  = {weights[1][0]:.6f}")