# Week 05 Hints

> **Rule:** Attempt the exercise for at least 30 minutes before reading Hint 1. Wait an additional 15 minutes before reading Hint 2 or 3.

---

## Exercise 5.1: Typed React Card with TypeScript Interfaces

### Hint Level 1 (Nudge)
Use object destructuring in the function parameters: `const UserBadge: React.FC<UserBadgeProps> = ({ user, onStatusToggle }) => { ... }`.

### Hint Level 2 (Concept Name)
For conditional class names or badges, use a mapping object or helper function typed with `Record<UserRole, string>`.

### Hint Level 3 (Direction)
Render a `<button onClick={() => onStatusToggle(user.id, !user.isActive)} aria-pressed={user.isActive}>` so accessibility tools recognize it as a state toggle switch.

---

## Exercise 5.2: Debug This — Stale Closures & Infinite Render Loops

### Hint Level 1 (Nudge)
When `useEffect` has no dependency array at all, it runs after *every single render*. Since the effect calls `setMetrics`, it triggers a render, which triggers the effect, infinitely.

### Hint Level 2 (Concept Name)
Use functional state updates: `setSeconds(prev => prev + 1)` allows the interval callback to always operate on the freshest state value without closing over a stale variable.

### Hint Level 3 (Direction)
Always return a cleanup callback from `useEffect`:
```tsx
useEffect(() => {
  const timer = setInterval(() => {
    setSeconds(prev => prev + 1);
  }, 1000);
  return () => clearInterval(timer);
}, []); // Empty dependency array ensures timer is created once
```

---

## Exercise 5.3: Safe Asynchronous Fetching with Loading & Error States

### Hint Level 1 (Nudge)
Instantiate `const controller = new AbortController()` inside the effect and pass `{ signal: controller.signal }` to `fetch()`.

### Hint Level 2 (Concept Name)
In the catch block, check if `error.name === 'AbortError'`. If it is an abort error, ignore it because it was intentionally cancelled.

### Hint Level 3 (Direction)
Structure your effect with cleanup:
```tsx
useEffect(() => {
  const controller = new AbortController();
  setState({ status: 'loading' });

  fetch(url, { signal: controller.signal })
    .then(res => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json();
    })
    .then(data => setState({ status: 'success', data }))
    .catch(err => {
      if (err.name !== 'AbortError') {
        setState({ status: 'error', message: err.message });
      }
    });

  return () => controller.abort();
}, [url]);
```
