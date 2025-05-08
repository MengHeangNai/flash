'use client'
import { onlogout } from '@/stores/auth.store'
import React from 'react'

const HomePage = () => {

  return (
    <div className='flex flex-col disabled:flex items-center justify-center h-screen w-full '>
      <h1 className='text-4xl font-bold text-center'>
        Welcome to the Next.js 15 App Router with Tailwind CSS and TypeScript!
      </h1>
      <button onClick={() => {
        onlogout()
      }} className='bg-blue-600 text-white rounded p-2 mt-4'>
        log out
      </button>
    </div>
  )
}

export default HomePage
