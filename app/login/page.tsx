'use client';

import { useState } from 'react';
import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from '@/libs/firebase';
import { useRouter } from 'next/navigation';
import { onlogin, useAuthStore } from '@/stores/auth.store';

const LoginForm = () => {
    const router = useRouter();
    const setLoading = useAuthStore((state: any) => state.setLoading);
    const loading = useAuthStore((state: any) => state.loading);
    const error = useAuthStore((state: any) => state.error);

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);

        try {
            onlogin(email, password);
        } catch (err: any) {
            setLoading(false);
        } finally {
            setLoading(false);
        }
    };


    return (
        <div className='bg-white flex flex-col items-center justify-center h-screen w-full'>
            <form onSubmit={handleLogin} className="flex flex-col gap-4 w-full max-w-md mx-auto p-4">
                <h2 className="text-2xl font-bold text-black">Login</h2>
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    className="border p-2 rounded text-black"
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    className="border p-2 rounded text-black"
                />
                <button type="submit" className="bg-blue-600 text-white rounded p-2">
                    Log In
                    {loading && <span className="ml-2 spinner-border animate-spin"></span>}
                </button>
                {error && <p className="text-red-500">{error}</p>}
            </form>
        </div>
    );
};

export default LoginForm;
