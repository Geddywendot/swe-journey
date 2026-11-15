# Quiz 05

Test your understanding of React rendering mechanics, hook rules, and TypeScript type safety. Record your answers before consulting your learning partner.

1. Why does passing an empty dependency array `[]` to `useEffect` cause it to execute only once after the initial render?
   a) React disables the hook after first run.  
   b) Because none of the dependencies ever change between renders, React never re-executes the effect callback during subsequent updates.  
   c) It compiles to a Web Worker thread.  
   d) Browsers cache empty arrays permanently.  
   *(Answer key: `instructor-keys/quiz-05.md`)*

2. Why should React state never be mutated directly (e.g., `todos.push(newTodo)`)?
   a) JavaScript prohibits array mutations.  
   b) React relies on shallow object reference comparison (`prev !== next`) to determine if a component needs to re-render; mutating an object in place preserves its memory reference, preventing necessary UI updates.  
   c) Direct mutations crash the browser V8 engine.  
   d) Direct mutation converts arrays to strings.  
   *(Answer key: `instructor-keys/quiz-05.md`)*

3. What is a "stale closure" in React hooks?
   a) A closed socket connection.  
   b) A hook callback or event listener that captures and references variables from an older render cycle rather than their current values.  
   c) A memory leak in Vite.  
   d) A CSS style that failed to load.  
   *(Answer key: `instructor-keys/quiz-05.md`)*

4. How does `AbortController` resolve race conditions in client-side data fetching?
   a) It speeds up backend database queries.  
   b) It cancels active in-flight HTTP requests when a user changes input parameters, preventing earlier slow responses from overwriting newer query results.  
   c) It compresses JSON payloads over WebSocket.  
   d) It overrides the browser's CORS policy.  
   *(Answer key: `instructor-keys/quiz-05.md`)*

5. What is the benefit of modeling UI state as a TypeScript discriminated union (`type State = { status: 'idle' } | { status: 'loading' } | { status: 'error'; err: string }`) instead of multiple booleans (`isLoading`, `isError`, `isSuccess`)?
   a) It eliminates "impossible states" (such as `isLoading === true` and `isError === true` simultaneously) and enables exhaustive type checking.  
   b) It reduces bundle size by 50%.  
   c) It automatically generates CSS styles.  
   d) It allows TypeScript to bypass runtime validation.  
   *(Answer key: `instructor-keys/quiz-05.md`)*

6. What is the fundamental difference between `interface` and `type` in TypeScript?
   a) `interface` can only describe numbers.  
   b) `interface` is open to declaration merging and primarily used for object shapes; `type` alias can represent unions, primitives, tuples, and intersections.  
   c) `type` is executed at runtime in the browser.  
   d) There is no difference; they are strictly synonymous.  
   *(Answer key: `instructor-keys/quiz-05.md`)*

7. When does the cleanup function returned from `useEffect` execute?
   a) Only when the browser tab is closed.  
   b) Before the effect re-runs due to dependency changes, and when the component unmounts from the DOM.  
   c) Immediately before the component's JSX renders.  
   d) Whenever a user clicks anywhere on the page.  
   *(Answer key: `instructor-keys/quiz-05.md`)*

8. Why is testing user interactions via `@testing-library/react` (e.g. `screen.getByRole('button')`) preferred over testing component internal state?
   a) Testing internal state is not supported in TypeScript.  
   b) Testing visible user behavior ensures tests don't break during internal implementation refactors and guarantees accessibility compliance.  
   c) React Testing Library is faster than unit tests.  
   d) Browser vendors mandate role-based testing.  
   *(Answer key: `instructor-keys/quiz-05.md`)*
