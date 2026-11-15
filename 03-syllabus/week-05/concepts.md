# Week 05 Concepts

Master these 6 React and TypeScript principles. For each concept, practice explaining it aloud in your own words.

---

### 1. TypeScript Strict Mode & Narrowing
- **Plain words:** TypeScript compiles away at build time, leaving plain JavaScript. In `strict` mode, TypeScript prevents implicit `any` types, enforces null-checks (`value !== null`), and uses type narrowing (`typeof x === "string"`, discriminated unions) to guarantee type safety at compile time.
- **Explain it back prompt:** *"What is a discriminated union in TypeScript, and how does it prevent accessing invalid properties?"*

### 2. React Components as Pure Functions of Props and State
- **Plain words:** A React component is conceptually a pure mathematical function: given the same inputs (`props` and `state`), it should return the exact same JSX output. React compares previous and new virtual DOM trees to apply minimal updates to the real browser DOM.
- **Explain it back prompt:** *"Why should you never mutate state directly (e.g. `items.push(newItem)`) in React?"*

### 3. Component State (`useState`) & Immutability
- **Plain words:** When state changes via its setter function (`setCount(prev => prev + 1)`), React schedules a re-render of the component and its children. Because React detects changes by reference equality (`prev !== next`), state updates must create new objects or arrays rather than mutating existing memory in place.
- **Explain it back prompt:** *"Why does `const [user, setUser] = useState(...)` require `setUser({...user, name: 'Alice'})` instead of `user.name = 'Alice'`?"*

### 4. Side Effects & Synchronization (`useEffect`)
- **Plain words:** `useEffect` synchronizes a component with external systems (network requests, browser timers, event listeners). The dependency array `[depA, depB]` dictates when the effect re-runs. If dependencies change, React runs the cleanup function returned by the previous effect, then executes the new effect.
- **Explain it back prompt:** *"What causes an infinite render loop in `useEffect`, and how do you avoid it?"*

### 5. Asynchronous Data Fetching & Race Conditions
- **Plain words:** When user interactions trigger asynchronous fetches, responses may arrive out of order (e.g. searching for 'cat', then 'dog'; if 'cat' arrives last, the UI shows stale data). Proper effect architecture requires cleanup with `AbortController` or a boolean flag (`let active = true`).
- **Explain it back prompt:** *"How does an `AbortController` cancel an in-flight `fetch()` request when a component unmounts?"*

### 6. Controlled Components vs Uncontrolled Components
- **Plain words:** A controlled form input has its current value driven by React state (`value={name}` and `onChange={e => setName(e.target.value)}`), making React the single source of truth. An uncontrolled input retains its value in the DOM and is accessed via a `ref`.
- **Explain it back prompt:** *"What are the trade-offs between controlled inputs and uncontrolled inputs in React?"*
