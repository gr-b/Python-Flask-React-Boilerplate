import React, { useState } from 'react';

export default function Home() {
  const [response, setResponse] = useState('');

  const handleButtonClick = async () => {
    try {
      const result = await fetch('/api/test');
      const data = await result.text();
      setResponse(data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
      <div className="font-inter antialiased bg-gray-900 text-gray-200 tracking-tight">
        <div className="flex flex-col min-h-screen overflow-hidden">
          <h1>Python-Flask-React-Boilerplate</h1>
          <button
              onClick={handleButtonClick}
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Contact Backend
          </button>
          <p className="response-text">{response}</p>
        </div>
      </div>
  );
}

