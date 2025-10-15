# Environment Variable Guidelines

- Define secrets in Render dashboard, not in code.
- Use `SECRET_KEY`, `DATABASE_URL`, `API_KEY`, `JWT_SECRET`, etc.
- Never expose `.env` or config files publicly.
