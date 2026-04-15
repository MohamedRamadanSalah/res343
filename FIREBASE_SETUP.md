# 🔥 Firebase Setup Guide for Menu Manager

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **"Add Project"** or **"Create Project"**
3. **Project Name**: `menu-manager` (or your choice)
4. Accept terms and click **"Continue"**
5. Disable **Google Analytics** (optional) → Click **"Create Project"**
6. Wait for project to be created (1-2 minutes)

---

## Step 2: Set Up Authentication (Email/Password)

1. In Firebase Console, go to **Authentication** (left menu)
2. Click **"Get started"** → **"Sign-in method"**
3. Click **"Email/Password"**
4. Enable it → Click **"Save"**
5. Go to **"Users"** tab → Click **"Add user"**
   - Email: `admin@menu.com`
   - Password: Create a strong password (e.g., `Admin123!@#`)
   - Click **"Add user"**

---

## Step 3: Create Firestore Database

1. In Firebase Console, go to **Firestore Database** (left menu)
2. Click **"Create Database"**
3. Select **Production mode** (we'll use security rules)
4. Location: Choose closest to you
5. Click **"Create"**

---

## Step 4: Set Up Security Rules

In Firestore → **Rules** tab, replace with:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Allow authenticated users to read/write menus
    match /menus/{document=**} {
      allow read: if request.auth != null;
      allow create, update, delete: if request.auth != null && request.auth.uid == get(/databases/$(database)/documents/admins/$(request.auth.uid)).data.uid;
    }

    // Admin list
    match /admins/{document=**} {
      allow read: if request.auth != null;
    }
  }
}
```

Click **"Publish"**

---

## Step 5: Get Firebase Config

1. In Firebase Console, click the **⚙️ Settings icon** → **Project Settings**
2. Scroll down to **"Your apps"** section
3. Click **"Web"** (if not created) → Register app
4. Copy the **Firebase Config** object:

```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID",
};
```

---

## Step 6: Update admin.html

1. Open `admin.html` in code editor
2. Find this section (around line 350):

```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
};
```

3. Replace with your actual config from Step 5
4. **Save the file**

---

## Step 7: Create Admin Document (Optional - for Advanced Security)

1. In Firestore, click **"Create collection"**
2. Name: `admins`
3. Add first document with ID: Your User UID (found in Authentication → Users)
4. Add field: `uid` (type: string) = your user ID

---

## Step 8: Update Client Page (index.html)

In your `index.html`, at the end of the Script section (before `</body>`), add:

```html
<!-- Firebase for reading menus -->
<script src="https://www.gstatic.com/firebasejs/10.5.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.5.0/firebase-firestore.js"></script>

<script>
  // Same Firebase config as admin.html
  const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID",
  };

  firebase.initializeApp(firebaseConfig);
  const db = firebase.firestore();

  // Load menus from Firebase
  async function loadMenusFromFirebase() {
    try {
      const snapshot = await db.collection("menus").orderBy("category").get();

      // Build menu objects from Firebase data
      const sohoItems = {},
        istikItems = {};

      snapshot.forEach((doc) => {
        const item = doc.data();
        const category = item.category;

        const menuItem = {
          name: item.name,
          desc: item.desc || "",
          price: item.price,
          ar: { name: item.nameAr, desc: item.descAr || "" },
        };

        if (item.menu === "soho") {
          if (!sohoItems[category]) sohoItems[category] = [];
          sohoItems[category].push(menuItem);
        } else if (item.menu === "istik") {
          if (!istikItems[category]) istikItems[category] = [];
          istikItems[category].push(menuItem);
        }
      });

      // Update global menu objects
      window.sohoMenu = sohoItems;
      window.istikMenu = istikItems;

      // Re-render menus
      renderSohoMenu();
      renderIstikMenu();
    } catch (error) {
      console.error("Error loading menus:", error);
    }
  }

  // Call on page load
  document.addEventListener("DOMContentLoaded", loadMenusFromFirebase);
</script>
```

---

## Step 9: Deploy to Vercel

### Option A: Using Vercel CLI

```bash
npm install -g vercel
cd c:\Users\dell\Documents\menu4
vercel
```

### Option B: Connect GitHub

1. Push your files to GitHub
2. Go to [Vercel](https://vercel.com)
3. Click **"New Project"** → Select GitHub repo
4. Deploy!

---

## 🎯 Access Your Admin Dashboard

- **Admin Panel**: `https://your-domain.vercel.app/admin.html`
- **Client Menu**: `https://your-domain.vercel.app/index.html`

Login with:

- **Email**: `admin@menu.com`
- **Password**: (the password you created in Step 2)

---

## 📝 Database Structure

```
Firebase Project
├── menus/ (collection)
│   ├── Document 1
│   │   ├── menu: "soho"
│   │   ├── category: "Sandwiches"
│   │   ├── name: "Classic Burger"
│   │   ├── nameAr: "برجر كلاسيكي"
│   │   ├── desc: "Grilled burger..."
│   │   ├── descAr: "برجر مشوي..."
│   │   ├── price: 279
│   │   └── createdAt: (timestamp)
│   └── Document 2...
└── admins/ (collection - optional)
    └── [userID]
        └── uid: (user ID)
```

---

## 🔧 Troubleshooting

### Login not working?

- ✅ Check email/password in Firebase Authentication
- ✅ Make sure user is enabled (not disabled)

### Items not appearing?

- ✅ Check Firestore rules are published
- ✅ Verify data exists in Firestore console
- ✅ Check browser console for errors (F12)

### Client not loading menus?

- ✅ Update Firebase config in `index.html`
- ✅ Ensure Firestore security rules allow reads

### Problems with Arabic text?

- ✅ Make sure HTML has `<meta charset="UTF-8">`

---

## 📞 Support

If you face issues:

1. Check [Firebase Documentation](https://firebase.google.com/docs)
2. Join [Firebase Discord Community](https://discord.gg/firebase)
3. Check browser console errors (F12 → Console tab)

---

## ✅ You're Done!

Your admin dashboard is ready! 🚀

**Next steps:**

1. Add menu items through the admin dashboard
2. They instantly appear on the client page
3. Share the admin URL with team members
4. Keep admin URL private (share only with admins)
