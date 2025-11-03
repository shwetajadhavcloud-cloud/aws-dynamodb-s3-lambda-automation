

# 🚀 Automated DynamoDB Data Export using AWS Lambda and S3

## 📘 Project Overview
This project automates data export from **Amazon DynamoDB** to **Amazon S3** using **AWS Lambda (Python)** triggered by S3 bucket events. It also sends notifications via **SNS** upon successful data export.

Whenever a file is uploaded to the **Source S3 bucket**, Lambda:
1. Reads the new object metadata.
2. Stores it into **DynamoDB**.
3. Exports table items to a **Destination S3 bucket**.
4. Sends a success message through **Amazon SNS**.

---

## 🧰 AWS Services Used
- **Amazon S3** – Source & destination buckets for data storage.  
- **AWS Lambda (Python)** – Processes and automates data workflow.  
- **Amazon DynamoDB** – NoSQL database to store object details.  
- **Amazon SNS** – Sends notifications after successful export.  
- **IAM Roles** – Controls permissions and access policies.
 

---## 📸 Lambda Trigger Screenshot
Here’s a view of my AWS Lambda function trigger setup:

![Lambda Trigger Screenshot](lambda-trigger-screenshot.png)


## ⚙️ Architecture Workflow
