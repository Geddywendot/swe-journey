import React from 'react';
import { Repository } from '../types/api';

interface RepositoryCardProps {
  repo: Repository;
}

export const RepositoryCard: React.FC<RepositoryCardProps> = ({ repo }) => {
  // TODO: Implement accessible repository card with name, description, star count, and language badge
  return (
    <article className="repo-card" data-testid={`repo-card-${repo.id}`}>
      {/* TODO: Implement card details */}
      <h3>{repo.name}</h3>
      <p>{repo.description || 'No description provided'}</p>
      <span>⭐ {repo.stargazers_count}</span>
      {repo.language && <span>{repo.language}</span>}
    </article>
  );
};
