# 🛍️ End-to-End E-Commerce Flow (Django + Stripe)

This project implements a complete e-commerce flow with **user authentication**, **product browsing**, **secure Stripe checkout**, and **admin management**.

---

## 🔹 Full Project Flow

### 1️⃣ User Registration & Login
- When the site is opened, the **login page** is the entry point.
- **Existing users** log in with username & password.
- **New users** click **Register**, fill out details, and an account is created.
- Django’s built-in authentication handles:
  - Secure password hashing
  - Session-based login
  - Logout functionality

---

### 2️⃣ Home Page (after login)
- Shows **all active products** from the database.
- Each product displays:
  - Name  
  - Price (converted from cents → dollars)  
  - Image  
  - Optional description  
  - Quantity input + **Buy** button
- Also includes **My Orders** → showing the logged-in user’s previous purchases.

---

### 3️⃣ Checkout
- When user clicks **Buy**:
  - `checkout` view verifies product exists and is active.
  - Reads chosen quantity.
  - Creates a **Stripe Checkout Session** with:
    - Product name
    - Price (in cents)
    - Quantity
  - Redirects the user to **Stripe’s hosted checkout page**.

---

### 4️⃣ Payment (Stripe)
- **Stripe securely handles payment details**.
- If successful → user is redirected to:  
  `/success/?session_id=...`
- If cancelled → user is sent back to:  
  `/products/`

---

### 5️⃣ Success Page
- `success` view checks `session_id` with Stripe:
  - Confirms payment is **paid**
  - Retrieves product name, quantity, and amount
  - Saves the order for the logged-in user  
    (`get_or_create` prevents duplicates)
- Renders a **Payment Successful** page.
- Refreshing the page is **safe** (no duplicate charges or orders).

---

### 6️⃣ Orders (User Account)
- Users can view their own **order history** on the home page.
- Orders display:
  - Product name
  - Quantity
  - Total paid

---

### 7️⃣ Django Admin (for Staff/Store Manager)
- **Products**:
  - Add/edit/remove products with images, price, description
  - Toggle active/inactive products
- **Orders**:
  - View all orders by all users
  - See product name, buyer, quantity, and amount
  - Search & filter orders easily

---

## ✅ End Result
You now have:

🔐 **Authentication** → Users must register/login before shopping  
🛒 **Products page** → Users see available products  
💳 **Stripe Checkout** → Secure payment flow  
📦 **Order tracking** → Users see their own orders  
🛠️ **Admin management** → Staff can add products & track all orders  

---

## ⚙️ Tech Stack
- **Django** (Backend & Auth)
- **Bootstrap** (Frontend)
- **Stripe API** (Payments)
- **Django Admin** (Management)

---

