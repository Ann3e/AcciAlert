# 🚨 AcciAlert - AI-Powered Accident Detection & Alert System

## 📌 Problem Statement
Many people hesitate to report road accidents due to fear, confusion, or lack of awareness, leading to delays in emergency response. This hesitation can result in preventable fatalities as victims do not receive timely medical attention. 

Current systems rely heavily on human intervention, which can be inconsistent and inefficient in critical situations.

## 💡 Solution - AcciAlert
**AcciAlert** automates accident detection and alerting using machine learning, ensuring **real-time identification of accidents** and **immediate notifications** to nearby hospitals and law enforcement. By eliminating the need for human intervention, it enables **faster emergency response**, reducing fatalities and improving road safety.

---

## ✨ Features
✅ **Real-Time Accident Detection** using ML models  
✅ **Automated Emergency Alerts** sent to hospitals & authorities  
✅ **Location Tracking** using latitude & longitude  
✅ **Seamless Integration** with existing CCTV & traffic systems  
✅ **Cost-Effective Deployment** with minimal additional infrastructure  

---

## 🛠️ Tech Stack
- **Machine Learning** (YOLOv8 for object detection)
- **Python** (OpenCV, NumPy, Pandas, PyTorch)
- **Google Colab** (for model training & testing)
- **Twilio API** (for sending **SMS alerts** to emergency responders)
- **JSON** (for storing latitude, longitude, and video metadata)  

---

## 🚧 Challenges Faced
🚫 **Live Video Detection Issues:** We couldn't implement live video detection through **Google Colab** due to its limitations in handling real-time video streams.  
⏳ **Long Training Time:** Training our dataset on **VS Code** took more than **2 days**, making it impractical for efficient model development.  
📉 **Overfitting on Accident Data:** Initially, our model **overfitted on accident scenes**, causing false positives and requiring additional data preprocessing and augmentation.  
⚡ **Computational Constraints:** Limited access to **high-end GPUs** slowed down training and testing, making it difficult to experiment with more complex models.  

---

## 🚀 Future Scope
🔹 **Real-Time Detection** integrated with smart city surveillance  
🔹 **IoT-Based Alerts** for enhanced emergency response  
🔹 **Predictive Analytics** to reduce accident-prone areas  
🔹 **Crowdsourced Reporting** to improve accuracy  

---

## ⚡ How to Run the Project
 Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AcciAlert.git
