import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { vi, describe, it, expect, beforeEach } from 'vitest';
import App from '../App';
import * as api from '../services/api';

vi.mock('../services/api');

describe('GitHub Organization Explorer App', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders application header and search bar', () => {
    render(<App />);
    expect(screen.getByText('GitHub Organization Explorer')).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/enter organization/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /search/i })).toBeInTheDocument();
  });

  it('displays loading indicator and renders repository cards on successful search', async () => {
    const mockRepos = [
      {
        id: 101,
        name: 'react',
        full_name: 'facebook/react',
        description: 'The library for web and native user interfaces',
        html_url: 'https://github.com/facebook/react',
        stargazers_count: 220000,
        forks_count: 45000,
        language: 'JavaScript',
        updated_at: '2026-11-15T00:00:00Z',
      },
    ];

    vi.spyOn(api, 'fetchOrgRepositories').mockResolvedValue(mockRepos);

    render(<App />);
    const searchButton = screen.getByRole('button', { name: /search/i });
    fireEvent.click(searchButton);

    expect(screen.getByRole('status')).toHaveTextContent('Loading repositories...');

    await waitFor(() => {
      expect(screen.getByText('react')).toBeInTheDocument();
      expect(screen.getByText(/The library for web and native/)).toBeInTheDocument();
      expect(screen.getByText(/220000/)).toBeInTheDocument();
    });
  });

  it('displays error alert with retry button when API fails', async () => {
    vi.spyOn(api, 'fetchOrgRepositories').mockRejectedValue(new Error('Organization not found'));

    render(<App />);
    const searchButton = screen.getByRole('button', { name: /search/i });
    fireEvent.click(searchButton);

    await waitFor(() => {
      expect(screen.getByRole('alert')).toBeInTheDocument();
      expect(screen.getByText(/Error: Organization not found/i)).toBeInTheDocument();
      expect(screen.getByRole('button', { name: /retry/i })).toBeInTheDocument();
    });
  });
});
