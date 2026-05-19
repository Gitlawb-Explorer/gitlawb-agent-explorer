# security policy

## supported versions

| Version | Supported          |
| ------- | ------------------ |
| 0.3.x   | :white_check_mark: |
| < 0.3   | :x:                |

## reporting a vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT open a public issue**
2. Email: gitlawbagent@gmail.com
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

## response timeline

- **Acknowledgment:** within 48 hours
- **Initial assessment:** within 1 week
- **Fix/patch:** depends on severity

## security considerations

This is a static HTML application with the following security notes:

- All agent data is hardcoded (mock data) — no server-side processing
- No authentication or authorization mechanisms
- No external API calls
- Clipboard API usage is sandboxed by browser security model
- Canvas rendering is isolated

## best practices

When contributing:

- Do not introduce external dependencies
- Do not add `eval()`, `innerHTML` with user input, or other XSS vectors
- Do not add tracking scripts or analytics
- Keep the single-file architecture
- All data should remain hardcoded or generated client-side
