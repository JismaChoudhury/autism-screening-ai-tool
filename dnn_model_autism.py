# dnn_model_autism.py 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# Load dataset
df = pd.read_csv("data/autism_screening_adults.csv")  # Replace with your filename

# Preprocessing
df.dropna(inplace=True)  # Simple cleanup
label_cols = ['gender', 'ethnicity', 'jundice', 'austim', 'used_app_before', 'relation', 'Class/ASD']
le = LabelEncoder()

for col in label_cols:
    df[col] = le.fit_transform(df[col])

# Features and label
X = df.drop('Class/ASD', axis=1)
y = df['Class/ASD']

# Split & scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build DNN model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)))
model.add(Dropout(0.3))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train
early_stop = EarlyStopping(patience=5, restore_best_weights=True)
history = model.fit(X_train_scaled, y_train, validation_split=0.2, epochs=100, callbacks=[early_stop])

# Evaluate
loss, acc = model.evaluate(X_test_scaled, y_test)
print(f"\nTest Accuracy: {acc:.4f}")
