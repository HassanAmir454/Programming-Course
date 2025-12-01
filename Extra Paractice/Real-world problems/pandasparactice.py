import pandas as pd
import matplotlib.pyplot as plt

data = {
    'temperature' : [23, 43, 53, 28, 4, 1, 7, 21, 32, 14],
    'movement' : [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    'activity' : [1, 2, 3, 4, 5,6, 5, 3, 2, 1]
}

df = pd.DataFrame(data)
print(df)

# Temperature plot
plt.figure(figsize=(10, 5))
# plt.plot(df['temperature'], label="Temperature")
# plt.ylabel("Temperature")
# plt.title("Temperature Over Time")
# plt.legend()
# plt.show()

# # Movement plot
# plt.figure(figsize=(10, 5))
# plt.plot(df['movement'], label="Movement")
# plt.ylabel("Movement")
# plt.title("Movement Over Time")
# plt.legend()
# plt.show()
########################################################################################
plt.subplot(3, 1, 1)
plt.plot(df['temperature'], label="Temperature" , color = "red")
plt.title("Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature")

plt.subplot(3, 1, 2)
plt.plot(df['movement'], label="Movement", color="Green")
plt.title("Movement")
plt.xlabel("Time")
plt.ylabel("Movement")

plt.subplot(3, 1, 3)
plt.bar(range(len(df['activity'])), df['activity'], label="Activity", color="orange")
plt.title("Activity")
plt.xlabel("Time")
plt.ylabel("Activity")

plt.tight_layout()
plt.show()
#############################################################################################################