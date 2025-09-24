import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchRss = async () => {
      try {
        const response = await fetch('http://localhost:8000/rss');
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        const data = await response.json();
        setItems(Array.isArray(data.items) ? data.items : []);
      } catch (err) {
        setError(err.message || 'Failed to load');
      } finally {
        setLoading(false);
      }
    };

    fetchRss();
  }, []);

  if (loading) {
    return <div style={{ padding: 24 }}>Loading…</div>;
  }

  if (error) {
    return <div style={{ padding: 24, color: 'crimson' }}>Error: {error}</div>;
  }

  if (!items.length) {
    return <div style={{ padding: 24 }}>Нет новостей</div>;
  }

  const first = items[0];

  return (
    <div style={{ padding: 24 }}>
      <h1 style={{ marginTop: 0 }}>{first.title}</h1>
      {first.published && (
        <div style={{ color: '#666', marginBottom: 12 }}>{first.published}</div>
      )}
      <div dangerouslySetInnerHTML={{ __html: first.summary || '' }} />
      {first.link && (
        <div style={{ marginTop: 12 }}>
          <a href={first.link} target="_blank" rel="noreferrer">Открыть источник</a>
        </div>
      )}
    </div>
  );
}

export default App;
