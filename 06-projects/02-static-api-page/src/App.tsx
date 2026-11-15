import React, { useState } from 'react';
import { AsyncState, Repository } from './types/api';
import { SearchBar } from './components/SearchBar';
import { RepositoryCard } from './components/RepositoryCard';
import { fetchOrgRepositories } from './services/api';

export const App: React.FC = () => {
  const [org, setOrg] = useState('facebook');
  const [state, setState] = useState<AsyncState<Repository[]>>({ status: 'idle' });

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Initiate fetchOrgRepositories with loading state, cancellation, and error handling
    setState({ status: 'loading' });
    fetchOrgRepositories(org)
      .then((data) => setState({ status: 'success', data }))
      .catch((err) => setState({ status: 'error', message: err.message }));
  };

  return (
    <main className="app-container">
      <header>
        <h1>GitHub Organization Explorer</h1>
        <SearchBar value={org} onChange={setOrg} onSubmit={handleSearch} />
      </header>

      <section className="results-container">
        {state.status === 'loading' && <p role="status">Loading repositories...</p>}
        {state.status === 'error' && (
          <div role="alert" className="error-box">
            <p>Error: {state.message}</p>
            <button onClick={handleSearch}>Retry</button>
          </div>
        )}
        {state.status === 'success' && state.data.length === 0 && (
          <p>No repositories found for organization.</p>
        )}
        {state.status === 'success' && (
          <div className="repo-grid" role="region" aria-label="Repositories">
            {state.data.map((repo) => (
              <RepositoryCard key={repo.id} repo={repo} />
            ))}
          </div>
        )}
      </section>
    </main>
  );
};

export default App;
