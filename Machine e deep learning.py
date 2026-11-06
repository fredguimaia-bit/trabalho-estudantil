import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 1. Definir a arquitetura da Rede Neural
modelo = tf.keras.Sequential([
    # Camada de entrada/escondida com 8 neurônios e ativação ReLU
    tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),

    # Segunda camada escondida com 8 neurônios
    tf.keras.layers.Dense(8, activation='relu'),

    # Camada de saída com 3 neurônios (uma para cada espécie de Iris)
    tf.keras.layers.Dense(3, activation='softmax')
])

# 2. Compilar o modelo
modelo.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 3. Exibir o resumo da estrutura do modelo
modelo.summary()

historico = modelo.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=8,
    validation_split=0.1,
    verbose=1
)

import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

# 1. Avaliação básica de Perda e Acurácia
perda_teste, acuracia_teste = modelo.evaluate(X_test, y_test, verbose=0)

print(f"Perda no Teste (Test Loss): {perda_teste:.4f}")
print(f"Acurácia no Teste (Test Accuracy): {acuracia_teste * 100:.2f}%\n")

# 2. Obter as probabilidades e converter para a classe prevista (0, 1 ou 2)
y_pred_probs = modelo.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

# 3. Exibir o Relatório Detalhado (Precisão, Recall e F1-Score)
print("=== RELATÓRIO DE CLASSIFICAÇÃO ===")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 4. Matriz de Confusão
print("=== MATRIZ DE CONFUSÃO ===")
print(confusion_matrix(y_test, y_pred))
