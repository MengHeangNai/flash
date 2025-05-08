// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getDatabase } from "firebase/database";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
    apiKey: "AIzaSyBg5K7aiSljrmb6e0xtFcYhnnhSsP4EePA",
    authDomain: "my-project-b56c4.firebaseapp.com",
    databaseURL: "https://my-project-b56c4-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "my-project-b56c4",
    storageBucket: "my-project-b56c4.firebasestorage.app",
    messagingSenderId: "437524201843",
    appId: "1:437524201843:web:6d9d833a9db8cabe3a0506",
    measurementId: "G-T4FYCJ6FWP"
};

export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);