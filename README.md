

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

![Lambda Trigger Screenshot](lambda-trigger-screenshot.jpg)


## ⚙️ Architecture Workflow
[S3 Source Bucket] → [Lambda Function] → [DynamoDB Table] → [S3 Destination Bucket] → [SNS Notification]


---

## 🧑‍💻 Lambda Function (Python)
See [`lambda_function.py`](lambda_function.py) for full source code.  
The function handles both **S3 triggers** and **direct Lambda invocations** for testing.

---

## 🧾 Deployment Steps
1. Create two S3 buckets: **source** and **destination**.  
2. Create a **DynamoDB table** (e.g., `newtable`).  
3. Create an **SNS topic** for success notifications.  
4. Create a **Lambda function** using `lambda_function.py`.  
5. Attach an **IAM role** with these permissions:
   - AmazonS3FullAccess  
   - AmazonDynamoDBFullAccess  
   - AmazonSNSFullAccess  
   - CloudWatchLogsFullAccess  
6. Add an **S3 trigger** for `ObjectCreated` events to invoke Lambda automatically.  
7. Upload a file to the source bucket to test the workflow.

---

## 📈 Outcome
✅ Serverless and fully automated data pipeline  
✅ Real-time event handling and notifications  
✅ Secure access using IAM policies  

---

## 📂 Repository Structure


aws-dynamodb-s3-lambda-automation/
│
├── lambda_function.py
├── s3-event-sample.json
└── README.md
