

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data for chatbot vs. human agent customer support interactions
labels = ['Chatbot AI', 'Human Agents']
sizes = [65, 35]  # Percentage of interactions handled
colors = ['green', 'yellow']

# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})
plt.title("Customer Support Interaction Distribution (Chatbot vs. Human)")
plt.show()

# Response time comparison (in seconds)
categories = ['Query Understanding', 'Resolution Time', 'Follow-up']
human_agents = [8, 15, 10]
chatbot_ai = [3, 7, 4]

# Bar Chart
plt.figure(figsize=(8, 5))
sns.barplot(x=categories, y=human_agents, color='red', label="Human Agents")
sns.barplot(x=categories, y=chatbot_ai, color='blue', label="Chatbot AI")

plt.xlabel("Customer Support Stages")
plt.ylabel("Average Response Time (sec)")
plt.title("Chatbot vs. Human Agent Response Time")
plt.legend()
plt.show()

# Adoption trend over years (percentage of chatbot use)
years = np.arange(2015, 2025)
chatbot_adoption = [5, 10, 15, 20, 30, 45, 55, 65, 75, 85]

# Line Chart
plt.figure(figsize=(8, 5))
plt.plot(years, chatbot_adoption, marker='o', linestyle='-', color='blue', label="Chatbot Adoption Rate")

plt.xlabel("Year")
plt.ylabel("Chatbot Adoption (%)")
plt.title("AI Chatbot Adoption in Customer Support (2015-2025)")
plt.grid(True)
plt.legend()
plt.show()