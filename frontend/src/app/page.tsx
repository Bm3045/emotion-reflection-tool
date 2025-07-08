/* eslint-disable @typescript-eslint/no-unused-vars */
'use client';

import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<{ emotion: string; confidence: number } | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const res = await axios.post('http://localhost:8000/analyze', { text });
      setResult(res.data);
    } catch (err) {
      setError('Something went wrong. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-purple-200 flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-lg p-6 space-y-6">
        <h1 className="text-2xl font-bold text-center text-gray-800">Emotion Reflection Tool</h1>

        <label className="block">
          <span className="text-gray-700">How are you feeling?</span>
          <textarea
            className="mt-2 w-full border border-gray-300 rounded-lg p-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
            rows={4}
            value={text}
            placeholder="I feel nervous about my first job interview..."
            onChange={(e) => setText(e.target.value)}
          />
        </label>

        <button
          onClick={handleSubmit}
          disabled={loading || text.trim() === ''}
          className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50 transition"
        >
          {loading ? 'Analyzing...' : 'Submit'}
        </button>

        {result && (
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
            <h2 className="text-lg font-semibold text-blue-800">Result</h2>
            <p className="text-blue-700 mt-1">
              Emotion: <strong>{result.emotion}</strong>
            </p>
            <p className="text-blue-700">
              Confidence: <strong>{(result.confidence * 100).toFixed(2)}%</strong>
            </p>
          </div>
        )}

        {error && <p className="text-red-600 text-sm text-center">{error}</p>}
      </div>
    </div>
  );
}
