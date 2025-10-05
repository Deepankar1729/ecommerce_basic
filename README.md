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
  `/home/`

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
🛒 **Home page** → Users see available products  
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

## 🔹 🛠️ Setup & Run Instructions

### 1️ Clone the Repository

Start by cloning the project repo:

    ```bash
    git clone https://github.com/Deepankar1729/ecommerce_basic.git
    cd ecommerce_basic

### 2 Create a Virtual Environment

Creating a virtual environment helps keep dependencies separate from your system Python.

    ```bash
    # Create virtual environment
      python -m venv venv

Activate the virtual env

    # Linux/Mac:
      source venv/bin/activate

    # Windows:
      venv\Scripts\activate

Install Project Dependencies

    ```bash
       pip install -r requirements.txt
    
### 3 Configure Environment Variables (.env)

This step sets up the environment variables needed for Stripe and Django settings.

---

### 1️⃣ Create a Stripe Account

- If you don’t already have one, sign up at [https://stripe.com](https://stripe.com).  
- Use your Stripe account to obtain test API key.

---

### 2️⃣ Get Stripe API Keys

- Navigate to **Developers → API Keys** in the Stripe Dashboard.  
- Copy your **Test Secret Key**.

---

### 3️⃣ Create a `.env` File

In the root of your project, create a file named `.env` and add your key:

    ```env
       STRIPE_SECRET_KEY=sk_test_YOUR_OWN_SECRET_KEY

### 4 Database Setup

Apply Migrations

Run the following command to create the necessary database tables:

    ```bash
       python manage.py migrate

Create a Superuser
    
    ```bash
       python manage.py createsuperuser

Verify Database Setup

     ```bash
        python manage.py runserver

The server will start and listen on the default address: http://127.0.0.1:8000/

### 5 Test Stripe Payments

This step guides you to test the Stripe checkout flow safely using Stripe's test cards.

---

### 1️⃣ Add a Product (Optional)

- If your database is empty, log in as a superuser at [http://127.0.0.1:8000/admin/] 
- Add at least one active product with:
  - Name
  - Price (in cents)
  - Description
  - Image
  - Mark it as active

---

### 2️⃣ Access the Products Page

- Log in as a normal user (not admin) at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
- You should see available products with **Buy buttons**.

---

### 3️⃣ Proceed to Checkout

- Click the **Buy** button for a product.  
- You will be redirected to the Stripe-hosted checkout page.

---

### 4️⃣ Enter Test Payment Information

Use Stripe **test card numbers** to simulate payments:

- **Card number:** `4242 4242 4242 4242`  
- **Expiry date:** Any future date (e.g., `12/34`)  
- **CVC:** Any 3-digit number (e.g., `123`)  
- **ZIP code:** Any valid number (e.g., `12345`)

> ✅ This simulates a successful payment in test mode.  


---

### 5️⃣ Complete Payment

- Click **Pay** on the Stripe page.  
- After successful payment:
  - You are redirected to the **Payment Success** page
  - The order is recorded in the database
  - Refreshing the page is safe (no duplicate orders)

- If you cancel:
  - You are sent back to the **home page**

---

##  AI assist:

- Used chatgpt for understanding how stripe works, how to creating a checkout view and for styling my pages with bootsrap.
- Total time spent: Almost 9 hours. Most time spent in understanding stripe because it is a new concept for me.
- The code quality can be improved using webhooks.

---

##  Note:
- I did not pasted my personal stripe key for privacy reasons. Please test this with your own stripe secret key. Thank you.



