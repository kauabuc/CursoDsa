import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow import keras

(imagens_treino, labels_treino), (imagens_teste,
                                  labels_teste) = keras.datasets.cifar10.load_data()

nomes_classes = ['airplane', 'automobile', 'bird', 'cat',
                 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

imagens_treino = imagens_treino / 255.0
imagens_teste = imagens_teste / 255.0


def vizualiza_imagens(imagens, labels):
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(imagens[i], cmap=plt.cm.binary)
        plt.xlabel(nomes_classes[labels[i][0]])
    plt.show()


vizualiza_imagens(imagens_treino, labels_treino)

modelo = keras.models.Sequential()

modelo.add(keras.layers.Conv2D(
    32, (3, 3), activation="relu", input_shape=(32, 32, 3)))
modelo.add(keras.layers.MaxPooling2D((2, 2)))

modelo.add(keras.layers.Conv2D(64, (3, 3), activation="relu"))
modelo.add(keras.layers.MaxPooling2D((2, 2)))

modelo.add(keras.layers.Conv2D(64, (3, 3), activation="relu"))
modelo.add(keras.layers.MaxPooling2D((2, 2)))


modelo.add(keras.layers.Flatten())
modelo.add(keras.layers.Dense(64, activation="relu"))
modelo.add(keras.layers.Dense(10, activation="softmax"))

# print(modelo.summary())

modelo.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy", metrics=["accuracy"])

history = modelo.fit(imagens_treino,
                     labels_treino,
                     epochs=10,
                     validation_data=(imagens_teste, labels_teste))


erro_teste, acc_teste = modelo.evaluate(imagens_teste, labels_teste, verbose=2)

nova_imagem = Image.open("pytohn/Cursodsa/cap17/nova_imagem.jpg")

nova_imagem = nova_imagem.resize((32, 32))

nova_imagem_array = np.array(nova_imagem) / 255.0

nova_imagem_array = np.expand_dims(nova_imagem_array, axis=0)
previsoes = modelo.predict(nova_imagem_array)

print(previsoes)
classe_prevista = np.argmax(previsoes)
nome_classe_prevista = nomes_classes[classe_prevista]

print(nome_classe_prevista)
