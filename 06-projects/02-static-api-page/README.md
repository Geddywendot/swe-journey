# Project 02: Static API Explorer (React + TypeScript + Vite)

A modern, responsive, typed single-page application built with React 18+, TypeScript, Vite, and React Testing Library.

---

## 1. Project Overview

Modern frontend engineering requires fetching data from remote REST endpoints, managing complex client-side state lifecycles (loading, success, error, empty), and rendering responsive, accessible UI components.

In this project, you will build an interactive **GitHub Organization Repository Explorer** that consumes the public GitHub REST API, allows filtering by language or search term, sorts repositories by star count, and handles network edge cases cleanly.

---

## 2. Requirements & Acceptance Criteria

1. **Strict TypeScript:**
   - Zero `any` types.
   - Comprehensive data interfaces for GitHub repositories, owner profiles, and UI state.
2. **State Management:**
   - Explicit state modeling: `loading`, `error` (with retry button), and `success`.
   - Cancellation of in-flight requests using `AbortController` on new searches.
3. **User Experience & Accessibility:**
   - Responsive CSS Grid card layout that adapts from mobile viewports to desktop.
   - Accessible search input with proper `<label>` and keyboard navigation.
   - Empty state message when a search query returns 0 repositories.
4. **Testing:**
   - Automated tests in `src/__tests__/App.test.tsx` using Vitest and `@testing-library/react`.

---

## 3. Project Setup

Install dependencies and run the development server:

```bash
# In 06-projects/02-static-api-page/
npm install
npm run dev
```

Run test suite:
```bash
npm test
```

When you first open this project, the test suite will **fail** because starter components return incomplete JSX with `TODO` markers. Implement the components until all tests pass.
