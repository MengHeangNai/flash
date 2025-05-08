'use client';
import { useEffect } from 'react';
import { onAuthStateChanged } from 'firebase/auth';
import { auth } from '@/libs/firebase';
import { fetchUserData, useAuthStore } from '@/stores/auth.store';
import { useRouter } from 'next/navigation';

type AuthProviderProps = {
    children: React.ReactNode;
};

export const AuthProvider = ({ children }: AuthProviderProps) => {
    const setUser = useAuthStore((state: any) => state.setUser);
    const router = useRouter();

    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, async (user) => {
            if (user) {
                try {
                    router.push('/');
                    const userData = await fetchUserData(user.uid);
                    setUser(userData);
                } catch (error) {
                    console.error('User fetch error:', error);
                    router.push('/login');
                }
            } else {
                router.push('/login');
            }
        });

        return () => unsubscribe();
    }, [setUser, router]);

    return children;
};
