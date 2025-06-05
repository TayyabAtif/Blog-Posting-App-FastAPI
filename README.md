# 📝 FastAPI Blog Backend

A full-featured, secure blog backend built with **FastAPI** and **MongoDB**, supporting user management, blogging, newsletter emails, and real-time updates via WebSockets.

## 🚀 Features

- ✅ User Signup & Login with JWT
- 👤 Admin & General User Roles
- 📰 Post Creation (Admins only), Update, Delete, Get All
- 🧠 Category-Based Filtering (Programming, Engineering)
- ❤️ Like/Unlike System
- 💬 Comment System with Nested Replies
- 👥 Follow/Unfollow Users + Followers Count
- 📬 Subscribe to Email Newsletters
- 📢 WebSocket for Real-Time Notifications
- 🔐 Secure Password Hashing
- 📈 Post Count Per User
- 📁 Clean Folder Structure with Modular Routing

## 🛠 Tech Stack

- **Backend**: FastAPI
- **Database**: MongoDB
- **Auth**: JWT
- **Email**: smtplib, threading
- **Testing**: Postman
- **Real-Time**: WebSocket

## 🔧 .env (Environment Variables)

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=youremail@gmail.com
EMAIL_PASSWORD=yourapppassword

📬 Want to try?
Open Postman

Register → Login → Get Token

Use token to test routes

Subscribe → Send newsletter → Email arrives

Open WebSocket and create a post → Notification appears in WebSocket

