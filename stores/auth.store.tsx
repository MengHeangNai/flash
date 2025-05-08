// store/authStore.js
import { auth, db } from '@/libs/firebase';
import { error } from 'console';
import { signInWithEmailAndPassword, createUserWithEmailAndPassword, sendPasswordResetEmail, updatePassword } from 'firebase/auth';
import { query, getDocs, collection, where, limit, doc, updateDoc } from 'firebase/firestore';
import { create } from 'zustand';


interface AuthState {
    user: any;
    loading: boolean;
    error: any;
    setUser: (user: any) => void;
    setLoading: (loading: boolean) => void;
    setError: (error: any) => void;
}

export const useAuthStore = create<AuthState>((set) => ({
    user: null,
    loading: true,
    error: null,
    setUser: (user: any) => set({ user }),
    setLoading: (loading: boolean) => set({ loading }),
    setError: (error: any) => set({ error }),
}));


export const fetchUserData = async (uid: string) => {

    const queryData = query(
        collection(db, 'users'),
        where('key', '==', uid),
        limit(1)
    );

    try {
        const snapshot = await getDocs(queryData);
        const data = snapshot.docs.map(doc => ({
            ...doc.data(),
            id: doc.id
        }));
        return data[0] || null;
    } catch (error) {
        console.error('Error fetching user data:', error);
        throw error;
    }
};

export const onlogin = (email: string, password: string) => {
    const setError = useAuthStore.getState().setError;
    try {
        signInWithEmailAndPassword(auth, email, password)
            .then((userCredential) => {
                const user = userCredential.user;
                console.log('User logged in:', user);
            }
            ).catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;
                console.log('Error logging in:', errorCode, errorMessage);
                setError(errorMessage);
            });
    } catch (error) {
        console.log('Login error:', error);
    }
}

export const onsignup = async (email: string, password: string) => {
    try {
        await createUserWithEmailAndPassword(auth, email, password);
    } catch (error) {
        console.log('Signup error:', error);
    }
}

export const onlogout = () => {
    try {
        auth.signOut();
    } catch (error) {
        console.log('Logout error:', error);
    }
}

export const onresetpassword = (email: string) => {
    try {
        sendPasswordResetEmail(auth, email);
    } catch (error) {
        console.log('Reset password error:', error);
    }
}

export const onupdateprofile = async (uid: string, data: any) => {
    try {
        const userRef = doc(db, 'users', uid);
        await updateDoc(userRef, data);
    } catch (error) {
        console.log('Update profile error:', error);
    }
}

export const onupdatepassword = async (newPassword: string) => {
    try {
        const user = auth.currentUser;
        if (user) {
            await updatePassword(user, newPassword);
        }
    } catch (error) {
        console.log('Update password error:', error);
    }
}