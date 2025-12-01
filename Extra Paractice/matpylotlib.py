import pandas as pd
import matplotlib.pyplot as plt

data = {
    'temperature' : [23, 43, 53, 28, 4, 1, 7, 21, 32, 14],
    'movement' : [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 8))

# TOP bar graph (Temperature)
plt.subplot(2, 1, 1)
plt.bar(range(len(df['temperature'])), df['temperature'])
plt.title("Temperature")

# BOTTOM bar graph (Movement)
plt.subplot(2, 1, 2)
plt.bar(range(len(df['movement'])), df['movement'])
plt.title("Movement")

plt.tight_layout()
plt.show()
