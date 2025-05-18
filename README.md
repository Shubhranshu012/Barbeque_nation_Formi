# 🧠 Barbeque nation Communication System with Retell, Dashchat, Make.com, and Google Sheets

## Overview

This project integrates:
- **Retell AI**: For real-time voice-based communication and agent interaction
- **Dashchat**: To invoke and manage the created agent
- **Make.com (Integromat)**: As a middleware platform to automate data processing
- **Google Sheets**: For storing structured output like phone numbers, time, date and Other Info

---

## 🔁 Data Flow Architecture

1. **User speaks to Retell AI Agent By the Help of the Frontend Given by DashChat **
2. Agent processes intent and calls a webhook or external function
3. **Make.com** receives data via a webhook
4. **Make.com** parses and pushes the data (e.g., phone, time, date) to **Google Sheets**

---

## 🔧 Components & Setup

### 1. Retell AI
- Create a conversational agent with state machines and intents
- Use an `External Function` call inside Retell to trigger Make.com's webhook


### 2.Use Make.com
- Set up the project (Used For Automation)
- Set the structure and The flow of data
- Configure All the Path The input to be recived and the Output


### 3.Set Up ChatDash
- used to give the used access to a Frontend to interact with the agent
- create a preject 
- link the agen creted by the Retell Ai bu using its agent id and the Api Key 
- the ChatDash Will Give you The Enbeded Code with then can be uaed in Html or React or any thing For Publishing the Project in the Web



Note:- The Conversation Flow has Also been Added


