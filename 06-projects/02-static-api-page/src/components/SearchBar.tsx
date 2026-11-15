import React from 'react';

interface SearchBarProps {
  value: string;
  onChange: (value: string) => void;
  onSubmit: (e: React.FormEvent) => void;
}

export const SearchBar: React.FC<SearchBarProps> = ({ value, onChange, onSubmit }) => {
  // TODO: Implement accessible search form with <form>, <label>, <input>, and submit <button>
  return (
    <form onSubmit={onSubmit}>
      {/* TODO: Implement search inputs and labels */}
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Enter organization (e.g. facebook)..."
      />
      <button type="submit">Search</button>
    </form>
  );
};
