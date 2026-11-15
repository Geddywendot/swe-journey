import { Repository } from '../types/api';

/**
 * Fetch repositories for a specified GitHub organization.
 * 
 * TODO: Implement API fetch using fetch() with signal support.
 * Endpoint: https://api.github.com/orgs/{org}/repos?per_page=30&sort=updated
 */
export async function fetchOrgRepositories(
  org: string,
  signal?: AbortSignal
): Promise<Repository[]> {
  // TODO: Fetch from GitHub API, handle non-200 responses, parse JSON
  throw new NotImplementedError('Learner task: Implement fetchOrgRepositories()');
}

class NotImplementedError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'NotImplementedError';
  }
}
