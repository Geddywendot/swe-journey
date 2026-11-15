# Week 05 Exercises

Complete all Silver exercises to pass the week. Gold exercises are optional stretch challenges.

---

## Exercise 5.1: Typed React Card with TypeScript Interfaces

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Build a reusable, strongly-typed React component `UserBadge.tsx` that displays user profiles with status indicators, badges, and an interactive toggle button.

**Starter skeleton:**
```tsx
import React from 'react';

export type UserRole = 'admin' | 'editor' | 'viewer';

export interface UserProfile {
  id: string;
  name: string;
  email: string;
  role: UserRole;
  isActive: boolean;
  avatarUrl?: string;
}

interface UserBadgeProps {
  user: UserProfile;
  onStatusToggle: (id: string, newStatus: boolean) => void;
}

export const UserBadge: React.FC<UserBadgeProps> = ({ user, onStatusToggle }) => {
  // TODO: Implement accessible profile card with role badges and toggle button
  return <div>{/* TODO */}</div>;
};
```

**Acceptance criteria:**
- [ ] Strict TypeScript: zero `any` types permitted.
- [ ] Accessible button with `aria-pressed` reflecting `isActive`.
- [ ] Displays role-specific styling or badges based on `UserRole`.
- [ ] Verified with a unit test using `@testing-library/react`.

**Rules:** AI off. Use Vite + React + TypeScript setup.  
**Hints:** See `hints.md` section 5.1

---

## Exercise 5.2: Debug This — Stale Closures & Infinite Render Loops

**Type:** silver ("debug this")  
**Time box:** 60–90 min  
**Task:** A developer created an auto-refreshing metrics timer component, but it either re-renders thousands of times per second, crashes with `Maximum update depth exceeded`, or captures a stale count variable.

Here is the buggy code:
```tsx
import React, { useState, useEffect } from 'react';

export const BuggyTimer: React.FC = () => {
  const [seconds, setSeconds] = useState(0);
  const [metrics, setMetrics] = useState<number[]>([]);

  // Bug 1: Infinite loop - updates metrics on every render, triggering re-render!
  useEffect(() => {
    fetch('/api/latest-metric')
      .then(res => res.json())
      .then(data => setMetrics([...metrics, data.value]));
  }); // Notice missing dependency array!

  // Bug 2: Stale closure and interval leak!
  useEffect(() => {
    const timer = setInterval(() => {
      setSeconds(seconds + 1); // Stale reference to seconds!
    }, 1000);
    // Missing cleanup!
  }, []);

  return <div>Seconds: {seconds} | Metrics count: {metrics.length}</div>;
};
```

**Acceptance criteria:**
- [ ] Resolve the infinite re-render loop by configuring appropriate dependency arrays.
- [ ] Fix the interval timer using functional state updates (`setSeconds(s => s + 1)`).
- [ ] Implement cleanup function (`clearInterval(timer)`) to prevent memory leaks on unmount.
- [ ] Write a test asserting that intervals are cleared when unmounted.

**Rules:** AI off. Test with React Testing Library.  
**Hints:** See `hints.md` section 5.2

---

## Exercise 5.3: Safe Asynchronous Fetching with Loading & Error States

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Build a data fetching component `RepositoryList.tsx` that fetches public GitHub repositories for a given organization name. The component must model three explicit states: `loading`, `error` (with retry button), and `success` with rendered cards.

**Acceptance criteria:**
- [ ] Use discriminated union type for UI state: `{ status: 'idle' } | { status: 'loading' } | { status: 'error'; message: string } | { status: 'success'; data: Repo[] }`.
- [ ] Clean up in-flight requests using `AbortController` if the organization prop changes or component unmounts.
- [ ] Render semantic error alert with a functional Retry button.
- [ ] Zero unhandled promise rejections.

**Rules:** AI off. Use native `fetch` with `AbortController`.  
**Hints:** See `hints.md` section 5.3

---

## Exercise 5.4: Custom Hook with Debounced Search and Request Cancellation

**Type:** gold (stretch)  
**Time box:** 120–180 min  
**Task:** Build a custom hook `useDebouncedFetch<T>(query: string, delayMs: number): { data: T | null; isLoading: boolean; error: Error | null }`. The hook must debounce the user's keystrokes, cancel any active HTTP request if the query changes before completion, cache successful responses in memory, and prevent race conditions.

**Acceptance criteria:**
- [ ] Debounce timer resets on every keystroke.
- [ ] In-flight requests aborted via `AbortController`.
- [ ] Client-side in-memory cache keyed by query string.
- [ ] 100% test coverage using `@testing-library/react-hooks` or `renderHook`.

**Rules:** No hints provided for gold stretch exercises.
