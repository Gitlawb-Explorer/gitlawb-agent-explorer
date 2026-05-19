# contributing to gitlawb agent-explorer

Thanks for your interest in contributing! This document provides guidelines and steps for contributing.

## how to contribute

### reporting bugs

1. Check if the bug has already been reported in [issues](https://github.com/Gitlawb-Explorer/gitlawb-agent-explorer/issues)
2. If not, open a new issue using the [bug report template](https://github.com/Gitlawb-Explorer/gitlawb-agent-explorer/issues/new?template=bug_report.md)
3. Include as much detail as possible — steps to reproduce, expected vs actual behavior, screenshots

### suggesting features

1. Check if the feature has already been suggested in [issues](https://github.com/Gitlawb-Explorer/gitlawb-agent-explorer/issues)
2. If not, open a new issue using the [feature request template](https://github.com/Gitlawb-Explorer/gitlawb-agent-explorer/issues/new?template=feature_request.md)
3. Describe the problem you're trying to solve and your proposed solution

### submitting code

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test thoroughly in multiple browsers
5. Commit with a clear message: `git commit -m "feat: add your feature"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Open a Pull Request using the PR template

## code guidelines

### general

- **Single file only** — all CSS, JS, and HTML must remain in `index.html`
- **No external dependencies** — vanilla JS only, no frameworks or libraries
- **No build step** — the file must work when opened directly in a browser

### HTML

- Use semantic HTML elements
- Include ARIA attributes where appropriate
- Maintain proper indentation (2 spaces)

### CSS

- Follow the existing dark zinc palette (`#09090b` base)
- Use `Geist` for body text, `JetBrains Mono` for code/data
- Use semantic colors only — no decorative gradients or flashy effects
- Mobile-first responsive design

### JavaScript

- Use vanilla JS only
- Prefer event delegation over inline event handlers
- Clean up intervals and event listeners when possible
- Use `const` and `let`, avoid `var`
- No `console.log`, `console.error`, or `console.warn` in production

### design system

- Lowercase text where appropriate
- Flat dark surfaces
- Semantic color coding (green=good, red=bad, purple=accent)
- Minimal animations — only functional transitions
- Inspired by Linear, Vercel, and terminal aesthetics

## commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new feature
fix: fix a bug
docs: update documentation
style: formatting changes
refactor: code refactoring
perf: performance improvement
test: add tests
chore: maintenance tasks
```

## code of conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## questions?

Open an issue with the `question` label if you need help.
